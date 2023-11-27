import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('Data_remaja_aug_2022.csv')
# print(df)
print(df.columns)
print(df['NAMA LENGKAP (NAMA + NAMA BELAKANG/MARGA)'].unique)