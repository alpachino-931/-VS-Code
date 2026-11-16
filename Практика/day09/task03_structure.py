# Задание 3. Структура

import pandas as pd

df = pd.read_csv("students.csv")

print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
