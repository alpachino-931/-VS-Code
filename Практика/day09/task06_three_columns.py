# Задание 6. Три столбца

import pandas as pd

df = pd.read_csv("students.csv")

print(df[["Имя", "Группа", "Посещено"]])
