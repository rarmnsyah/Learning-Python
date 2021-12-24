# builtin adalah sebuah fungsi yang biasa digunakan di python tanpa import spesifik library
# Berikut semua contoh builtin fungsi pada python

# 1. Absolut (abs(x))
# Fungsi yang mengembalikan nilai mutlak dari variable yang dikehendaki
print(abs(-2), abs(3.2)) # 2 3.2

# 2. all(iterable) --> iterable = variable yang dapat diulang
# Fungsi yang mereturn nilai true, jika seluruh element pada iterable bernilai true / iterable = empty
emptyList = []
otherList = [1,3,0]
print(all(emptyList)) #True
print(all(otherList)) #False

# 3. any(iterable)
# Funsi yang mereturn nilal true, jika terdapat element pada iterable yang bernilai true dan return false jika iterable = empty
print(any(emptyList)) #False
print(any(otherList)) #True

# 4. ascii(object)
# Fungsi yang akan mencetak output sesuai objek, tanpa memedulikan karakter non-ascii seperti \t, \n, dsb 
testString = 'a\t\tsdaf'
print(ascii(testString)) #a\t\tsdaf
print(testString) #a        sdaf

# 5. binary-converter (bin(x))
# Fungsi untuk mengkonversi integer number menjadi binary string dengan awalan '0b'
print(bin(14)) #0b10 --> untuk menghilangkan 0b bisa menggunakan berbagai cara ya

# 6. list() / objek = []
# Fungsi builtin yang berguna untuk menginisialisasi new list, nutuk pemahaman spesifik mengenai list, dapat searching ya
newList = list()
newList2 = []

# 7. set()
# Fungsi untuk menginisialisasi new set, arti spesifik dapat searching juga ya
newSet = set()

# 8. dict() / objek = {}
# Fungsi untuk menginisialisasi new dict
newDict = dict()
newDict2 = {}

# 9. length (len(s))
# Fungsi yang mengembalikan nilai panjang sebuah objek dapat berupa string, list, dsb.
testLengthList = [2,3,41,12]
testLengthSet = {2,3,41,2}
print(len(testLengthList)) #4
print(len(testLengthSet)) #3

# 10. eval(expression)
# Fungsi yang mengembalikan nilai berdasarkan operasi yang ditulis dengan string
print(eval('4 / 12 + 1')) #1.333

# testing