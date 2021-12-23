import random
import dataHangman

def permainan(kataTebakan):
    jawaban = ['_' for _ in range(len(kataTebakan))]
    health = len(kataTebakan)
    repeater = True
    while(health and repeater):
        output(jawaban)
        masukan = input("Tebak 1 huruf!: ") 
        print()
        count = kataTebakan.count(masukan)

        if(len(masukan) > 1):
            print("1 Angka woi!!")
            health -= 1
            print("Nyawa anda tersisa:", health)
        else:
            if masukan in kataTebakan:
                if masukan in jawaban:
                    print('Huruf sudah digunakan!')
                else:
                    find = 0
                    for i in range(count):
                        index = kataTebakan.find(masukan, find, len(kataTebakan))
                        jawaban[index] = masukan.upper()
                        find = index + 1
            else:
                health -= 1
                print("Huruf {} Tidak ada Pada Kata!\nNyawa anda tersisa:{}".format(masukan,health))
        repeater = '_' in jawaban
    output(jawaban)

    if(health == 0):
        print("\nYahh! Anda kalah! Tetap Semangat! :D")
        print("Jawabannya adalah: {}".format(kataTebakan.upper()))
        

def output(jawaban):
    for i in jawaban:
        print(i, end = ' ')
    print()

print("-"*4 +"Selamat Datang di Permainan Tebak Nama" + "-"*4)

kata = dataHangman.data


print('\n' + "-"*15 + "Silahkan Tebak!" + "-"*15)

kataTebakan = random.choice(kata)
permainan(kataTebakan)

print("-"*10 + 'Terima Kasih Sudah Bermain' + '-'*10)