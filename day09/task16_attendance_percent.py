# Задание 16. Процент посещаемости

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")
df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)

print(df)
