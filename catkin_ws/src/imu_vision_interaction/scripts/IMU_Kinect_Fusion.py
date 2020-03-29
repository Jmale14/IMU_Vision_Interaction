#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int8
from imu_vision_interaction.msg import kinect_msg
import cv2
import numpy as np
import time
from state_estimators import current_state_est
import argparse
import matplotlib.pyplot as plt


im_screw_hist = np.zeros((1, 3), dtype=np.int)
timer = time.time()
imu_state_hist = np.array([4, 4, 4], dtype=np.int)
CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']

parser = argparse.ArgumentParser(
        description='Fusion of screw/bolt state estimation from IMU and vision sources')

parser.add_argument('--disp', '-V',
                    help='Enable graph of predictions over time',
                    default=None,
                    action="store_true")

args = parser.parse_args()

if args.disp:
    plt.ion()
    fig, axs = plt.subplots(2)


class StateEst:
    def __init__(self):
        self._final = [None, None]
        self._im = [None, None]
        self._imu = [None, None]


def plot_estimation():
    global state_est
    legend = ['Image', 'IMU', 'Final']
    Titles = ['Screws', 'Bolts']
    global axs
    for i in range(0, 2):
        ax = axs[i]
        ax.cla()
        ax.plot(state_est._im[:, i])
        ax.plot(state_est._imu[:, i])
        ax.plot(state_est._final[:, i])
        ax.set_ylabel('Estimated Number')
        ax.set_title(Titles[i])
        ax.legend(legend)

    plt.pause(0.0001)


state_est = StateEst()


def imu_callback(data):
    global imu_state_hist
    global im_screw_hist
    global state_est
    imu_state_hist = np.hstack((imu_state_hist, data.data))
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

    rospy.Subscriber('IMU_Data', Int8, imu_callback)
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
