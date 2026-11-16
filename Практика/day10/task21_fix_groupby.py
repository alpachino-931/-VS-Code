# Задание 21. Исправленный groupby: метод вызывается через скобки

import pandas as pd

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Баллы"].mean()

print(result)
