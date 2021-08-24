import pandas as pd
import numpy as np

data_kematian = pd.read_csv('./data/data_kematian_kelurahan.csv')

print(data_kematian)

print(data_kematian.info())

jumlah = data_kematian['jumlah']

print(jumlah)

jumlah_bersih = jumlah.dropna()

print(jumlah_bersih, '\n\n\n')

jumlah_kematian = data_kematian[data_kematian['jumlah'] > 10]

print(jumlah_kematian['jumlah'].count(), '\n\n\n')
print(jumlah_kematian['jumlah'].sum(), '\n\n\n')

data_kematian['jumlah'] = data_kematian['jumlah'].fillna(value=data_kematian['jumlah'].mean())
print(data_kematian['jumlah'].values)