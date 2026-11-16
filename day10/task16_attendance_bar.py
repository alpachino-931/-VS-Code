# Задание 16. Посещаемость на диаграмме
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")
result = df.groupby("Группа")["Посещено"].mean().reset_index()

plt.bar(result["Группа"], result["Посещено"])
plt.title("Средняя посещаемость по группам")
plt.xlabel("Группа")
plt.ylabel("Средняя посещаемость")
plt.grid()
plt.show()
