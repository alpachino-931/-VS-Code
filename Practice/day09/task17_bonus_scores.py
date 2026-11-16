# Задание 17. Бонусные баллы

import pandas as pd

df = pd.read_csv("students.csv")
df["Баллы+5"] = df["Баллы"] + 5

print(df)
