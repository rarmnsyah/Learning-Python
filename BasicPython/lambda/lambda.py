# ----------LAMBDA-----------
# lambda pada dasarnya adalah sebuah fungsi dengan cara penulisan yang lebih sederhana
# dengan contoh struktur:
# variable = lambda | variable | : bentuk eksekusi
# contoh deklarasi lambda pada umumnya(basic)
# lambda dengan 1 argumen
lambdaExample = lambda a: a ** 2

# lambda dengan 2 argumen
lambdaExample2 = lambda a,b : a+b

print(lambdaExample(2), lambdaExample2(2,3))

# 2 contoh lambda diatas memilki bentuk yang sama dengan
def fungsiAsLambda(a):
    return a**2

def fungsiAsLambda2(a,b):
    return a + b

# Lambda juga dapat menggunakan input infinity seperti fungsi
# infinity 1
lambdaExample3 = lambda *a: print(a)

# infinity 2
lambdaExample4 = lambda **a: print(a.values())

lambdaExample3(1,2,3,4,5)
lambdaExample4(a=1,b=2,c=3)

# contoh penerapan lambda versi hard
# contoh lambda ini akan memastikan syarat(filter) terpenuhi,
# baru eksekusi dapat dijalankan
li = [i for i in range(10)]
beyond_five = list(filter(lambda x: (x>5), li))
print(beyond_five)

