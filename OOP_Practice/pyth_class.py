# ==============================Class=================================
class mahasiswa(): #template

    # package init (otomatis dijalankan ketika class dipang
    # init (otomatis dijalankan ketika class dipanggil)
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

    # package in class
    # self mengartikan kepemilikan class
    def aktivitas(self, aktivitas_sekarang):
        print(self.nama,"(",self.nim, ")", 'sedang', aktivitas_sekarang)


# ==========================Main_Program==============================

mahasiswa1= mahasiswa("Otong Surajat", 123) #object / instance
# penjelasan:
# mahasiswa1 disini dideklarasi dengan input_name = "Otong Surajat"
# sehingga akan memasuki def init dan merubah self.nama menjadi "Otong Surajat"
# hasilnya mhasiswa1.nama menjadi "Otong Surajat"
mahasiswa1.aktivitas("tidur")

# otong dan ucup disini dijadikan sebagai 'self'

