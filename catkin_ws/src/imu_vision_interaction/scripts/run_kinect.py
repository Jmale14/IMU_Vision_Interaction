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
from std_msgs.msg import String, Float64MultiArray
from rospy.numpy_msg import numpy_msg
from image_screw_detector import ImScrewDetector
from std_msgs.msg import MultiArrayDimension
#from cv_bridge.boost.cv_bridge_boost import getCvType


def kinect_run():
    # Camera
    camera = None
    pub = rospy.Publisher('Image_Screws', Float64MultiArray, queue_size=1)
    rospy.init_node('Kinect_Main', anonymous=True)
    rate = rospy.Rate(10)
    try:
        im_screw_detect = ImScrewDetector()
    except Exception:
        print("**Screw Detect Error**")
        traceback.print_exc(file=sys.stdout)


    while not rospy.is_shutdown():
        try:
            image = np.array(frame_convert2.video_cv(freenect.sync_get_video()[0]))
            if args.disp:
                cv2.imshow('Image', image)
                if cv2.waitKey(10) == 27:
                    break
        except TypeError as e:
            time.sleep(1)
        except Exception as e:
            print("**Get Image Error**")
            traceback.print_exc(file=sys.stdout)
            break


        im_screw_states = im_screw_detect.detect_screws(image)

        # safe_move = camera.safetomove(image)  # Needs work
        #im_screw_states = Float64MultiArray(data=im_screw_states)
        pub_states.data = im_screw_states.tolist()
        pub.publish(pub_states)
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
