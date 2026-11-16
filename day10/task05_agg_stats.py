# Задание 5. Несколько показателей через agg()
import sys
import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

stats = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"])

print(stats)
