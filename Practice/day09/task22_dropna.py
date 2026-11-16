# Задание 22. Удаление пропусков

import pandas as pd

missing_df = pd.read_csv("students_missing.csv")

clean_df = missing_df.dropna()
clean_df = clean_df.reset_index(drop=True)

print(clean_df)
