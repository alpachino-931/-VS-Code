# Задание 24. Сохраните всю таблицу

import os
import sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

df.to_csv("all_students_result.csv", index=False, encoding="utf-8")

print("Файл all_students_result.csv создан")
