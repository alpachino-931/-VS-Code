# Задание 15. Создай файл

with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

print("Файл hello.txt создан")
