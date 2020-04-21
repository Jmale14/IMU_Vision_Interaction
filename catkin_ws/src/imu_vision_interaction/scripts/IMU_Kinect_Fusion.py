#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int8, Float64
from imu_vision_interaction.msg import kinect_msg, IMU_msg, gui_msg
import cv2
import numpy as np
import time
from state_estimators import current_state_est
import argparse
import matplotlib.pyplot as plt

CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
pos = np.arange(len(CATEGORIES))

# parser = argparse.ArgumentParser(
#         description='Fusion of screw/bolt state estimation from IMU and vision sources')
#
# parser.add_argument('--disp', '-V',
#                     help='Enable graph of predictions over time',
#                     default=None,
#                     action="store_true")
#
# args = parser.parse_args()
#
# if args.disp:
#     plt.ion()
#     fig, axs = plt.subplots(2, 2)
#
#

#
#
# def plot_estimation():
#     global state_est
#     global CATEGORIES
#     legend = ['Image', 'IMU', 'Final']
#     Titles = ['Total No. Screws', 'Total No. Bolts']
#     global axs
#     for i in range(0, 2):
#         ax = axs[0, i]
#         ax.cla()
#         ax.plot(state_est._im[:, i])
#         ax.plot(state_est._imu[:, i])
#         ax.plot(state_est._final[:, i])
#         ax.set_ylabel('Estimated Number')
#         ax.set_title(Titles[i])
#         ax.legend(legend)
#         ax.set_ylim(bottom=0)
#
#     ax = axs[1, 0]
#     ax.cla()
#     ax.bar(pos, imu_pred, align='center', alpha=0.5)
#     ax.set_xticks(pos)
#     ax.set_xticklabels(CATEGORIES)
#     ax.set_ylabel('Confidence')
#     ax.set_ylim([0, 1])
#     ax.set_title('Current IMU Prediction')
#
#     ax = axs[1, 1]
#     ax.cla()
#     ax.bar([1, 2], [im_screw_hist[-1, 1], im_screw_hist[-1, 2]], align='center', alpha=0.5)
#     ax.set_xticks([1, 2])
#     ax.set_xticklabels(['Screws', 'Bolts'])
#     ax.set_ylabel('Confidence')
#     ax.set_ylim([0, 4])
#     ax.set_title('Current image Prediction')
#
#     plt.pause(0.0001)
#
#
#
# state_est = StateEst()


class FusionListener:
    def __init__(self):
        self._imu_pred = np.zeros(5)
        self._imu_pred_hist = np.empty(5)
        self._im_screw_hist = np.zeros((1, 5))
        self._timer = time.time()
        self._imu_state_hist = np.array([4, 1])
        self._im_stat = 2
        self._imu_stat = [2, 2, 2, 2]
        self._state_est = self.StateEst()
        self._no_completed = 0

        self.pub = rospy.Publisher('gui_Data', gui_msg, queue_size=1)
        self.imu_sub = rospy.Subscriber('IMU_Data', IMU_msg, self.imu_callback)
        self.im_sub = rospy.Subscriber('Image_Screws', kinect_msg, self.imscrews_callback)
        self.gui_sub = rospy.Subscriber('completed_parts', Int8, self.gui_callback)

    class StateEst:
        def __init__(self):
            self._final = np.zeros(2)
            self._im = np.zeros(2)
            self._imu = np.zeros(2)

    def imu_callback(self, data):
        self._imu_stat = data.imu_stat
        self._imu_pred = data.imu_msg
        self._imu_state_hist = np.vstack((self._imu_state_hist, [np.argmax(self._imu_pred), 0]))
        self._imu_pred_hist = np.vstack((self._imu_pred_hist, self._imu_pred))
        #rospy.loginfo(rospy.get_caller_id() + ' - I heard %s', data.data)
        self.fusion()

        # if args.disp:
        #     plot_estimation()

    def imscrews_callback(self, data):
        self._im_stat = data.im_stat
        screw_probs = [data.im_screw_probs_1, data.im_screw_probs_2, data.im_screw_probs_3, data.im_screw_probs_4]
        screw_sum = 0
        bolt_prob = 0
        for entry in screw_probs:
            if np.argmax(entry) == 0:
                screw_sum += entry[0]
            elif (np.argmax(entry) == 2) & (entry[2] >= bolt_prob):
                bolt_prob = entry[2]
        self._im_screw_hist = np.vstack((self._im_screw_hist, [time.time(), data.tally[0], data.tally[2], screw_sum, bolt_prob]))
        cutoff_t = time.time() - 1
        self._im_screw_hist = np.delete(self._im_screw_hist, np.where(self._im_screw_hist[:, 0] < cutoff_t)[0], axis=0)
        self.fusion()
        # rospy.loginfo(f"{rospy.get_caller_id()}:"
        #               f"    Safe Move: {data.safe_move} \n"
        #               f"    Image Screw Predictions: {data.im_screw_probs_1} \n"
        #               f"                             {data.im_screw_probs_2} \n"
        #               f"                             {data.im_screw_probs_3} \n"
        #               f"                             {data.im_screw_probs_4} \n"
        #               f"    Predictions Tally: {data.tally}")

    def gui_callback(self, data):
        if data.data != self._no_completed:
            self._no_completed = data.data
            self._state_est = self.StateEst()

    def pub_message(self):
        rate = rospy.Rate(10)
        msg = gui_msg()
        msg.imu_stat = self._imu_stat
        msg.kin_stat = self._im_stat
        msg.state_est_final = np.round(self._state_est._final).astype(int)
        msg.state_est_im = np.round(self._state_est._im).astype(int)
        msg.state_est_imu = np.round(self._state_est._imu).astype(int)
        msg.imu_pred = self._imu_pred
        msg.im_pred = [self._im_screw_hist[-1, 1], self._im_screw_hist[-1, 2]]
        self.pub.publish(msg)
        if time.time() - self._timer > 1:
            print(f"IMU:{self._state_est._imu} IM:{self._state_est._im} Final:{self._state_est._final}")
            self._timer = time.time()
        rate.sleep()

    def fusion(self):
        self._state_est, self._imu_state_hist, self._imu_pred_hist = \
            current_state_est(self._im_screw_hist, self._imu_state_hist, self._state_est, self._im_stat, self._imu_stat, self._imu_pred_hist)
        self.pub_message()


def main():
    rospy.init_node('fusion_listener', anonymous=True)
    fusion_inst = FusionListener()
    rospy.spin()


if __name__ == '__main__':
    print("Starting Fusion Node")
    main()
