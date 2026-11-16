# Задание 28. Исправленная сортировка: sort_values вызывается через скобки

import pandas as pd

df = pd.read_csv("students.csv")

result = df.sort_values("Баллы", ascending=False)

print(result)
