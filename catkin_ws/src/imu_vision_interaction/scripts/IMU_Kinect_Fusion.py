#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64MultiArray
from rospy.numpy_msg import numpy_msg
import cv2


def imu_callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' - I heard %s', data.data)


def imscrews_callback(data):
    rospy.loginfo(f"{rospy.get_caller_id()} - Image Screw Predictions: {data.data}")
    return image

def IMU_listener():
    rospy.init_node('IMU_listener', anonymous=True)

    rospy.Subscriber('IMU_Data', String, imu_callback)
    rospy.Subscriber('Image_Screws', Float64MultiArray, imscrews_callback)

    rospy.spin()


if __name__ == '__main__':
    IMU_listener()



#
# try:
#     im_screw_detect = ImScrewDetector()
# except Exception:
#     print("**Screw Detect Error**")
#     traceback.print_exc(file=sys.stdout)
#
# while True:
#
#     try:
#         image = camera.framegrab()
#     except Exception as e:
#         traceback.print_exc(file=sys.stdout)
#         time.sleep(1)
#
#     if cv2.waitKey(10) == 27:
#         break
#
#     # current_action = findaction(actions, IMUdata)  # Needs work
#
#     # prev_actions = prev_actions.append(current_action)  # Needs work
#
#     im_screw_states = im_screw_detect.detect_screws(image)
#
#     # final_screws = finalscrewstates(im_screws, prev_actions)  # Needs work
#
#     # safe_move = camera.safetomove(image)  # Needs work
#
#     # robot_state = robotstateupdate(final_screws, safe_move)  # Needs work
#
#     if robot_state == 'change_side':
#         prev_actions = []
#
# cv2.destroyAllWindows()
