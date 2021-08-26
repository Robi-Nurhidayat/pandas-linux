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
                        'KELAS' : ['IF6','IF6','IF6','IF6','IF6']},index=[np.array(np.arange(0,5))])
    
print(data2)


data3 = pd.DataFrame({'NIM' : [10118260,10118261,10118262,10118263,10118264],
                        'NAMA' : ['Nurhidayat', 'Asep', 'Faishal', 'Perdana Yusuf', 'Fauzan'],
                        'KELAS' : ['IF7','IF7','IF7','IF7','IF7']},index=[np.array(np.arange(5,10))])


data4 = pd.DataFrame({'NIM' : [10118270,10118271,10118272,10118273,10118274],
                        'NAMA' : ['Bambang', 'Ari', 'Fikri', 'Yusuf', 'Adi'],
                        'KELAS' : ['IF8','IF8','IF8','IF8','IF8']},index=[np.array(np.arange(10,15))])


# menjumlahkan dataframe
dataJumlah = pd.concat([data2,data3,data4], axis=0)

print(dataJumlah)


# mengelompokkan dataframe dengan fungsi groupby

bisnis = pd.DataFrame(
    {
        'perusahaan' : ['telkomsel','indosat','axis','xl','xl','indosat','tree','smartfren'],
        'karyawan' : ['agus','jaka','robi','bagus','eni','adi','asep','cicit'],
        'age' : [21,22,23,25,28,23,20,30]
    }
)


print(bisnis)

# kita bisa kelompokkan dengan fungsi groupby

print(bisnis.groupby('perusahaan').sum())
print(bisnis.groupby('perusahaan').count())
print(bisnis.groupby('perusahaan').mean())
print(bisnis.groupby('perusahaan').min())
print(bisnis.groupby('perusahaan').max())
print(bisnis.groupby('perusahaan').age.min())
print(bisnis.groupby('perusahaan').describe().transpose())

print('yang bawah tanpa grup by \n\n\n')

print(bisnis.groupby('perusahaan'))
# print(bisnis['perusahaan'])