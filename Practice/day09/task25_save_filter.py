# Задание 25. Сохраните фильтр

import pandas as pd

df = pd.read_csv("students.csv")

result = df[df["Баллы"] >= 80]
result.to_csv("high_scores.csv", index=False, encoding="utf-8")

print(result)
