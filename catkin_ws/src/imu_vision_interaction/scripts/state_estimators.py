#!/usr/bin/env python3

# import the necessary packages
import numpy as np


def im_state_est(im_screw_hst):

    im_count = [None, None]

    #Could add probabilities to bin count as weight parameter?
    screw_bins = np.bincount(np.array(im_screw_hst[:, 1], dtype=np.int))
    bolt_bins = np.bincount(np.array(im_screw_hst[:, 2], dtype=np.int))

    im_count[0] = np.argmax(screw_bins)
    im_count[1] = np.argmax(bolt_bins)
    return im_count


def imu_state_est(imu_state_hist):
    #print(f"1: {imu_state_hist}")
    #'Dilation' filter to remove single erroneous predictions
    if imu_state_hist[-1] == imu_state_hist[-3]:
        imu_state_hist[-2] = imu_state_hist[-1]

    #Group predictions of same type together
    if imu_state_hist[-2] == imu_state_hist[-3]:
        imu_state_hist = np.delete(imu_state_hist, -2)

    #print(f"2: {imu_state_hist}")
    return imu_state_hist


def current_state_est(im_screw_hist, imu_state_hist):
    imu_state_hist = imu_state_est(imu_state_hist)
    count = np.bincount(np.array(imu_state_hist, dtype=np.int))
    #print(f"Count:{count}")
    imu_count = [None, None]
    imu_count[0] = count[2]
    imu_count[1] = count[0]
    im_count = im_state_est(im_screw_hist)

    state_est = [None, None]
    state_est[0] = round(np.mean([imu_count[0], im_count[0]]))  # screws
    state_est[1] = round(np.mean([imu_count[1], im_count[1]]))  # bolts
    print(f"IMU:{imu_count} IM:{im_count} Final:{state_est}")
    return state_est, imu_state_hist
