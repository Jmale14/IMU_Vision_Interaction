#import statements
import freenect
import frame_convert2
import numpy as np
import time
import cv2


class Camera:
    def __init__(self):
        time.sleep(2)
        pass

    def framegrab(self):
        image = np.array(frame_convert2.video_cv(freenect.sync_get_video()[0]))
        return image


    def Kill(self):
        raise freenect.Kill()
        pass
