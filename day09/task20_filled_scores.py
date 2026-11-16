# Задание 20. Только заполненные баллы

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

missing_df = pd.read_csv("students_missing.csv", encoding="utf-8")

print(missing_df[missing_df["Баллы"].notna()])
