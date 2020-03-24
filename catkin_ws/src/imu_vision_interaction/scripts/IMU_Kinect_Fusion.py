#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from imu_vision_interaction.msg import kinect_msg
import cv2


def imu_callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' - I heard %s', data.data)


def imscrews_callback(data):
    rospy.loginfo(f"{rospy.get_caller_id()} - Safe Move: {data.safe_move} \n"
                  f"Image Screw Predictions: {data.im_screw_probs_1}\n"
                  f"                         {data.im_screw_probs_2} \n"
                  f"                         {data.im_screw_probs_3} \n"
                  f"                         {data.im_screw_probs_4} \n")


def IMU_listener():
    rospy.init_node('IMU_listener', anonymous=True)

    rospy.Subscriber('IMU_Data', String, imu_callback)
    rospy.Subscriber('Image_Screws', kinect_msg, imscrews_callback)

    rospy.spin()


if __name__ == '__main__':
    IMU_listener()
