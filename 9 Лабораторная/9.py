#Задание Окно регистрации пользователя.
import os
from tkinter import *
from tkinter import messagebox
def registr_user():     # Регистрируем пользователя
    if not login.get() or not parol.get():
        messagebox.showerror("Ошибка", "'Логин' и 'Пароль' должны быть заполнены.")
    elif proverka_logina():
        messagebox.showerror("Ошибка", "Учетная запись уже существует.")
    else:
        with open("users.txt", "a") as file:
            file.write(f"{login.get()}:{parol.get()}\n")
        messagebox.showinfo("Успех","Регистрация успешно завершена.\nВойдите в аккаунт")
def proverka_logina():      # Проверяем наличие логина в файле
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            lines = file.readlines()
            login_vvod = login.get()
            for line in lines:
                if login_vvod in line:
                    return True
        return False
def proverka_users():  # Проверяем наличие данных в файле о пользователе
    if os.path.exists("users.txt"):
        file = open("users.txt", "r+")
        lines = file.readlines()
        login_vvod = login.get()
        parol_vvod = parol.get()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                sohranenii_login, sohranenii_password = parts
                if login_vvod == sohranenii_login and parol_vvod == sohranenii_password:
                    return True
        return False
def enter_users():  # Атвторизуем пользователя
    if proverka_users():
        messagebox.showinfo("Успех!", "Вы вошли в свой аккаунт")
        root.destroy()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")
root = Tk()  # Создаем окно
root.title("Регистрация/вход")
root.geometry("400x300")
Label_login = Label(text="Логин")
Label_login.pack(padx=6, pady=6)
login = Entry(bd=2)
login.pack(padx=6, pady=6)
Label_parol = Label(text="Пароль")
Label_parol.pack(padx=6, pady=6)
parol = Entry(bd=2)
parol.pack(padx=6, pady=6)
vhod_btn1 = Button(text="Войти",command=enter_users)
vhod_btn1.pack(padx=6, pady=6)
registr_btn2 = Button(text="Зарегистрироваться",command=registr_user)
registr_btn2.pack(padx=6, pady=6)
root.mainloop()
