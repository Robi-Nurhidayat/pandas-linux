import numpy as np
import pandas as pd

# list angka

angka = [1,2,3,4,5]

# list simbol

simbol = ['A','B','C','D','E']

# angka diubah ke series pandas

angka_series = pd.Series(angka,index=simbol)
print(angka_series)
print(type(angka_series))


# mengubah list ke array di numpy kemudian dijadikan pandas series

np.random.seed(20)
angka2 = np.array(angka)

angka2 = pd.Series(angka2)

print(angka2)


# dictionary

dic = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}


dic = pd.Series(dic)

print(dic)