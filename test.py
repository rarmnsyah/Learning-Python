import sys

class mantapJiwa:
    __bar = 2

    def __init__(self):
        self.jiwa = 12
        print(self.__bar)

a = mantapJiwa()

print(a.jiwa)

def faktorial(a):
    output = a
    for i in range(a-1, 0, -1):
        output*=i
    return 1 if a == 0 else output

def combination(a,b):
    print(int(faktorial(b)/(faktorial(a)*faktorial(b-a))))
    return int(faktorial(b)/(faktorial(a)*faktorial(b-a)))

def tentukanTeamLomba(a,b,c):
    mat = combination(1,a) * combination(2,b) * combination(2,c)
    kimia = combination(2,a) * combination(3,b) * combination(1,c)
    
    return 'Matematika: {} team\nKimia: {} team'.format(mat, kimia)

def checkRookMove(n, path):
    for i in range(len(path) - 1):
        if not(abs(path[i] - path[i+1]) == 1 or abs(path[i] - path[i+1]) == n):
            return "ILLEGAL"
    return 'LEGAL'

def lordUsop(A, B):
    newB = []
    for b in B:
        newB.append('0' + str(b) if b<10 else str(b))

    # Write your code here
    temp = []
    for i in range(0, len(A), 2):
        obj = A[i] + A[i+1]
        temp.append(obj)

    newB2 = newB.copy()
    idx = []
    for i in range(len(temp)):
        if temp[i] in newB:
            newB2.remove(temp[i])
        else:
            idx.append(i)

    index = 0
    for i,j in zip(idx, newB2):
        temp[i] = newB2[index]
        index+=1

    return ''.join(temp)

def AyoBerhitung(A):
    output = 0
    stk = []
    for i in A:
        if i > 0:
            output += i
            stk = []
        else:
            stk.append(i)
            if len(stk) == 5:
                output += max(stk)
    
    return output

def cekGender(username):
    # Write your code here
    username = ' ' + username + ' '
    jumlah = 0
    stk = list()
    for i in range(1,len(username)-1):
        if username[i] == username[i-1] or username[i] == username[i+1]:
            continue
        else:
            jumlah += 1
    return 'IGNORE HIM!' if jumlah % 2 == 1 else 'CHAT WITH HER!'

# # print(cekGender('abaaaabbas'))
# print(len(sys.argv))
# print(sys.argv)
# print(sys.argv[1])

coba = 'nama saya risky armansyah risky'

print(coba.replace('risky', 'rehan', 3))

print('angka'.zfill(10))

print('jum\'at')

print(11 >> 1)

from operator import *
hijau = 5
kuning = 10
print('Kelereng Hijau = {}'.format(hijau))
print('Kelereng Kuning = {}'.format(kuning))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(hijau, kuning): {}'.format(func.__name__, func(hijau, kuning)))

print(12 | 1)

import os
print(os.getcwd())

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')

a = lambda x,y : x * y
print(a(2,3))

a = {1,2}
print(a[0])