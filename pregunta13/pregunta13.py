#!/usr/bin/env python3

import numpy as np
import cv2 as cv

img = cv.imread('lenna.jpg', cv.IMREAD_GRAYSCALE)

dst = img[:,:]

cv.imshow('original', img)
cv.imshow('reconstructed', dst)
cv.waitKey(0)
