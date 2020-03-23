import imageFunctions # import Camera
from image_screw_detector import ImScrewDetector
import traceback
import sys
import freenect
import cv2
import frame_convert2
import numpy as np

# Camera
cam = None
try:
    camera = imageFunctions.Camera()
except Exception:
    print("**Image Error**")
    traceback.print_exc(file=sys.stdout)

try:
    im_screw_detect = ImScrewDetector()
except Exception:
    print("**Screw Detect Error**")
    traceback.print_exc(file=sys.stdout)

while 1:
    image = camera.framegrab()
    #print(np.shape(image))
    #cv2.imshow('image', image)
    if cv2.waitKey(10) == 27:
        break
    # try:
    #
    #     cv2.imshow("mainIm", image)
    # except Exception:
    #     print("**Grabbing Error**")
    #     traceback.print_exc(file=sys.stdout)
    #     camera.Kill()


    im_screw_states = im_screw_detect.detect_screws(image)

cv2.destroyAllWindows()