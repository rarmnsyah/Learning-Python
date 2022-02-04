'''
file ini dibuat untuk membahas 5 basic function untuk pemula ketika menggunakan
libray opencv / cv2
'''
import cv2
import numpy as np
from numpy.lib.function_base import iterable

path = "C:/Users/LENOVO/Template Program/Python/Materi/Machine Learning/OpenCV/Resources/instagram_icon-removebg-preview.png"
img = cv2.imread(path)
cv2.imshow('basicIMG', img)

'''
1. fungsi grayscale untuk convert img to other color_scale (mengatur skala warna pada gambar)
    cv2.cvtColor(object, cv2.'skala_warna')
'''
rescaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('rescaleIMG' ,rescaleImg)


'''
2. fungsi blur kedua adalah fungsi untuk menambah blur pada img
    cv2.GaussianBlur(object, ('size_of_kernel '), 'blur_value)
    size_of_kernel berfungsi juga untuk menentukan blur_value-nya
'''
blurImg = cv2.GaussianBlur(img, (7,7) , 2)
cv2.imshow('blurIMG' , blurImg)

'''
3. fungsi canny untuk mengubah img menjadi objek canny(berupa garis hitam putih)
    cv2.Canny(object, paramater)
    --> semakin kecil paramater (x,y), maka detail object semakin tinggi
    --> ideal paramater untuk digunakan (x = 100, y = 200)
'''
cannyImg = cv2.Canny(rescaleImg, 100,200    )
cannyImg2 = cv2.Canny(rescaleImg, 1,1)
cv2.imshow('canIMG100200', cannyImg)
cv2.imshow('canIMG11', cannyImg2)

'''
4. Fungsi dilate untuk increase tight of line dari canny img
    cv2.dilate(object, kernel, iterations)
    kernel merupakan matriks yang dapat diambil dari library numpy menggunakan fungsi
    np.ones(n,n), np.uint8)
    iterations berarti berapa kali fungsi tersebut akan diulangi, semakin tinggi berarti semakin
    banyak fungsi tsb digunakan
'''
kernel = np.ones((5,5), np.uint8)
print(kernel)
dilationImg = cv2.dilate(img,kernel , iterations = 1)
dilationImgCanny = cv2.dilate(cannyImg, kernel, iterations= 1)
cv2.imshow('dilatesIMG', dilationImg)
cv2.imshow('dilIMGCan' , dilationImgCanny)

'''
5. fungsi eroded berfunsi sebagai kebalikan dari fungsi dilate
    yaitu untuk menurunkan tight of line dari sebuah objek gambar
    cv2.erode(object, kernel, iterations)
'''
erodedImg = cv2.erode(dilationImgCanny, kernel, iterations = 1)
cv2.imshow('erodedIMG', erodedImg)

cv2.waitKey(0)