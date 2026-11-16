# Задание 1. Средний балл по группам
import sys
import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

print(df.groupby("Группа")["Баллы"].mean())
