# Задание 10. Средняя посещаемость по группам
import sys
import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

result = df.groupby("Группа")["Посещено"].mean().reset_index()
result.to_csv("average_attendance.csv", index=False, encoding="utf-8")

print(result)
print("Файл average_attendance.csv создан")
