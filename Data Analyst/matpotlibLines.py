import matplotlib.pyplot as plt
import random as rand
import numpy as np

# matpotlib adalah salah satu library di python yang biasa digunakan oleh data scientist sebagai sarana untuk memvisualisasikan objek data.

def matplotlibLines():
    # Fungsi ini merupakan fungsi untuk memvisualisasikan data menjadi sebuah grafik lines
    year = [1950, 1970, 1990, 2012]
    pop = [2.519, 3.692, 5.263, 6.972]
    outerPop = [3.213, 1.231, .3213, .012]

    # plt.plot memvisualkan grafik garis antara year (x) dan population(y) dengan garis yang tersambung
    plt.plot(pop)

    # sementara itu, plt.scatter akan memvisualisasi grafik seperti plot, hanya saja dengan garis terputus (hanya titik-titik)
    # plt.scatter(year, outerPop)
    plt.show()

def matplotlibHistogram():
    # Fungsi ini digunakan untuk memvisualisasikan data menjadi sebuah histogram
    values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
    plt.hist(values, bins = 3) #bins merupakan banyaknya batang yang akan divisualisasikan
    plt.show()

# randList = [rand.randint(40,49) for i in range(5)] + [rand.randint(50,59) for i in range(3)] + [rand.randint(60,69) for i in range(10)]
# plt.hist(randList,cumulative = True)
# plt.show()
matplotlibLines()
