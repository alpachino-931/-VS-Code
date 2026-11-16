# Задание 3. Максимальный балл по группам

import pandas as pd

df = pd.read_csv("students.csv")

print(df.groupby("Группа")["Баллы"].max())
