field = [['_' for _ in range(3)] for _ in range(3)]

player = {
    1 : 'O',
    2 : 'X'
}

# testing
def printField():
    for i in field:
        print('|', end='')
        for j in i:
            print(' {} |'.format(j), end='')
        print()

def winner():
    for i in field:
        cek = i[0]
        if i.count(cek) == 3 and cek != '_':
            return '{} WINNER'.format(cek)

    for i in range(3):
        cek = field[0][i]
        if field[1][i] == cek and field[2][i] == cek and cek != '_':
            return '{} WINNER'.format(cek)

    if field[0][0] == field[1][1] == field[2][2] !='_':
        return '{} WINNER'.format(field[0][0])
    elif field[0][2] == field[1][1] == field[2][0] !='_':
        return '{} WINNER'.format(field[0][0])

    test = 0
    for i in field:
        if '_' not in i:
            test += 1
    
    if test == 3:
        return 'DRAW'
    

def main():
    off = 9
    playerOption = 1
    while off:
        printField()
        repeater = True
        while repeater:
            userInput = input('\n----Player {} ({})----\nSilahkan Pilih: '.format(playerOption, player[playerOption]))
            try:
                x,y = userInput.split(',')
                repeater = False
            except:
                printField()
                print("Format Yang Anda Masukkan Tidak Sesuai Ketentuan! \nFormat yang benar: x,y")
                repeater = True

        if int(x) not in range(1,4) or int(y) not in range(1,4):
            print('Silahkan Masukkan Inputan Yang Benar (x,y)\nInterval Range(3*3)')
        else:
            if field[int(x)-1][int(y)-1] == '_':
                field[int(x)-1][int(y)-1] = player[playerOption]
                playerOption = 1 if playerOption == 2 else 2
                off -= 1
                if(winner()):
                    printField()
                    print('\n{}'.format(winner()))
                    exit()
            else:
                print('Objek Sudah Terisi!')


main()


