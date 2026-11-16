# Задание 25. Список участников

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

participants = []

for number in range(1, 4):
    name = input("Введите имя участника " + str(number) + ": ")
    participants.append(name)

with open("participants.txt", "w", encoding="utf-8") as file:
    for participant in participants:
        file.write(participant + "\n")

print("Файл participants.txt создан")
