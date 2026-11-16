# Задание 27. Исправленный фильтр: каждое условие в круглых скобках

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

result = df[(df["Баллы"] >= 80) & (df["Посещено"] >= 16)]

print(result)
