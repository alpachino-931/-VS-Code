# Задание 19. Список технологий в файл

technologies = ["Python", "Git", "SQL", "Docker", "Linux"]

with open("technologies.txt", "w", encoding="utf-8") as file:
    for technology in technologies:
        file.write(technology + "\n")

print("Файл technologies.txt создан")
