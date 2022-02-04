import matplotlib.pyplot as mlt
import numpy as np
# pada file ini kita akan menggunakan data yang sedikit lebih banyak
# agar lebih terbiasa pada irl

# syntax pada numpy untuk mengakses banyak data (untuk latihan)
# karena irl kita akan menggunakan banyak data sekaligus
starts = 0.0 #batas awal data (float)
finish = 5.0 #batas akhir data (float)
nData = 100000 #banyaknya data yang dibutuhkan
randomData = np.random.uniform(starts, finish, nData)
# print(randomData)

# membuat histogram dari sekumpulan data
nBar = 250
mlt.hist(randomData,nBar)
mlt.show()
