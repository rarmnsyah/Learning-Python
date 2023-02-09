import os 
import numpy as np
import matplotlib.image as img
import cv2

path = os.path.dirname(os.path.realpath(__file__)) 
img_url = 'IMG-20181110-WA0061.jpg'
imgPath = os.path.join(path, 'resources', img_url)
outputPath = os.path.join(path, 'output')

m = cv2.imread(imgPath)

print(m.shape, m.flatten().shape)
print(np.array(m[0,0]) + 12)

width, heigth = m.shape[:2]

newImage = np.zeros([width, heigth, 3]);
brigther = -100

for w in range(width-1):
    for h in range(heigth-1):
        bright = np.array(m[w, h]) + brigther
        # print(bright, m[w,h])
        newImage[w, h] = bright #if bright < 255 else 255

print(newImage.shape, m.shape)


cv2.imshow('oldimage', m)
cv2.imshow('newimage', newImage)
cv2.waitKey(0)
# img.imsave(os.path.join(outputPath, 'newImage.png'), newImage)
