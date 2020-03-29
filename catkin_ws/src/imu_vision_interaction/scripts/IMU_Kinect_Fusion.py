#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int8
from imu_vision_interaction.msg import kinect_msg
import cv2
import numpy as np
import time
from state_estimators import current_state_est

im_screw_hist = np.zeros((1, 3), dtype=np.int)
timer = time.time()
imu_state_hist = np.array([4, 4, 4], dtype=np.int)
CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']


def imu_callback(data):
    global imu_state_hist
    global im_screw_hist
    imu_state_hist = np.hstack((imu_state_hist, data.data))
    #rospy.loginfo(rospy.get_caller_id() + ' - I heard %s', data.data)

    cutoff_t = time.time() - 5
    im_screw_hist = np.delete(im_screw_hist, np.where(im_screw_hist[:, 0] < cutoff_t)[0], axis=0)

    state_est, imu_state_hist = current_state_est(im_screw_hist, imu_state_hist)


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
