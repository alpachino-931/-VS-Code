# Задание 8. Одна группа

import pandas as pd

df = pd.read_csv("students.csv")

print(df[df["Группа"] == "1ИИ-2"])
