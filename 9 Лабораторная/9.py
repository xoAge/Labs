#Задание. Окно регистрации пользователя
from tkinter import *
from tkinter import messagebox
user_database = {}

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        if username in user_database:
            messagebox.showerror("Ошибка регистрации", "Пользователь с таким именем уже существует.")
        else:
            user_database[username] = password
            messagebox.showinfo("Регистрация успешна", "Регистрация прошла успешно. Пожалуйста, войдите с вашим именем и паролем.")
            register.destroy()
    else:
        messagebox.showwarning("Ошибка регистрации", "Пожалуйста, заполните оба поля.")
def login_user():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        if username in user_database and user_database[username] == password:
            messagebox.showinfo("Вход выполнен успешно", "Вход выполнен успешно.")
            login.destroy()
        else:
            messagebox.showerror("Ошибка входа", "Ошибка входа. Пожалуйста, проверьте ваше имя пользователя и пароль.")
    else:
        messagebox.showwarning("Ошибка входа", "Пожалуйста, заполните оба поля.")


register = Tk()
register.title('Регистрация')
register.geometry('300x250')
register.resizable(width=False, height=False)

reg_label = Label(register, text = 'Регистрация', font = 'Arial 15')
reg_label.pack()

username_label = Label(register, text='Логин', font = 'Arial 13')
username_label.pack()

username_entry = Entry(register, font = 'Arial 12')
username_entry.pack()

password_label = Label(register, text='Пароль', font = 'Arial 13')
password_label.pack()

password_entry = Entry(register, font = 'Arial 12')
password_entry.pack()

register_btn=Button(register, text = 'Регистрация', command = register_user)
register_btn.pack( padx=10, pady=20)
register.mainloop()


login = Tk()
login.title('Авторизация')
login.geometry('300x250')
login.resizable(width=False, height=False)

log_label = Label(login, text = 'Авторизация', font = 'Arial 15')
log_label.pack()

username_label = Label(login, text='Логин', font = 'Arial 13')
username_label.pack()

username_entry = Entry(login, font = 'Arial 12')
username_entry.pack()

password_label = Label(login, text='Пароль', font = 'Arial 13')
password_label.pack()

password_entry = Entry(login, fg='black', font = 'Arial 12')
password_entry.pack()

login_btn=Button(login, text = 'Войти', command = login_user)
login_btn.pack( padx=10, pady=20)

login.mainloop()
