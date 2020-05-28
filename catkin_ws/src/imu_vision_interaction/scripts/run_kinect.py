#!/usr/bin/env python3

# Build stuff
#cd~/libfreenect/wrappers/python
#Global Install: sudo python setup.py install
#Local Directory Install: python setup.py build_ext --inplace

# Import Statements
import freenect
import frame_convert2
import numpy as np
import traceback
import argparse
import sys
import time
import cv2
import rospy
from imu_vision_interaction.msg import kinect_msg
from image_screw_detector import ImScrewDetector  # Image screw detector class

def scale(image):
    height, width, channels = image.shape
    scale = 2  # x? digital zoom
    centerX, centerY = int(height / 2), int(width / 2)
    radiusX, radiusY = int(height / (scale * 2)), int(width / (scale * 2))
    minX, maxX = centerX - radiusX, centerX + radiusX
    minY, maxY = centerY - radiusY, centerY + radiusY
    image = cv2.resize(image[minX:maxX, minY:maxY], (width, height), interpolation=cv2.INTER_LINEAR)
    return image

def kinect_run():
    # ROS node setup
    pub = rospy.Publisher('Image_Screws', kinect_msg, queue_size=1)
    rospy.init_node('Kinect_Main', anonymous=True)
    rate = rospy.Rate(10)
    msg = kinect_msg()
    status = 3  # Current status = setting up
    try:
        im_screw_detect = ImScrewDetector()
    except Exception:
        print("**Screw Detect Error**")
        status = 0
        traceback.print_exc(file=sys.stdout)

    while not rospy.is_shutdown():
        try:
            image = np.array(frame_convert2.video_cv(freenect.sync_get_video()[0]))
            image = scale(image)

            status = 1  # Status ready
        except TypeError as e:
            time.sleep(1)
        except Exception as e:
            print("**Get Image Error**")
            status = 0  # error status
            traceback.print_exc(file=sys.stdout)
            break

        im_screw_states, tally = im_screw_detect.detect_screws(image, args.disp)
        im_screw_states = im_screw_states.tolist()

        # For each of 4 points, probability is each of 5 classes
        # ['screw_full', 'screw_empty', 'bolt_full', 'bolt_empty', 'null']
        msg.im_screw_probs_1 = im_screw_states[0]
        msg.im_screw_probs_2 = im_screw_states[1]
        msg.im_screw_probs_3 = im_screw_states[2]
        msg.im_screw_probs_4 = im_screw_states[3]
        msg.tally = tally  # Bolts and Screws Tally
        msg.im_stat = status  # Vision status no.

        msg.safe_move = False  # future use variable for robot
        pub.publish(msg)
        rate.sleep()


## Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run Screw recognition ROS node')

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
