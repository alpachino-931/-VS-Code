# Практика по Python

Учебные работы за 1 курс: от основ синтаксиса до анализа данных.

## Что внутри

| Папка | Тема |
|---|---|
| `Practice/day01` | Основы Python, виртуальное окружение |
| `Practice/day02` | Типы данных и ввод с клавиатуры |
| `Practice/day03` | Условия и логические операторы |
| `Practice/day04` | Списки и словари |
| `Practice/day05` | Циклы и работа с файлами |
| `Practice/day06` | NumPy: одномерные массивы |
| `Practice/day07` | NumPy: двумерные массивы |
| `Practice/day08` | Pandas: Series и DataFrame |
| `Practice/day09` | Pandas: CSV, фильтрация, пропуски |
| `Practice/day10` | Pandas: groupby и графики |

В каждой папке лежат файлы по заданиям и итоговая работа `final_dayN.py`.
Результаты сохраняются рядом: таблицы в CSV, графики в PNG.

## Запуск

```
python Practice/day10/task01_mean_by_group.py
```

Скрипты сами переходят в свою папку, поэтому запускать можно откуда угодно.

Для дней 9 и 10 нужны библиотеки:

```
pip install pandas matplotlib
```
