# Задание 22. Удаление пропусков

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

missing_df = pd.read_csv("students_missing.csv", encoding="utf-8")

clean_df = missing_df.dropna()
clean_df = clean_df.reset_index(drop=True)

print(clean_df)
