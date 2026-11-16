# Задание 16. Прочитай файл

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
