# Задание 19. Список технологий в файл

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

technologies = ["Python", "Git", "SQL", "Docker", "Linux"]

with open("technologies.txt", "w", encoding="utf-8") as file:
    for technology in technologies:
        file.write(technology + "\n")

print("Файл technologies.txt создан")
