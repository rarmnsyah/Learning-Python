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
        if n_racun <= P:
            ans.append(tanam)
    return ans

M, N, R, P = list(map(int, input().split()))
lahan = []
for _ in range(M):
    lahan.append(list(map(int, input().split())))

ans = tanaman_xiao(M, N, R, P, lahan)
for i in ans:
    print('{} {}'.format(i[0],i[1]))

'''
Jawaban Java

public static List<List<Integer>> TanamanObatXiao(int M, int N, int R, int P, List<List<Integer>> lahan) {
    List<List<Integer>> tanaman = new ArrayList<>();
    List<List<Integer>> sumber_racun = new ArrayList<>();
    List<List<Integer>> ans = new ArrayList<>();
    
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            List<Integer> temp = new ArrayList<>();
            temp.addAll(Arrays.asList(i, j));
            if (lahan.get(i).get(j) == 1) {
                tanaman.add(temp);
            } else if (lahan.get(i).get(j) == 2) {
                sumber_racun.add(temp);
            }
        }
    }
    
    for (List<Integer> tanam : tanaman) {
        int n_racun = 0;
        for (List<Integer> racun : sumber_racun) {
            if (Math.abs(tanam.get(0) - racun.get(0)) <= R && Math.abs(tanam.get(1) - racun.get(1)) <= R) {
                n_racun++;
            }
        }
        if (n_racun <= P) {
            ans.add(tanam);
        }
    }
    
    return ans;
}
    
'''
