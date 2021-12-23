# Primary key adalah dictionary sebagai key untuk mengakses soal, bobot soal, dan jawaban
primaryKey = {
    'Kecepatan':['Sebuah kelereng mula-mula dalam keadaan diam pada lantai yang licin, kemudian kelereng didorong sehingga mengalami percepatan sebesar 2 m/s^2, tentukan kecepatan kelereng setelah bergerak selama 4 sekon.\n\nA. 8 m/s\t\tB. 16 m/s\nC. 9 m/s\t\tD. 18m/s', 10, 'A'],
    'Jarak Tempuh Mobil':['Pada awalnya, Pak Indro mengendarai mobilnya dengan kecepatan tetap 20 m/s. Tiba-tiba, mobil tersebut direm sehingga mengalami perlambatan 10 m/s^2. Berapakah jarak yang ditempuh oleh mobil tersebut sampai berhenti? \n\nA. 10 m\t\tB. 20 m\nC. 15 m\t\tD. 25 m', 35, 'B'],
    'Jarak Tempuh Mobil Balap':['Sebuah mobil balap direm dengan perlambatan konstan dari kelajuan 25 m/s menjadi 15 m/s dalam jarak 40 m. Jarak total (dalam meter) yang telah ditempuh oleh mobil tersebut sampai akhirnya berhenti adalah \n\nA. 42,5 m\t\tB. 125 m\nC. 62,5 m\t\tD. 145 m', 40, 'C'],
    'Kecepatan Akhir':['Pada suatu perlombaan becak, sebuah becak dikayuh dengan kecepatan awal 2 m/s dan percepatan 2 m/s^2. Tentukanlah kecepatan becak setelah menempuh jarak 15 meter.\n\nA. 9 m\s\t\tB. 4 m\s\nC. 8 m\s\t\tD. 3 m\s', 15, 'C'],
    'Waktu Pengereman Kereta':['Diketahui sebuah kereta bergerak dengan kecepatan konstan 30 m/s. Kereta mengalami perlambatan 4 m/s2 hingga berhenti di stasion. Waktu yang dibutuhkan kereta hingga berhenti adalah… \n\nA. 7,5 s\t\tB. 6,5 s\nC. 4 s\t\tD. 10 s',70, 'B'],
    'Hukum 1 Newton':['Balok bermassa 20 kg berada di atas bidang miring licin dengan sudut kemiringan 30o. Jika Ucok ingin mendorong ke atas sehingga kecepatannya tetap maka berapakah gaya yang harus diberikan oleh Ucok?\n\nA. 125 N\t\tB. 50 N\nC. 75 N\t\tD. 100 N',25, 'D'],
    'Hukum 2 Newton':['Balok A bermassa 4 kg diletakkan di atas balok B yang bermassa 6 kg. Kemudian balok B ditarik dengan gaya F di atas lantai mendatar licin sehingga gabungan balok itu mengalami percepatan 1,8 m/s2. Jika tiba-tiba balok A terjatuh maka berapakah percepatan yang dialami oleh balok B saja?\n\nA. 3 m/s^2\t\tB. 6 m/s^2\nC. 9 m/s^2\t\tD. 12 m/s^2',55, 'A'],
    'Hukum 3 Newton':['Sebuah pesawat antariksa diluncurkan dengan menggunakan roket. Roket ini mempunyai tiga tabung gas. Setiap tabung dalam 1 sekon mampu menyemburkan 5 kg gas dengan kecepatan 400 m/s. Jika massa total roket dan pesawat ulang-alik 2 ton, berapakah percepatan roket 1 sekon setelah peluncuran?\n\nA. 16 m/s^2\t\tB. 14 m/s^2\nC. 8 m/s^2\t\tD. 7 m/s^2',85, 'D'],
    'Gaya Gesek':['Sebuah peti bermassa 50 kg, mula-mula diam di atas lantai horizontal kasar (μk = 0,1; μs = 0,5). Kemudian peti itu didorong dengan gaya F = 100 N yang arahnya membentuk sudut θ terhadap arah horizontal. Jika sin θ = 0,6 dan cos θ = 0,8. Gaya gesek yang dialaminya sebesar…\n\nA. 160 N\t\tB. 80 N\nC. 40 N\t\tD. 90 N',95, 'B']
}

# soal adalah dictionary untuk mengakses soal dari key yang sudah disediakan
soal = {}


for i in primaryKey:
    soal[i] = primaryKey[i][0]
# 'Kecepatan' : 'Sebuah.....'

bobotSoal = {}
for i in primaryKey:
    bobotSoal[i] = primaryKey[i][1]
# 'Kecepatan' : 10

jawaban = {}
for i in primaryKey:
    jawaban[i] = primaryKey[i][2]

def difficulty(nums):
    if nums in range(0,30): return 'Easy'
    elif nums in range(30,60): return 'Medium'
    else: return 'Hard'

dictDifficulty = {}
for i in bobotSoal:
    dictDifficulty[i] = difficulty(bobotSoal[i])



OpsiDifficulty = {
    '1' : 'easy',
    '2' : 'medium',
    '3' : 'hard'
}