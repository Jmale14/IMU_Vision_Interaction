#!/usr/bin/env python3

# import the necessary packages
import numpy as np


def im_state_est(im_screw_hst):
    #Could add probabilities to bin count as weight parameter?
    screw_bins = np.bincount(np.array(im_screw_hst[:, 1], dtype=np.int))
    bolt_bins = np.bincount(np.array(im_screw_hst[:, 2], dtype=np.int))

    im_count = [0, 0]
    try:
        im_count[0] = np.argmax(screw_bins)
    except ValueError:
        pass
    try:
        im_count[1] = np.argmax(bolt_bins)
    except ValueError:
        pass

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


def current_state_est(im_screw_hist, imu_state_hist, state_est):
    imu_state_hist = imu_state_est(imu_state_hist)
    imu_count = np.bincount(np.array(imu_state_hist, dtype=np.int))
    #print(f"Count:{count}")
    state_est._imu = np.vstack((state_est._imu, [imu_count[2], imu_count[0]]))
    state_est._im = np.vstack((state_est._im, im_state_est(im_screw_hist)))

    final_est = [None, None]
    final_est[0] = round(np.mean([state_est._imu[-1, 0], state_est._im[-1, 0]]))  # screws
    final_est[1] = round(np.mean([state_est._imu[-1, 1], state_est._im[-1, 1]]))  # bolts
    state_est._final = np.vstack((state_est._final, final_est))
    print(f"IMU:{state_est._imu[-1, :]} IM:{state_est._im[-1, :]} Final:{state_est._final[-1, :]}")

    return state_est, imu_state_hist
