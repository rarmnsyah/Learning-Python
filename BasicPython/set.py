"""
set adalah kumpulan data (array) selayaknya list, namun yang membedakannya dengan list adalah:
1. set tidak dapat menampung data yang sama (kloning value)
2. himpunan data didalam set, tidak diurut, dan setiap dipanggil urutan didalam set akan dipanggil secara acak
3. set juga tidak dapat dirubah
4. set ditandai dengan "variable = {}" atau variable = set(())
5. set juga dapat menampung type value yang berbeda beda
"""

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset.update(["apple", "mantaj", 'cherry', 12])
print(thisset)

# kita dapat menggunakan set untuk mengurangi 2 himpunan
testset = [1,23,4,1,5, 'mantap']
testset2 = [1,4,1,3,6]

anjay = 'amatna'
print(anjay[1:3])

set()

# merubah bentuk list menjadi set
print(set(testset2)-set(testset))
