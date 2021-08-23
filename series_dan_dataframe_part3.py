import pandas as pd
import numpy as np

# membaca data kapal titanic

# dataku = pd.read_csv('/data/kapal_titanic.csv')
dataku = pd.read_csv('kapal_titanic.csv')

print(dataku)

age = dataku.age

print(age)

print(age.describe())

print(age.count())


print(age.std())

print(age.median())


# jika inginn mendapatkan nilai tanpa na / nan bisa menggunakan method dropna
# drop cuma age series aja
age_bersih = age.dropna()

print(age_bersih, '\n\n\n')


# drop 1 dataframe jika ada nan nya

dataku2 = dataku.dropna(thresh=3) # kalo axis nya tidak disi maka tidak akan menampilkan baris yang ada nan nya


dataku3 = dataku.dropna(axis=1) # kalo axis nya 1 maka tidak akan tampil column yang ada nan nya

print(dataku2)
print(dataku3)


# masuk ke metod yang sangat penting

# jangan hapus data yang ada nan nya
# ganti nan dengan nilai rata2 dari colom itu

# untuk melakukan hal itu gunakan fillna

# example

dataku['age'] = dataku['age'].fillna(value=dataku['age'].mean())
print(dataku['age'].values)


# dimachine learning tidak dikenali data pandas series oleh karena itu
# ubah menjadi array
# cara nya sangat mudah , gunakan values

# dataku4_array = dataku4['age'].values

# print(dataku4_array)