#!/usr/bin/env python3

# import the necessary packages
import numpy as np


def im_state_est(im_screw_hst):
    #Could add probabilities to bin count as weight parameter?
    screw_bins = np.bincount(np.array(im_screw_hst[:, 1], dtype=np.int))
    bolt_bins = np.bincount(np.array(im_screw_hst[:, 2], dtype=np.int))

    im_count = [0, 0]
    try:
        im_count[0] = int(np.argmax(screw_bins))
        if im_count[1] > 3:
            im_count[1] = 3
    except ValueError:
        pass
    try:
        im_count[1] = int(np.argmax(bolt_bins))
        if im_count[1] > 1:
            im_count[1] = 1
    except ValueError:
        pass

    return im_count


def imu_state_est(imu_state_hist):
    #print(f"1: {imu_state_hist}")
    #'Dilation' filter to remove single erroneous predictions
    if np.shape(imu_state_hist)[0] > 3:
        if imu_state_hist[-1] == imu_state_hist[-3]:
            imu_state_hist[-2] = imu_state_hist[-1]

        #Group predictions of same type together
        if imu_state_hist[-2] == imu_state_hist[-3]:
            imu_state_hist = np.delete(imu_state_hist, -2)

    #print(f"2: {imu_state_hist}")
    return imu_state_hist


def current_state_est(im_screw_hist, imu_state_hist, state_est, im_stat, imu_stat):
    if all((i == 1) for i in imu_stat):
        imu_state_hist = imu_state_est(imu_state_hist)
        imu_count = np.bincount(np.array(imu_state_hist, dtype=np.int))
        # print(f"Count:{count}")
        if imu_count[2] > 3:
            imu_count[2] = 3
        if imu_count[0] > 1:
            imu_count[0] = 1
        state_est._imu = [int(imu_count[2]), int(imu_count[0])]

    if im_stat == 1:
        state_est._im = im_state_est(im_screw_hist)

    if (im_stat == 1) & all((i == 1) for i in imu_stat):
        final_est = [None, None]
        final_est[0] = int(round(np.mean([state_est._imu[0], state_est._im[0]])))  # screws
        if final_est[0] > 3:
            final_est[0] = 3
        final_est[1] = int(round(np.mean([state_est._imu[1], state_est._im[1]])))  # bolts
        if final_est[1] > 1:
            final_est[1] = 1
        state_est._final = final_est
    #print(f"IMU:{state_est._imu} IM:{state_est._im} Final:{state_est._final}")

    return state_est, imu_state_hist
