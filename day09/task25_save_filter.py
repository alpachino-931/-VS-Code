# Задание 25. Сохраните фильтр

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

result = df[df["Баллы"] >= 80]
result.to_csv("high_scores.csv", index=False, encoding="utf-8")

print(result)
