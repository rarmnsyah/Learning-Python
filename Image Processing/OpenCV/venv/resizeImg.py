# File ini dibuat sebagai catatan untuk meresize dan crop images
import cv2
import numpy as np 


path = "C:/Users/LENOVO/Template Program/Python/Materi/Machine Learning/OpenCV/Resources/instagram_icon-removebg-preview.png"
img = cv2.imread(path)
cv2.imshow('img', img)


cv2.waitKey()