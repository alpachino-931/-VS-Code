# Задание 24. Сохраните всю таблицу

import pandas as pd

df = pd.read_csv("students.csv")

df.to_csv("all_students_result.csv", index=False, encoding="utf-8")

print("Файл all_students_result.csv создан")
