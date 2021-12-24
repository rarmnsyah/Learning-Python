# File ini digunakan untuk mendeskripsi string di python
# Deklarasi string : (dapat menggunakan '' atau "")
stringExample1 = 'ini string'
stringExample2 = "ini string 2"

# Operasi pada string
concatString = stringExample1 + stringExample2 #menggabungkan string (+) atau menggunakan fungsi concate --> program akan eror jika string + !string
duplicateString = stringExample1 * 2 #duplicate string dapat menggunakan operator math (*) 
# substring --> [x:] = substring baru dengan index x - lastIndex
substring = stringExample1[1:]
# substring --> [:x] = substring baru dengan index firstIndex - x
substring2 = stringExample2[:2]

# fungsi pada string (dapat disearching ya jnck) / dapat diketahui dengan bantuan visual code (example : str.fungsi())
print(stringExample1.upper()) #contoh fungsi pada string