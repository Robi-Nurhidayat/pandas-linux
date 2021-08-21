import pandas as pd

dataku = pd.read_csv('./data/kapal_titanic.csv')

print(dataku.head(3))

print(dataku.info())

print(dataku.describe())

print(dataku.describe(include='O'))