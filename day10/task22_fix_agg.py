# Задание 22. Исправленный agg: список операций передается одним аргументом
import sys
import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

result = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max"])

print(result)
