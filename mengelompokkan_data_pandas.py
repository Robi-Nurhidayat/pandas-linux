import numpy as np
import pandas as pd

# buat dataframe
# menggunakan cara biasa
np.random.seed(100)
baris = np.array(np.arange(1,6))
column = np.array(['A','B','C','D','E'])
isi_data1 = np.random.randint(1,100,25).reshape(5,5)

data1 = pd.DataFrame(isi_data1,baris,column)

print(data1)


# buat dataframe menggunnakan dictionary

data2 = pd.DataFrame({'NIM' : [10118252,10118253,10118254,10118255,10118256],
                        'NAMA' : ['Robi Nurhidayat', 'Ramadhani', 'Muhammad Faishal Azizi', 'Bagus Perdana Yusuf', 'Muhammad Fauzan'],
                        'KELAS' : ['IF6','IF6','IF6','IF6','IF6']})
    
print(data2)