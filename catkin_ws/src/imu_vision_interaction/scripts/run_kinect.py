#!/usr/bin/env python3

# Build stuff
#cd~/libfreenect/wrappers/python
#Global Install: sudo python setup.py install
#Local Directory Install: python setup.py build_ext --inplace

# Import Statements
import freenect
import frame_convert2
import threading
import numpy as np
import traceback
import argparse
import sys
import time
import cv2
import rospy
from std_msgs.msg import String, Bool
from imu_vision_interaction.msg import kinect_msg
from image_screw_detector import ImScrewDetector


def kinect_run():
    # Camera
    camera = None
    pub = rospy.Publisher('Image_Screws', kinect_msg, queue_size=1)
    rospy.init_node('Kinect_Main', anonymous=True)
    rate = rospy.Rate(10)
    msg = kinect_msg()
    status = 3
    try:
        im_screw_detect = ImScrewDetector()
    except Exception:
        print("**Screw Detect Error**")
        status = 0
        traceback.print_exc(file=sys.stdout)

    while not rospy.is_shutdown():
        try:
            image = np.array(frame_convert2.video_cv(freenect.sync_get_video()[0]))
            status = 1
        except TypeError as e:
            time.sleep(1)
        except Exception as e:
            print("**Get Image Error**")
            status = 0
            traceback.print_exc(file=sys.stdout)
            break

        im_screw_states, tally = im_screw_detect.detect_screws(image, args.disp)
        im_screw_states = im_screw_states.tolist()
        # safe_move = camera.safetomove(image)  # Needs work

        msg.im_screw_probs_1 = im_screw_states[0]
        msg.im_screw_probs_2 = im_screw_states[1]
        msg.im_screw_probs_3 = im_screw_states[2]
        msg.im_screw_probs_4 = im_screw_states[3]
        msg.tally = tally
        msg.im_stat = status

        msg.safe_move = False
        pub.publish(msg)
        rate.sleep()


## Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Vision Processing System for IMechE UAS Challenge')

    parser.add_argument('--disp', '-V',
                        help='Enable displaying of camera image',
                        default=None,
                        action="store_true")

    args = parser.parse_args()

    try:
        kinect_run()
    except rospy.ROSInterruptException:
        print("run_kinect ROS exception")
    except Exception as e:
        print("**Image Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        cv2.destroyAllWindows()
