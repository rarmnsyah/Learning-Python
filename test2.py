def calculate_score(m, n, matrix):
    score = 0
    
    for _ in range(n):
        max_val = 0
        max_index = None
        
        # Cari nilai maksimum pada setiap matriks m
        for i in range(m):
            if matrix[i] > max_val:
                max_val = matrix[i]
                max_index = i
        
        # Tambahkan nilai maksimum ke skor
        score += max_val
        
        # Hapus nilai maksimum dari matriks m
        matrix[max_index] = 0
    
    return score

# Input dari pengguna
m, n = map(int, input().split())
matrix = list(map(int, input().split()))

# Panggil fungsi untuk menghitung skor
score = calculate_score(m, n, matrix)

# Output skor
print(score)
