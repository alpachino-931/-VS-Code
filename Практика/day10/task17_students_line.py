# Задание 17. Баллы студентов на линейном графике

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.plot(df["Имя"], df["Баллы"])
plt.title("Баллы студентов")
plt.xlabel("Студент")
plt.ylabel("Баллы")
plt.show()
