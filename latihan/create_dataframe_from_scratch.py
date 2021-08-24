import numpy as np
import pandas as pd

data = np.random.randint(1,10,10)
print(data, '\n\n')

# membuat dataframe dari 0



column = np.array(np.arange(1,5+1))
baris = np.array(np.arange(0,4))
isi_data_frame = np.random.randint(1,100,20).reshape(4,5)

dataframe = pd.DataFrame(isi_data_frame,baris,column)

print(dataframe)

# menampilkan statistik describe
print(dataframe.describe())


# slicing salah 1 data

print(dataframe[1])

