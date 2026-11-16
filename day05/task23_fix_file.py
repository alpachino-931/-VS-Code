# Задание 23. Исправленная программа: запятые, двоеточие, отступ

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Привет")

print("Файл data.txt создан")
