# День 10. Pandas: группировка и агрегация. Основы Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
print(df.head())

print("=" * 40)
print(df.groupby("Группа")["Баллы"].mean())
print(df.groupby("Группа")["Баллы"].sum())
print(df.groupby("Группа")["Баллы"].min())
print(df.groupby("Группа")["Баллы"].max())
print(df.groupby("Группа")["Имя"].count())

print("=" * 40)
stats = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"])
print(stats)

print("=" * 40)
result = df.groupby("Группа")[["Баллы", "Посещено"]].mean()
print(result)

print("=" * 40)
df["Статус"] = "зачет"
print(df.groupby(["Группа", "Статус"])["Баллы"].mean())

print("=" * 40)
result = df.groupby("Группа")["Баллы"].mean().reset_index()
result = result.sort_values("Баллы", ascending=False)
print(result)
result.to_csv("group_result.csv", index=False, encoding="utf-8")

print("=" * 40)
plt.bar(result["Группа"], result["Баллы"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("chart.png")
plt.show()

print("=" * 40)
plt.plot(df["Имя"], df["Баллы"], marker="o")
plt.title("Баллы студентов")
plt.xlabel("Студент")
plt.ylabel("Баллы")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("students_chart.png")
plt.show()

print("Файлы group_result.csv, chart.png и students_chart.png созданы")
