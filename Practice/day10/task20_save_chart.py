# Задание 20. Сохраните график в PNG

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.plot(df["Имя"], df["Баллы"], marker="o")
plt.title("Баллы студентов")
plt.xlabel("Студент")
plt.ylabel("Баллы")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("students_scores.png")
plt.show()

print("Файл students_scores.png создан")
