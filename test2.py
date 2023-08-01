def tanaman_xiao(M, N, R, P, lahan):
    tanaman = []
    sumber_racun = []
    ans = []
    for i in range(M):
        for j in range(N):
            if lahan[i][j] == 1:
                tanaman.append([i, j])
            elif lahan[i][j] == 2:
                sumber_racun.append([i, j])
    for tanam in tanaman:
        n_racun = 0
        for racun in sumber_racun:
            if abs(tanam[0]-racun[0]) <= R and abs(tanam[1]-racun[1]) <= R:
                n_racun += 1
        print(tanam, n_racun)
        if n_racun <= P:
            ans.append(tanam)
    return ans

M, N, R, P = list(map(int, input().split()))
lahan = []
for _ in range(M):
    lahan.append(list(map(int, input().split())))

print(tanaman_xiao(M, N, R, P, lahan))
