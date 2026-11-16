# Задание 28. Исправленная сортировка: sort_values вызывается через скобки

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

result = df.sort_values("Баллы", ascending=False)

print(result)
