# Задание 25. Анализ учебных групп
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

df = pd.read_csv("students.csv", encoding="utf-8")

stats = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"])
stats = stats.reset_index()
print(stats)

stats.to_csv("group_analysis_result.csv", index=False, encoding="utf-8")

plt.bar(stats["Группа"], stats["mean"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("group_analysis.png")
plt.show()

print("Файлы group_analysis_result.csv и group_analysis.png созданы")
