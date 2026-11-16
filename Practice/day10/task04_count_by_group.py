# Задание 4. Количество студентов в группе

import pandas as pd

df = pd.read_csv("students.csv")

print(df.groupby("Группа")["Имя"].count())
