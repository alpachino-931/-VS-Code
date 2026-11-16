# Задание 6. Два числовых столбца

import pandas as pd

df = pd.read_csv("students.csv")

result = df.groupby("Группа")[["Баллы", "Посещено"]].mean()

print(result)
