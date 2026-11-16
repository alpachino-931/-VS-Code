# Задание 20. Прочитай построчно

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

with open("technologies.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
