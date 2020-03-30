#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int8, Float64
from imu_vision_interaction.msg import kinect_msg, IMU_msg
import cv2
import numpy as np
import time
from state_estimators import current_state_est
import argparse
import matplotlib.pyplot as plt


imu_pred = np.zeros(5)
im_screw_hist = np.zeros((1, 3), dtype=np.int)
timer = time.time()
imu_state_hist = np.array([4, 4, 4], dtype=np.int)
CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
pos = np.arange(len(CATEGORIES))

parser = argparse.ArgumentParser(
        description='Fusion of screw/bolt state estimation from IMU and vision sources')

parser.add_argument('--disp', '-V',
                    help='Enable graph of predictions over time',
                    default=None,
                    action="store_true")

args = parser.parse_args()

if args.disp:
    plt.ion()
    fig, axs = plt.subplots(2, 2)


class StateEst:
    def __init__(self):
        self._final = [None, None]
        self._im = [None, None]
        self._imu = [None, None]


def plot_estimation():
    global state_est
    global CATEGORIES
    legend = ['Image', 'IMU', 'Final']
    Titles = ['Total No. Screws', 'Total No. Bolts']
    global axs
    for i in range(0, 2):
        ax = axs[0, i]
        ax.cla()
        ax.plot(state_est._im[:, i])
        ax.plot(state_est._imu[:, i])
        ax.plot(state_est._final[:, i])
        ax.set_ylabel('Estimated Number')
        ax.set_title(Titles[i])
        ax.legend(legend)
        ax.set_ylim(bottom=0)

    ax = axs[1, 0]
    ax.cla()
    ax.bar(pos, imu_pred, align='center', alpha=0.5)
    ax.set_xticks(pos)
    ax.set_xticklabels(CATEGORIES)
    ax.set_ylabel('Confidence')
    ax.set_ylim([0, 1])
    ax.set_title('Current IMU Prediction')

    ax = axs[1, 1]
    ax.cla()
    ax.bar([1, 2], [im_screw_hist[-1, 1], im_screw_hist[-1, 2]], align='center', alpha=0.5)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(['Screws', 'Bolts'])
    ax.set_ylabel('Confidence')
    ax.set_ylim([0, 4])
    ax.set_title('Current image Prediction')

    plt.pause(0.0001)



state_est = StateEst()


def imu_callback(data):
    global imu_state_hist
    global im_screw_hist
    global state_est
    global imu_pred
    imu_pred = data.imu_msg
    imu_state_hist = np.hstack((imu_state_hist, np.argmax(imu_pred)))
    #rospy.loginfo(rospy.get_caller_id() + ' - I heard %s', data.data)

    cutoff_t = time.time() - 5
    im_screw_hist = np.delete(im_screw_hist, np.where(im_screw_hist[:, 0] < cutoff_t)[0], axis=0)

    state_est, imu_state_hist = current_state_est(im_screw_hist, imu_state_hist, state_est)

    if args.disp:
        plot_estimation()


def imscrews_callback(data):
    global im_screw_hist
    im_screw_hist = np.vstack((im_screw_hist, [time.time(), data.tally[0], data.tally[2]]))
    # rospy.loginfo(f"{rospy.get_caller_id()}:"
    #               f"    Safe Move: {data.safe_move} \n"
    #               f"    Image Screw Predictions: {data.im_screw_probs_1} \n"
    #               f"                             {data.im_screw_probs_2} \n"
    #               f"                             {data.im_screw_probs_3} \n"
    #               f"                             {data.im_screw_probs_4} \n"
    #               f"    Predictions Tally: {data.tally}")


def IMU_listener():

    rospy.init_node('IMU_listener', anonymous=True)

    rospy.Subscriber('IMU_Data', IMU_msg, imu_callback)
    rospy.Subscriber('Image_Screws', kinect_msg, imscrews_callback)


    # if time.time() - timer > 0.5:
    #     cutoff_t = time.time() - 5
    #     np.delete(im_screw_hst, np.where(im_screw_hst[:, 0] < cutoff_t)[0], axis=0)
    #
    #     global imu_state_hist
    #     state_est, imu_state_hist = current_state_est(im_screw_hst, imu_state_hist)
    #
    #     timer = time.time()

    rospy.spin()



if __name__ == '__main__':
    print("Starting Fusion Node")
    IMU_listener()
