# Задание 24. Журнал результатов

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

scores = [78, 55, 91, 60, 44]

with open("scores.txt", "w", encoding="utf-8") as file:
    for score in scores:
        file.write(str(score) + "\n")

with open("scores.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
