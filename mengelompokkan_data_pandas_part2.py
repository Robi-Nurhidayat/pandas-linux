import pandas as pd
import numpy as np

# mengabungkan tipe data seperti sql

satu = pd.DataFrame({
    'id' : [i for i in range(0,5)],
    'nama' : ['robi','adi','asep','jaka','ari'],
    'usia' : [20,29,20,22,21]
 })


print(satu)


dua = pd.DataFrame({
    'id' : [i for i in range(0,5)],
    'nama' : ['robi','adi','asep','jaka','ari'],
    'usia' : [20,29,20,22,21]
 })


# gabungkan dengan metod merge
# khusus untuk column

gabung = pd.merge(satu,dua,how='inner',on='id')


print(gabung)


tiga = pd.DataFrame({
    'id1' : [i for i in range(0,5)],
    'id2' : [0,2,3,4,5],
    'nama' : ['robi','adi','asep','jaka','ari'],
    'usia' : [20,29,20,22,21]
 })


empat = pd.DataFrame({
    'id1' : [i for i in range(0,5)],
    'id2' : [0,1,3,4,5],
    'nama' : ['robi','adi','asep','jaka','ari'],
    'usia' : [20,29,20,22,21]
 })

gabung2 = pd.merge(tiga, empat, how='outer', on=['id1','id2'])

print(gabung2)


# khusus untuk baris mengunakan join

benda1 = pd.DataFrame({
    'kode' : [i for i in range(1,4)],
    'nama' : ['jambu','Air','Es'],
},index=['K1','K2','K3'])

print(benda1)

benda2 = pd.DataFrame({
    'kode' : [i for i in range(1,4)],
    'nama' : ['jambu','Air','Es'],
},index=['K1','K2','K4'])

# default how = 'left'
# gabungJoinBenda = benda1.join(benda2.set)

# print(gabungJoinBenda)