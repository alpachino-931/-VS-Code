# Задание 13. Сортировка по баллам по убыванию

import pandas as pd

df = pd.read_csv("students.csv")

print(df.sort_values("Баллы", ascending=False))
