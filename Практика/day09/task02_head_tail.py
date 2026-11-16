# Задание 2. Первые и последние строки

import pandas as pd

df = pd.read_csv("students.csv")

print(df.head(3))
print(df.tail(2))
