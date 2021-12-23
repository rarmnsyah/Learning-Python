import DataSoal as ds

soal = []

def sorting(type):
    queue = {}
    for i in ds.primaryKey:
        queue[i] = ds.primaryKey[i]
    nilaiSoal = {}
    for i in ds.primaryKey:
        nilaiSoal[ds.bobotSoal[i]] = i
    ds.primaryKey.clear()
    if type == 1:
        for i in sorted(nilaiSoal):
            ds.primaryKey[nilaiSoal[i]] = queue[nilaiSoal[i]]
    else:
        for i in sorted(nilaiSoal)[::-1]:
            ds.primaryKey[nilaiSoal[i]] = queue[nilaiSoal[i]]

def showSoal():
    print()
    print('No\tSoal (difficulty)')
    for i in range(len(soal)):
        print('{}\t{} ({})'.format(i+1,soal[i], ds.difficulty(ds.bobotSoal[soal[i]])))

def updateSoal():
    soal.clear()
    for j in ds.primaryKey:
        soal.append(j)
    showSoal()

def homeScreen():
    print('===============TEST_SOAL_FISIKA===============')
    updateSoal()
    
def KKM(nilai):
    print("Nilai Anda Adalah: {}".format(nilai))
    if 70 <= nilai <= 100:
        return 'Selamat Anda Lulus TEST FISIKA'
    else: return 'Maaf, Ands Harus Mengulang Tahun Depan :D'

homeScreen()
nilai = 0

urutSoal = input("Sorting Soal?(y/n): ")
if urutSoal.casefold() == 'y':
    tipeSort = input('(up): Easy-->Hard, (down): Hard-->Easy = ')
    if tipeSort.casefold() == 'up':
        sorting(1)
    elif tipeSort.casefold() == 'down':
        sorting(0)
    updateSoal()
    
while(ds.primaryKey):
    pilihSoal = int(input('Pilih Soal: '))
    if(pilihSoal in range(1, len(ds.primaryKey)+1)):
        primkey = soal[pilihSoal-1]
        print('\n{}. {}'.format(pilihSoal,ds.soal[primkey]))
        print(f'\nBobot Soal: {ds.bobotSoal[primkey]}')
        opsi = input("Pilih Jawaban Anda: ")
        if opsi.upper() == ds.jawaban[primkey]:
            nilai += ds.bobotSoal[primkey]
        del ds.primaryKey[primkey]
        updateSoal()
    else:
        print('Soal Tidak Ada')

nilai = nilai*100 / (sum(ds.bobotSoal.values()))
print(KKM(nilai))

