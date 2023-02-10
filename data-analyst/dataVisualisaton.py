# Untuk visualisasi data pada Python, kita akan menggunakan llibrary pandas
import pandas as pd
import matplotlib.pyplot as plt
data_kopi = {'jenis_kopi' : ['Latte', 'Cappucino', 'Americano', 'Espresso'], 'total_omset': [942, 1716, 731,220]}

def tableChart():
    # visualisasi data menggunakan table chart di pandas
    kopi_df = pd.DataFrame(data_kopi)
    print(kopi_df) # -->
    '''
    Bentuk visualisasi yang dihasilkan
    jenis_kopi  total_omset
    0      Latte          942
    1  Cappucino         1716
    2  Americano          731
    3   Espresso          220
    Perlu diingat! Bahwa length pada class(jenis_kopi, total_omset) haruslah sama, jika tidak, maka akan menghasilkan error
    '''

def pieChart():
    # Visualisasi data Pie Chart pada Pandas
    kopi_df = pd.DataFrame(data_kopi)
    # Untuk memvisualisasi data menggunakan pie chart kita perlu statement sebagai berikut:
    kopi_df = kopi_df.plot(kind = 'pie', y='total_omset', labels = kopi_df['jenis_kopi'], autopct = '%1.1f%%', startangle = 90, legend = False, figsize = (12,8))
    plt.show()

pieChart()
 