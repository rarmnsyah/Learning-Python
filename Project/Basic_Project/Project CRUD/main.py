import os
if not os.path.exists('C:/Users/LENOVO/Template Program/Python/Project/Basic_Project/Project CRUD/database.txt'):
    file1 = open('C:/Users/LENOVO/Template Program/Python/Project/Basic_Project/Project CRUD/database.txt', 'w')
    file1.write('Admin,Risky Armansyah,Sungailiat,31 Oktober 2003')
    file1.close()
from database import *
# create
def create():
    username = input('Username: ')
    while username in data:
        print('Username Sudah Terdaftar! Silahkan Ganti')
        username = input('Username: ')
    nama = input('Nama Lengkap\t\t: ')
    ttl = input('Tempat / Tanggal Lahir\t: ')
    while '/' not in ttl:
        print('Silahkan Masukkan TTL Sesuai Format (TEMPAT/TANGGAL)')
        ttl = input('Tempat / Tanggal Lahir\t: ')
    tempat,tanggal = ttl.split('/')
    tanggal = tanggal.strip()
    tempat = tempat.strip()

    file1= open('C:/Users/LENOVO/Template Program/Python/Project/Basic_Project/Project CRUD/database.txt', 'a')
    file1.write('\n{},{},{},{}'.format(username, nama, tempat, tanggal))
    file1.close()
    opsi()

# read
def read():
    print('No.\tName\t\t\tTempat Lahir\t\tTanggal Lahir')
    no = 1
    for i in data:
        print(f'{no}.\t{data[i][0]}\t\t{data[i][1]}\t\t{data[i][2]}')
        no += 1
    opsi()

# update
def update():
    listData = []
    for i in data:
        listData.append(i)
    pilih = int(input('Pilih Data yang Hendak di-UPDATE: '))
    nama = input('Nama Lengkap\t\t: ')
    ttl = input('Tempat / Tanggal Lahir\t: ')
    while '/' not in ttl:
        print('Silahkan Masukkan TTL Sesuai Format (TEMPAT/TANGGAL)')
        ttl = input('Tempat / Tanggal Lahir\t: ')
    tempat,tanggal = ttl.split('/')
    tanggal = tanggal.strip()
    tempat = tempat.strip()
    data[listData[pilih-1]] = [nama,tempat, tanggal]
    update2()
    opsi()

# delete
def delete():
    listData = []
    for i in data:
        listData.append(i)
    pilih = int(input('Pilih Data yang Hendak di-DELETE: '))
    del(data[listData[pilih-1]])
    opsi()

def close():
    exit()

def opsi():
    opsi = int(input("\nSILAHKAN PILIH OPSI: "))
    opsiDef = [create, read, update, delete, close]
    opsiDef[opsi-1]()
    
# ui
print('=========SELAMAT-DATANG-DI-APLIKASI-PENDAFTARAN-DATA=========')
print('PILIH OPSI BERIKUT: \n1.\tCREATE\n2.\tREAD\n3.\tUPDATE\n4.\tDELETE\n5.\tEXIT')
opsi()