import tkinter as tk
from tkinter import filedialog
import os
import chardet
# верхние библиотеки не изучал
import openpyxl

from openpyxl import load_workbook
import pandas as pd
from typing import Any
# в программу подается файл со списком входящих звонков за период времени.
# программа вычисляет количество всех входящих  звонков и количество уникальных входящих .
# программа вычисляет % повторных звонков(сколько из 100 звонков позвонили еще раз)

def select_file():
    """Открывает окно выбора файла"""
    root = tk.Tk()
    root.withdraw()  # скрыть главное окно

    file_path = filedialog.askopenfilename(
        title="Выберите  файл",
        filetypes=[
            ("All files", "*.*")
        ]
    )

    return file_path

# Использование
file_path = select_file()
if file_path:
    print(f"Выбран файл: {file_path}")

# старт моей программы

def operations(file_path)->float:


    # df = pd.read_csv(file_path, encoding='windows-1251')# из манго офис скачивается именно  csv файл
    # df.to_excel(file_path, index=False)# сохраняем как иксель
    df = pd.read_excel(file_path, header=1)

    df = df[df["Участники"].str.contains("КЦ", na=False)]#фильтрует по столбцу участники - выбирает только строки содержащие КЦ
    df= df.iloc[:,[2]]#срез, копирует в память только 3 столбец
    df_clean = df.drop_duplicates()#присваивает новой переменной отфильтрованный датафрейм(3 столбец), в котором нет дубликатов строк

    df_clean.to_excel(file_path, index=False) #перезаписывает новые данные в старый файл
    wb = load_workbook(file_path)
    wb.active["B1"] = "количество всех входящих"
    wb.active["C1"] = "количество уникальных входящих"
    wb.active["D1"] = "доля повторных звонков"
    wb.active["B2"] = len(df)

    wb.active["C2"] = len(df_clean)
    partclean = round((len(df)-len(df_clean))/len(df)*100, 2)
    wb.active["D2"] = partclean

    wb.save(file_path)
    print("доля повторных звонков: ", partclean)
    print()
operations(file_path)
