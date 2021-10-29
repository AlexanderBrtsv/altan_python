# ***Генератор паролей***

# Импортирование модулей
# import tkinter
from tkinter import Tk, StringVar, Label, Entry, Button
import hashlib
from typing import Text

# объект окна
window = Tk()
window.title("Генератор паролей v.0.1")

# Основная функция
def generator():
    """
    Функция хеширования строк паролей
    """
    # Прием строки сырой пароли 
    pwd_str = pwd.get()
    # кодирование в байт-строку
    byte_str = pwd_str.encode()

    # хеширование (применение хеш-функции)
    hash_str = hashlib.sha256(byte_str)

    # преобразование объект хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]


    # print(hex_str)

    # Запись хеш-строки в объект StringVar
    hash_pwd.set(hex_str)

# generator("password")

# Контейнер для хранения строк
pwd = StringVar()
hash_pwd = StringVar()

# Виджет (компонент) текстовой метки
Label(text="Пароль:").grid(row=0, column=0, padx=20, pady=20)

# Виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1, padx=20, pady=20)

# виджет кнопки
btn = Button(text="Start", command=generator)
btn.grid(row=0, column=2, padx=20, pady=20)

# виджет поля вывода 
Entry(textvariable=hash_pwd).grid(row=1, column=1, padx=20, pady=20)

# Запуск (точка входа программы)
window.mainloop()
