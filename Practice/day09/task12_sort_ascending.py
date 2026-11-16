# Задание 12. Сортировка по баллам

import pandas as pd

df = pd.read_csv("students.csv")

print(df.sort_values("Баллы"))
