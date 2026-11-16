# Задание 30. Таблица товаров из CSV

import pandas as pd

df = pd.read_csv("products.csv")
df["Стоимость"] = df["Цена"] * df["Количество"]

result = df.sort_values("Стоимость", ascending=False)
print(result)

print("Товары с ценой выше 3000:")
expensive = result[result["Цена"] > 3000]
print(expensive)

result.to_csv("products_result.csv", index=False, encoding="utf-8")
print("Файл products_result.csv создан")
