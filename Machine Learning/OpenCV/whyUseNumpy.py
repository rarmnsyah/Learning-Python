import numpy as np
import random

randList1 = [random.randint(0,10) for _ in range(10)]
randList2 = [random.randint(0,10) for _ in range(10)]
# Mengapa kita menggunakan library numpy pada saat mengelola sejumlah besar data?
# Hal ini dikarenakan numpy memiliki method array (like list) yang dapat memudahkan proses pengolahan data, yang tidak dapat dilakukan oleh normal list

# Perlu diingat! Numpy array hanya dapat menyimpan satu jenis tipe data, dan jika kita mencoba untuk input >1 tipe data, maka seluruh tipe data akan dikonversi menjadi tipe data yang sama (type coercion)
# Selain itu, numpy array tidak sama dengan list yang ada di default python, kita bisa menganggapnya sebagai tipe data yang baru


# Contoh:
np_array_1 = np.array(randList1)
np_array_2 = np.array(randList2)
# Privilege 1: Kita dapat mengoperasikan data pada list secara langsung (1 by 1 (sort by range)) seperti berikut:
# ctt : range antar list harus sama
list1MultByList2 = np_array_1 * np_array_2
# print(list1MultByList2)
'''
That actually the same thing with this
list1MultByList2 = []
for i in range(len(np_array_1)):
    list1MultByList2.append(np_array_1[i] * np_array_2[i])
'''

# Privilege 2: Dengan numpy array kita dapat memperoleh sublist sesuai dengan yang kita perlukan (selected berdasakan kondisi boolean)
# Contoh:
newList = list1MultByList2[list1MultByList2 > 7] #newList hanya akan menyimpan value berdasarkan kondisi yang terpenuhi saja (seperti contoh : x > 7)
# print(newList)


# ============================================================================
# 2D NUMPY
np_2d = np.array([randList1, randList2])
# Privilege 3:
# Ketika menggunakan numpy 2d array, kita dapat memanggil data dengan cara:
# np_2d[0][1] == np_2d[0,1] --> Kedua hal ini memiliki fungsi yang sama, dan keduanya work
# Selain itu, menggunakan tekhnik pemanggilan numpy array, kita dapat langsung membuat sublist secara instan, contoh:
# print(np_2d[:,5:9]) #Hal ini tidak dapat dilakukan menggunakan cara default secara instan

# Privilege 4:
# Dengan menggunakan tekhnik pemanggilan numpy, kita dapat mengoperasikan data tersebut secara lebih lanjut, contoh:
# Ketika kita hendak mencari rata-rata dari data yang kita punya, kita dapat menggunakna statement berikut:
mean = np.mean(np_2d[:,0]) #statement ini akan mereturn nilai rata-rata dari np_2d colom 1 ke variable mean
# kita juga dapat mengakses berbagai basic statistic operation seperti di file sebelah

corr= np.corrcoef