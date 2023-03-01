import os
import numpy as np
import matplotlib.image as img
import cv2
import time
import matplotlib.pyplot as plt
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
img_url = 'instagram_icon-removebg-preview.png'
imgPath = os.path.join(path, 'resources', img_url)
outputPath = os.path.join(path, 'output')

# format cv2 adalah BGR bukan RGB
m = cv2.imread(imgPath)


def get_pixel(image):
    imshape = image.shape
    print(imshape[0], imshape[1])
    for i in range(imshape[0]):
        for j in range(imshape[1]):
            print('pixel ({}, {}) : {}'.format(i, j, image[i, j]))
            time.sleep(0.5)


def img_brighter(image, brighter):
    width, heigth = image.shape[:2]
    newImage = np.zeros([width, heigth, 3])
    for w in range(width - 1):
        for h in range(heigth - 1):
            images_bit = np.array(image[w, h])
            # luma = 0.07*images_bit[0] + 0.72*images_bit[1] + 0.21*images_bit[2]
            # luma += brighter
            brighter_bit = np.clip(images_bit + brighter, 0, 255)
            newImage[w, h] = brighter_bit
    # print(newImage)

    return newImage


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


def img_histogram_gray_plt(image):
    if (len(image.shape) == 3):
        image = img_grayscale_converter(image)

    hist_value = {}
    # hist_value.key = image[0]

    plt.hist(np.array(image).flatten(), bins=255)
    # print(np.array(image).flatten())
    plt.show()


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


def img_freq_hist(image):
    hist_value = img_histogram_gray_manual(image)
    freq_hist = {i: 0 for i in range(256)}

    freq_hist[0] = hist_value[0]

    for i in range(1, 256):
        freq_hist[i] = freq_hist[i - 1] + hist_value[i]

    print(freq_hist)
    plt.bar(freq_hist.keys(), freq_hist.values())
    plt.show()

cv2.imshow('gambar', m)
# img_histogram_gray_manual(m)
# newImageGrayscale = img_grayscale_converter(m)
# newBrighterImage = img_brighter(m, -50)
# newImageNegative = img_negative_converter(newImageGrayscale)
# newImageBlackwhite = img_blackwhite_converter(newImageGrayscale)
# img_histogram_gray_plt(m)
img_freq_hist(m)
# get_pixel(m)

# cv2.imshow('oldimage', m)
# cv2.imshow('imgBrighter', newBrighterImage)
# cv2.imshow('imgGrayscale', newImageGrayscale)
# cv2.imshow('imgNegativeGrayscale', newImageNegative)
# cv2.imshow('imgBlackWhite', newImageBlackwhite)
# cv2.waitKey(0)
# cv2.imshow('newimage', newImage)
# # img.imsave(os.path.join(outputPath, 'newImage.png'), newImage)
