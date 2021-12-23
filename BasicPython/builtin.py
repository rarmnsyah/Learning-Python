# builtin adalah sebuah fungsi yang biasa digunakan di python tanpa import spesifik library
# Berikut semua contoh builtin fungsi pada python

contohList = [1,23,2,4,4,5,5]

# 1. Absolut (abs(x))
# Fungsi yang mengembalikan nilai mutlak dari variable yang dikehendaki
print(abs(-2), abs(3.2)) # 2 3.2

# 2. all(iterable) --> iterable = variable yang dapat diulang
# Fungsi yang mereturn nilai true, jika seluruh element iterable bernilai true / iterable = empty
emptyList = []
returnFalseList = [1,3,0]
print(all(emptyList)) #True
print(all(returnFalseList)) #False


# 1. length
# Fungsi yang berguna untuk mereturn panjang sebuah string, list, set, dsb.
print(len(contohList))

# 2. 