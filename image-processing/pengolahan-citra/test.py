import os
import cv2

path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(path, 'resources')
images = []

# format cv2 adalah BGR bukan RGB
for filename in os.listdir(path):
    images.append(cv2.imread(os.path.join(path, filename)))
    
for i, image in enumerate(images):
    cv2.imshow('image{}'.format(i), image)

cv2.waitKey()
# print(images)
