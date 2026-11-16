# Задание 2. Минимальный балл по группам

import pandas as pd

df = pd.read_csv("students.csv")

print(df.groupby("Группа")["Баллы"].min())
