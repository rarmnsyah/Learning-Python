class ojek():
    def __init__ (self, nama, transmisi, daerah_kerja):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah_kerja = daerah_kerja

    def cek_id (self):
        print ('nama:', self.nama)
        print ('transmisi:', self.transmisi)
        print ('daerah kerja:', self.daerah_kerja)

# ini adalah inheritance (warisan)
# jadi, gojek adalah warisan dari ojek, karena gojek juga merupakan ojek
# sehingga, kita bisa menulis fungsi di gojek tanpa harus mengulang 
class Gojek(ojek):
    pass

mario = ojek ('mario' , 'manual' , 'bandung selatan')
# contoh penggunaan 'Gojek' melalui inheritance ojek
jason = Gojek ('jason' , 'automatic' , 'babel')

mario.cek_id()
jason.cek_id()
print(mario.nama)
    