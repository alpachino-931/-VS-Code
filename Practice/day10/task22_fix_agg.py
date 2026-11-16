# Задание 22. Исправленный agg: список операций передается одним аргументом

import pandas as pd

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max"])

print(result)
