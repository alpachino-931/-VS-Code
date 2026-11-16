# Задание 7. Высокие баллы

import pandas as pd

df = pd.read_csv("students.csv")

print(df[df["Баллы"] >= 80])
