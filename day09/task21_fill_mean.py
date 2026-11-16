# Задание 21. Заполнение средним

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

missing_df = pd.read_csv("students_missing.csv", encoding="utf-8")

average = missing_df["Баллы"].mean()
missing_df["Баллы"] = missing_df["Баллы"].fillna(average)

print(missing_df)
