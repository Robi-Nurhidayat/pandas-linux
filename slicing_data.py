import pandas as pd

data1 = pd.read_csv('./data/kapal_titanic.csv')

print(data1.head(5),'\n')

# slicing sperti list

print(data1['sex'].head(5), '\n')

# slicing dengan list lebih dari 1 atribut

print(data1[['sex','age']].head(5), '\n')

# slicing dengan dot notation (.)

print(data1.head().fare, '\n')

# slicing dengan menggunakan fungsi iloc
# iloc adalah fungsi yang digunakan untuk melakukan slicing dengan ketentuan iloc[baris,Column]
# apabila namaColumn tidak diisi maka secara default akan mengambil baris aja
# iloc juga sperti list bisa mengambil indeks dengan rentang tertentu
# example

print(data1.iloc[:4], '\n')
print(data1.iloc[:,3].head(5), '\n')
print(data1.iloc[-5:-2, -5:-2], '\n')

# untuk slicing dengan rentang tertentu menggunakan iloc maka penulisann nya iloc[[x,x,x],[z,z,z]]
# example

print(data1.iloc[[0,2,4],[-1,1,2]], '\n\n')


# slicing menggunakan loc
# jika tisak tahu urutan / indeks nya bisa menggunakan loc sebagai pengganti iloc
# jika ingin menggunakan nama nya langsung


data2 = pd.read_csv('./data/kapal_titanic.csv', index_col='embarked')

print(data2.head(5),'\n')

print(data2.head(5).loc['S', 'age'],'\n')

# jika ingin lebih dari satu slicing

print(data2.loc[['S','Q'], ['fare','age']])


# kesimpulan
# perbedaan iloc dann loc
# iloc slicing dengan nomor baris atau column
# sedangkan loc menggunakann nama column dan baris
