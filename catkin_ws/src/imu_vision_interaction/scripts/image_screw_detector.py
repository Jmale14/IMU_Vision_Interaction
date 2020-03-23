# https://www.learnopencv.com/blob-detection-using-opencv-python-c/
# Paper 'Multimodal Control for Human-Robot Cooperation'
# https://github.com/ShubhamCpp/Circle-Detection-in-Real-Time

# import the necessary packages
import numpy as np
import argparse
import cv2
import time
import freenect
import frame_convert2
from datetime import datetime
import os
from tensorflow.keras.models import load_model
from sklearn.neighbors import NearestNeighbors

class ImScrewDetector:
    def __init__(self):
        self._size = 28
        self._CATEGORIES = ['screw_full', 'screw_empty', 'bolt_full', 'bolt_empty', 'null']

        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()
        # Change thresholds
        params.filterByColor = 1;
        params.blobColor = 0;
        # Filter by Area.
        params.filterByArea = 1
        params.minArea = 200
        # Filter by Circularity
        params.filterByCircularity = 1
        params.minCircularity = 0.2
        # Filter by Convexity
        params.filterByConvexity = 1
        params.minConvexity = 0.87
        # Filter by Inertia
        params.filterByInertia = 1
        params.minInertiaRatio = 0.3

        # Create a detector with the parameters
        ver = cv2.__version__.split('.')
        if int(ver[0]) < 3:
            self._detector = cv2.SimpleBlobDetector(params)
        else:
            self._detector = cv2.SimpleBlobDetector_create(params)

        # load model
        model = load_model('Screw_Model.h5')
        # summarize model.
        model.summary()
        self._model = model
        self._lasttime = 0

    def rot_crop(self, image, pts, box, x, y):
        width = int(pts[1][0])
        height = int(pts[1][1])
        src_pts = box.astype("float32")
        dst_pts = np.array([[0, height - 1],
                            [0, 0],
                            [width - 1, 0],
                            [width - 1, height - 1]], dtype="float32")
        m = cv2.getPerspectiveTransform(src_pts, dst_pts)
        out = cv2.warpPerspective(image, m, (width, height))
        out = cv2.resize(out, (x, y))
        return out

    def save_img(self, image):
        path = os.getcwd()
        os.chdir(path + '/raw_data')
        timestr = datetime.now().strftime("%Y%m%d-%H%M%S%f")
        cv2.imwrite(timestr + '.jpg', image)
        os.chdir(path)

    def find_four_closest(self, pointpts):
        n = 0
        nearestpoints = [None]*len(pointpts)
        no_neigh = len(pointpts)
        if no_neigh > 4:
            no_neigh = 4
        neigh = NearestNeighbors(n_neighbors=no_neigh)
        neigh.fit(pointpts)
        distances, indices = neigh.kneighbors(pointpts)

        neigh = NearestNeighbors(n_neighbors=no_neigh)
        neigh.fit(distances)
        distances2, indices2 = neigh.kneighbors(distances)

        scores = np.std(distances2, axis=0)# * np.mean(distances2, axis=0)
        pointidx = np.argmin(scores)
        closestptsidx = indices2[pointidx]
        return closestptsidx

    def detect_screws(self, frame):
        grayIN = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # apply GuassianBlur to reduce noise. medianBlur is also added for smoothening, reducing noise.
        gray = cv2.GaussianBlur(grayIN, (3, 3), 0)
        gray = cv2.medianBlur(gray, 5)

        ddepth = cv2.CV_64F

        # Gradient X
        grad_x = cv2.Sobel(gray, ddepth, 1, 0, 3)
        #abs_grad_x = cv2.convertScaleAbs(grad_x)
        # Gradient Y
        grad_y = cv2.Sobel(gray, ddepth, 0, 1, 3)
        #abs_grad_y = cv2.convertScaleAbs(grad_y)
        # Total Gradient (approximate)
        grad = cv2.magnitude(grad_x, grad_y)
        grad = cv2.convertScaleAbs(grad)

        # Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
        gray = cv2.adaptiveThreshold(grad, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv2.THRESH_BINARY, 11, 15)

        gray = cv2.medianBlur(gray, 3)
        kernel = np.ones((3, 3), np.uint8)
        gray = cv2.erode(gray, kernel, iterations=4)

        # Detect blobs.
        keypoints = self._detector.detect(gray)

        listpoints = []
        pointpts = np.zeros((len(keypoints), 2))
        p = 0
        for point in keypoints:
            listpoints.append(point)
            pointpts[p] = [point.pt[0], point.pt[1]]
            p = p+1

        i = 0
        guesses = [None] * len(keypoints)
        for point in keypoints:
            rect = ((point.pt[0], point.pt[1]), (point.size, point.size), 0)
            box_pts = np.int0(cv2.boxPoints(rect))
            image = self.rot_crop(grayIN, rect, box_pts, self._size, self._size)
            image = image.reshape(1, 28, 28, 1)
            guess = self._model.predict_proba(image)
            guesses[i] = guess[0]
            i = i + 1

        i = 0
        #screw_probs = np.zeros(4)
        fourkeypoints = [None] * 4
        tally = np.zeros(5)

        if len(pointpts) > 0:
            closestptsidx = self.find_four_closest(pointpts)

            for p in range(0, len(closestptsidx)):
                idx = closestptsidx[p]
                if np.max(guesses[idx]) > 0.999999:
                    guess = int(np.argmax(guesses[idx]))
                    tally[guess] = tally[guess] + 1
                    if guess == 4:
                        pass
                    else:
                        #screw_probs[p] = prob
                        fourkeypoints[p] = keypoints[idx]

                        txt = f"{self._CATEGORIES[guess]}"
                        frame = cv2.drawKeypoints(frame, fourkeypoints, np.array([]), (0, 0, 255),
                                                  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                        frame = cv2.putText(frame, txt, (int(keypoints[idx].pt[0]), int(keypoints[idx].pt[1])),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

                i = i + 1

        # for g in guesses:
        #     prob = np.max(g)
        #     guess = int(np.argmax(g))
        #     if guess == 4:
        #         tally[4] = tally[4]+1
        #         pass
        #     else:
        #         if guess == 0 | guess == 1:
        #             # Screw
        #             tally[guess] = tally[guess] + 1
        #             if prob >= np.min(screw_probs):
        #                 screw_probs[np.argmin(screw_probs)] = prob
        #                 fourkeypoints[np.argmin(screw_probs)] = keypoints[i]
        #
        #                 txt = f"{self._CATEGORIES[guess]}"
        #                 frame = cv2.drawKeypoints(frame, fourkeypoints, np.array([]), (0, 0, 255),
        #                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #                 frame = cv2.putText(frame, txt, (int(keypoints[i].pt[0]), int(keypoints[i].pt[1])),
        #                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        #
        #         else:
        #             # Bolt
        #             tally[guess] = tally[guess] + 1
        #             if prob >= bolt_probs:
        #                 bolt_probs = prob
        #                 fourkeypoints[3] = keypoints[i]
        #
        #                 txt = f"{self._CATEGORIES[guess]}"
        #                 frame = cv2.drawKeypoints(frame, fourkeypoints, np.array([]), (0, 0, 255),
        #                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #                 frame = cv2.putText(frame, txt, (int(keypoints[i].pt[0]), int(keypoints[i].pt[1])),
        #                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        #
        #     i = i + 1

        # Display the resulting frame
        cv2.imshow("Circles", frame)
        im_screw_probs = np.empty((4, 5))



        i = 0;
        for point in fourkeypoints:
            if point is not None:
                pointint = listpoints.index(point)
                im_screw_probs[i] = guesses[pointint]
            i = i+1

        if time.time() - self._lasttime > 1:
            print(tally)
            self._lasttime = time.time()

        return im_screw_probs
