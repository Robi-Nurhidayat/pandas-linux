import numpy as np
import pandas as pd

# belajar membuat dataframe dari nol

np.random.seed(100)

dataku = pd.DataFrame(np.random.randn(3,4),['A','B','C'],['Satu','Dua','Tiga','Empat'])

print(dataku)

# menambahkan column baru

dataku['data_baru'] = dataku['Empat'] + dataku['Tiga']

print(dataku)


# menghapus column
# jika menggunakan cara dibawah ini harus ditampung kedalam variable dulu agar dihapus secara permanen

print(dataku.drop('Dua',axis=1))


# jika tidak ingin ditampung di dalam variabel
# maka gunakan inplace = True

dataku.drop('Satu', axis=1, inplace=True)

print(dataku)

# menghapus baris,, tinggal ganti axis nya jadi = 0

dataku.drop('A', axis=0, inplace=True)

print(dataku)

print(dataku.shape)


# melakukan proses komparasi

dataku_bol = dataku > 0

print(dataku_bol)

print(dataku[dataku_bol])

dataku = dataku[dataku > 0]

print(dataku)


dataku2 = pd.DataFrame(np.random.randn(3,4),['A','B','C'],['Satu','Dua','Tiga','Empat'])

print(dataku2, '\n\n')


hasil = dataku2[dataku2['Satu'] > 0]
hasil2 = dataku2['Satu'] > 0

print('hasil 1')
print(hasil, '\n\n')

print('hasil 2')
print(hasil2)
