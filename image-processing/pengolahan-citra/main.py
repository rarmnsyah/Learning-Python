import os 
import numpy as np
import matplotlib.image as img
import cv2

path = os.path.dirname(os.path.realpath(__file__)) 
img_url = 'instagram_icon-removebg-preview.png'
imgPath = os.path.join(path, 'resources', img_url)
outputPath = os.path.join(path, 'output')

# format cv2 adalah BGR bukan RGB
m = cv2.imread(imgPath)

def img_brighter(image, brighter):
    width, heigth = image.shape[:2]
    newImage = np.zeros([width, heigth, 3]);
    for w in range(width-1):
        for h in range(heigth-1):
            images_bit = image[w,h]
            luma = 0.07*images_bit[0] + 0.72*images_bit[1] + 0.21*images_bit[2]
            luma += brighter
            brighter_bit = [0.07*luma, 0.72*luma, 0.21*luma]
            newImage[w,h] = brighter_bit

    return newImage

def img_grayscale_converter(image):
    width, heigth = image.shape[:2]
    newImage = np.zeros((width, heigth), np.uint8);
    for w in range(width-1):
        for h in range(heigth-1):
            grayscale_bit = np.clip(image[w, h][0]*0.07 + image[w,h][1]*0.72 + image[w,h][2]*0.21, 0, 255)
            newImage[w,h] = grayscale_bit
    return newImage

def img_negative_converter (image):
    if (len(image.shape) == 3):
        image = img_grayscale_converter(image)

    width, heigth = image.shape[:2]
    newImage = np.zeros((width, heigth), np.uint8);
    for w in range(width-1):
        for h in range(heigth-1):
            negative_bit = 255-image[w,h]
            newImage[w,h] = negative_bit
    return newImage

def img_blacwhite_converter (image, threshold = 128):
    if (len(image.shape) == 3):
        image = img_grayscale_converter(image)

    width, heigth = image.shape[:2]
    newImage = np.zeros((width, heigth), np.uint8);
    for w in range(width-1):
        for h in range(heigth-1):
            bw_bit = 255 if image[w,h] >= threshold else 0
            newImage[w,h] = bw_bit
    return newImage
            

newBrighterImage = img_brighter(m, 0)
newImageGrayscale = img_grayscale_converter(m)
newImageNegative = img_negative_converter(newImageGrayscale)
newImageBlackwhite = img_blacwhite_converter(newImageGrayscale)

# newImage = bright_updater(0.5, m)
# print(newImage.shape, m.shape)

cv2.imshow('oldimage', m)
cv2.imshow('imgBrighter', newBrighterImage)
cv2.imshow('imgGrayscale' , newImageGrayscale)
cv2.imshow('imgNegativeGrayscale', newImageNegative)
cv2.imshow('imgBlackWhite', newImageBlackwhite)
# cv2.imshow('newimage', newImage)
cv2.waitKey(0)
# # img.imsave(os.path.join(outputPath, 'newImage.png'), newImage)
