# File ini dibuat sebagai catatan untuk meresize dan crop images
import cv2
import numpy as np
import basicFuntion as bf

img = bf.getImg()
cv2.imshow('img', img)

cv2.waitKey()