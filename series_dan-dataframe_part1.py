import pandas as pd
import numpy as np

label = ['satu', 'dua', 'tiga']

angka = [10,20,30]

np_angka = np.array(angka)

# print(np_angka)

dictionary = {
    'satu' : 10,
    'dua'  : 20,
    'tiga' : 30
}


# print(dictionary)


# cara membuat pandas series dengan menggunakan keyword pd.Series

# mengubah list menjadi series
dataku1 = pd.Series(angka, index=label)
print(dataku1['satu'])


# mengubah array ke series
print(pd.Series(np_angka))


# memasukkan dictionari menjadi pandas series

dataDic = pd.Series(dictionary)

print(dataDic)

# mengubah data list / array / dictionary menjadi dataframe
# sebelum melakukan nya ubah dulu masing2 menjadi series

# dic
dataDicFrame = dataDic.to_frame()

print(dataDicFrame)

# list
dataListFrame = dataku1.to_frame()
print(dataListFrame)


# menjumlahkan dataframe

# kita buat lagi dic

dictionary2 = {
    'satu' : 10,
    'dua'  : 20,
    'tiga' : 30,
    'empat' : 40,
    'lima' : 50
}


# ubah dic 2 menjadi series dulu

dataDic2 = pd.Series(dictionary2)

# ubah ke dataframe
dataDicFrame2 = dataDic2.to_frame()

# jumlahkan data dic 1 frame dan data dic 2 frame
# agar lebih mudah tampung ke dalam variable

jumlahDic = dataDicFrame + dataDicFrame2

print(jumlahDic)