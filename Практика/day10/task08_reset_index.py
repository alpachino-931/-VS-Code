# Задание 8. reset_index()

import pandas as pd

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Баллы"].mean().reset_index()

print(result)
