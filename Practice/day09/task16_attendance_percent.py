# Задание 16. Процент посещаемости

import pandas as pd

df = pd.read_csv("students.csv")
df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)

print(df)
