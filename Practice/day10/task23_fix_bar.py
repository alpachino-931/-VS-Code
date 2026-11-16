# Задание 23. Исправленный bar: аргументы в круглых скобках

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
result = df.groupby("Группа")["Баллы"].mean().reset_index()

plt.bar(result["Группа"], result["Баллы"])
plt.title("Средний балл по группам")
plt.show()
