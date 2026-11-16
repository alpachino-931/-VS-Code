# Задание 10. Средняя посещаемость по группам

import pandas as pd

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Посещено"].mean().reset_index()
result.to_csv("average_attendance.csv", index=False, encoding="utf-8")

print(result)
print("Файл average_attendance.csv создан")
