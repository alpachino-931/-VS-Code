# Задание 9. Низкая посещаемость

import pandas as pd

df = pd.read_csv("students.csv")

print(df[df["Посещено"] < 16])
