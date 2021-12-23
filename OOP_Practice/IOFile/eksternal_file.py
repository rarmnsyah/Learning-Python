# ============================File_Eksternal============================
import os

# syntax pada eksternal file
# w = write mode (membuat dan menghapus data lama)
# r = read mode (membaca data only)
# a = appending mode (menambah data pada baris terakhir atau membuat file baru jika file tidak ada)
# x = create mode (membuat spesifik file, return error jika file telah ada)
# r+ = write and read mode

# =============================Write_Mode=================================
file1 = open("data.txt","w")
file1.write("membuat ulang data pada file data.txt")
file1.close() 

# =============================Read_Mode=================================
file2 = open("data.txt", "r")
print(file2.read())
file2.close()

# ===========================Appending_Mode===============================
file3 = open("data.txt", 'a')
file3.write("\nupdate / ditambah dengan mode appen")
file3.close()

# os.remove("data.txt")
