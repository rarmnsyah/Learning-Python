import os
import numpy as np
import matplotlib.image as img
import cv2
import time
import matplotlib.pyplot as plt
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(path, 'Resources')
images = []

# format cv2 adalah BGR bukan RGB
for filename in os.listdir(path):
    print(filename)
    images.append(cv2.imread(os.path.join(path, filename)))

for i, image in enumerate(images):
    cv2.imshow('image{}'.format(i), image)


# mengambil tiap pixel gambar
def get_pixel(image):
    imshape = image.shape
    print(imshape[0], imshape[1])
    for i in range(imshape[0]):
        for j in range(imshape[1]):
            print('pixel ({}, {}) : {}'.format(i, j, image[i, j]))
            time.sleep(0.5)

# thresholding
def img_blackwhite_converter(image, threshold=128):
    if (len(image.shape) == 3):
        image = img_grayscale_converter(image)

    width, heigth = image.shape[:2]
    newImage = np.zeros((width, heigth), np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            bw_bit = 255 if image[w, h] >= threshold else 0
            newImage[w, h] = bw_bit

    return newImage

# grayscale
def img_grayscale_converter(image):
    width, heigth = image.shape[:2]
    newImage = np.zeros((width, heigth), np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            grayscale_bit = np.clip(
                # image[w, h][0]*0.07 + image[w, h][1]*0.72 + image[w, h][2]*0.21, 0, 255)
                image[w, h][0] * 0.144 + image[w, h][1] * 0.587 +
                image[w, h][2] * 0.299,
                0,
                255)
            newImage[w, h] = grayscale_bit

    return newImage

# image brightening
def img_brighter(image, brighter):
    width, heigth = image.shape[:2]
    newImage = np.zeros([width, heigth, 3], dtype = np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            images_bit = np.array(image[w, h])
            brighter_bit = np.clip(images_bit + brighter, 0, 255)
            newImage[w, h] = brighter_bit

    return newImage

# negative grayscale image converter
def img_negative_converter(image):
    if (len(image.shape) == 3):
        image = img_grayscale_converter(image)

    width, heigth = image.shape[:2]
    newImage = np.zeros((width, heigth), np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            negative_bit = 255 - image[w, h]
            newImage[w, h] = negative_bit

    return newImage

# histogram pixel image counter automated
def img_histogram_gray_plt(image):
    if (len(image.shape) == 3):
        image = img_grayscale_converter(image)

    hist_value = {}
    # hist_value.key = image[0]

    plt.hist(np.array(image).flatten(), bins=255)
    # print(np.array(image).flatten())
    plt.show()

# histogram pixel image counter manually
def img_histogram_gray_manual(image):
    if (len(image.shape) == 3):
        image = img_grayscale_converter(image)

    hist_value = {i: 0 for i in range(256)}
    # for i in range(image.shape[0]):
    #     for j in range(image.shape[1]):
    image = np.array(image).flatten()
    for i in range(len(image)):
        hist_value[image[i]] += 1

    # hist_value = pd.DataFrame(image).groupby()

    # print(hist_value.keys(), hist_value.values())
    plt.bar(hist_value.keys(), hist_value.values())
    plt.show()

    return hist_value

# frequency histogram image counter
def img_freq_hist(image):
    hist_value = img_histogram_gray_manual(image)
    freq_hist = {i: 0 for i in range(256)}

    freq_hist[0] = hist_value[0]

    for i in range(1, 256):
        freq_hist[i] = freq_hist[i - 1] + hist_value[i]

    print(freq_hist)
    plt.bar(freq_hist.keys(), freq_hist.values())
    plt.show()

def image_aritmatika_operations(img1, img2, operator):
    if (img1.shape != img2.shape) :raise TypeError;
    # operator = (+, -, *)
    # print(img1.shape)
    width, heigth = img1.shape[:2]
    # newImage = np.zeros([width, heigth, 3], dtype = np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            img1[w,h] = eval('np.array(img1[w, h]) {} np.array(img2[w,h])'.format(operator))
    
    return img1

def boolean_operator_and(img1, img2):
    img1 = img_blackwhite_converter(img1, 60)
    img2 = img_blackwhite_converter(img2, 60)
    
    width, heigth = img1.shape[:2]
    newimg = np.zeros((width, heigth), np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            bit = img1[w,h] & img2[w,h]
            newimg[w, h] = bit

    return newimg

def boolean_operator_or(img1, img2):
    img1 = img_blackwhite_converter(img1, 60)
    img2 = img_blackwhite_converter(img2, 60)
    
    width, heigth = img1.shape[:2]
    newimg = np.zeros((width, heigth), np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            bit = img1[w,h] | img2[w,h]
            newimg[w, h] = bit

    return newimg

def boolean_operator_not(img):
    img = img_blackwhite_converter(img, 60)
    
    width, heigth = img.shape[:2]
    newimg = np.zeros((width, heigth), np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            bit = ~img[w,h]
            newimg[w, h] = bit

    return newimg

def image_dilated(img, x, y):
    width, heigth = img.shape[:2]
    y = -y
    newimg = np.zeros((width, heigth, 3), np.uint8)
    for w in range(width - 1):
        for h in range(heigth - 1):
            try:
                if (w+x<0 or h+y<0):newimg[w,h] = [0,0,0]
                else :newimg[w, h] = img[w+x, h+y] 
            except:
                newimg[w, h] = [0,0,0]
    return newimg

def image_rotated(img):
    width, heigth = img.shape[:2]
    newimg = np.zeros((width, heigth, 3), np.uint8)
    for w in range(width - 1):
        k = heigth-1
        for h in range(heigth - 1):
            newimg[k, w] = img[h, w]
            k -= 1
    return newimg

def image_zoomed(img, scale):
    width, heigth = img.shape[:2]
    newimg = np.zeros((width*2, heigth*2, 3), np.uint8)
    m, n = 0, 0
    for w in range(width - 1):
        for h in range(heigth - 1):
            newimg[m, n] = img[w, h]
            newimg[m, n+1] = img[w, h]
            newimg[m+1, n] = img[w, h]
            newimg[m+1, n+1] = img[w, h]
            n += scale
        m += scale
        n = 0
    return newimg

# operations = 


newImage = []
newImageGrayscale = img_grayscale_converter(images[1])
newBrighterImage = img_brighter(images[2], -10)
newNotImage = boolean_operator_not(images[4])
newAndImage = boolean_operator_and(images[8], images[1])
newAritmeticImage = image_aritmatika_operations(images[3], images[4], '+')
newDilatedImage = image_dilated(images[2], 25, 35)
newRotatedImage = image_rotated(images[9])
newZoomedImage = image_zoomed(images[7], 2)

# cv2.imshow('gambar', images[1])
cv2.imshow('grayscale', newImageGrayscale)
cv2.imshow('brigther', newBrighterImage)
cv2.imshow('not', newNotImage)
cv2.imshow('and', newAndImage)
cv2.imshow('aritmetic', newAritmeticImage)
cv2.imshow('dilated', newDilatedImage)
cv2.imshow('rotated', newRotatedImage)
cv2.imshow('zoomed', newZoomedImage)

# newImageNegative = img_negative_converter(newImageGrayscale)
# newImageBlackwhite = img_blackwhite_converter(newImageGrayscale)
# img_histogram_gray_manual(m)
# img_histogram_gray_plt(m)
# img_freq_hist(m)
# get_pixel(m)

cv2.waitKey(0)
# # img.imsave(os.path.join(outputPath, 'newImage.png'), newImage)
