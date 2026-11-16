# Задание 16. Прочитай файл

with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
