# pada materi ini saya akan memberi contoh machine learning
# dalam mengakses sebuah struktur data
import numpy as np
from scipy import stats
from scipy.special import comb, factorial

# jika kita mempunyai sekumpulan data mengenai umur masyarakat
# pada sebuah desa / lingkungan
ages = [5,3143,3,43,43,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print('data: ' , ages)

# mencari basic fungsi pada statistic (mean, meidan, mode)

# =================================================
# mean (rata-rata)
meanAges = np.mean(ages)
print('rata-rata pada data: ', meanAges)

# =================================================
# median (nilai tengah --> setelah data disorting)
medianAges = np.median(ages)
print('nilai tengah pada data: ', medianAges)

# =================================================
# mode (nilai yang paling sering muncul)
modeAges = stats.mode(ages).mode
print('mode pada data: ', modeAges)

# Setelah mengetahui basic fungsi statistic, berikut syntax untuk mencari standar devaiasi & variasi

# =================================================
# Standar deviasi (menghitung seberapa jauh penyebaran data yang terjdai pada data)
stdAges = np.std(ages)
print('standar deviasi data: ',stdAges)

# =================================================
# Varian (yaitu cara lain yang dapat mendefinisikan penyebaran data)
# varian juga merupakan sqrt(standar deviasi)
varianAges = np.var(ages)
print('varian pada data: ', varianAges)


# =================================================
# Kita lanjut dengan persentil (nilai, yang melebihi n persen dari keseluruhan data)
# value yang melebihi 10% dari all data
percentileData10 = np.percentile(ages, 10)
# value yang melebihi 75% dari all data
percentileData75 = np.percentile(ages, 75)
print('persentil 10% dari data: ' , percentileData10)
print('persentil 75% dari data: ' , percentileData75)


# =================================================
# operating factorial and combination function from scipy library
# combination

# =================================================
exComb = comb(3,2) #C(n,k) which n > k
print('C(3,2) = {}'.format(exComb))

# =================================================
# factorial
exFact = factorial(n = 5)
print('5 Factorial: ', exFact)
