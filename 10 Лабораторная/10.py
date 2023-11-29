#Написать крестики-нолики для игры с компьютером
import tkinter as tk
from tkinter import messagebox
import os
import random

class TicTacToeGame:
    def __init__(self):
        self.current_player = "X"
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.resizable(width=False, height=False)
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.window, text="", width=10, height=5,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)
    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Победитель", f"Игрок {self.current_player} победил!")
                self.reset()
            elif self.check_draw():
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset()
            else:
                self.switch_player()
                self.make_computer_move()
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player or self.board[0][i] == \
                    self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or self.board[0][2] == self.board[1][1] == \
                self.board[2][0] == player:
            return True
    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    def make_computer_move(self):
        best_move = self.get_best_move()
        if best_move:
            row, col = best_move
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O")
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Победитель", f"Игрок {self.current_player} победил!")
                self.reset()
            elif self.check_draw():
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset()
            else:
                self.switch_player()
    def get_best_move(self):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    available_moves.append((row, col))
        for move in available_moves:
            row, col = move
            self.board[row][col] = "O"
            if self.check_winner("O"):
                self.board[row][col] = ""
                return row, col
            self.board[row][col] = ""
        for move in available_moves:
            row, col = move
            self.board[row][col] = "X"
            if self.check_winner("X"):
                self.board[row][col] = ""
                return row, col
            self.board[row][col] = ""
        return random.choice(available_moves) if available_moves else None
    def reset(self):
        self.current_player = "X"
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        for row in self.buttons:
            for button in row:
                button.config(text="")
class RegistrationWindow:
    def __init__(self, filename):
        self.filename = filename
        self.window = tk.Tk()
        self.window.resizable(width=False,height=False)
        self.window.geometry('500x200')
        self.window.title("Регистрация")
        self.username_label = tk.Label(self.window, text="Логин:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()
        self.password_label = tk.Label(self.window, text="Пароль:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()
        self.register_button = tk.Button(self.window, text="Зарегистрироваться/Войти", command=self.register)
        self.register_button.pack( padx=10, pady=20)
    def shifr(self, message1):
        alfavit_EU = ''
        smeshenie = 1
        itog = ''
        message = message1.upper()
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
        print(itog)
        return itog
    def register(self):
        username = self.username_entry.get()
        password1 = self.password_entry.get()
        password = self.shifr(password1)
        if not username or not password:
            messagebox.showerror("Ошибка", "Введите логин и пароль")
            return
        with open(self.filename) as f:
            lines = f.readlines()
            for line in lines:
                saved_username, saved_password = line.strip().split(",")
                if username == saved_username and password == saved_password:
                    messagebox.showinfo("Успех", "Авторизация прошла успешно")
                    self.window.destroy()
                    game = TicTacToeGame()
                    tk.mainloop()
                    return
                elif username == saved_username:
                    messagebox.showinfo("Ошибка", "Пользователь с таким логином уже существует")
                    return
        with open(self.filename, "a") as f:
            f.write(f"{username},{password}\n")
            messagebox.showinfo("Успех", "Добро пожаловать\nРегистрация прошла успешно")
            self.window.destroy()
            game = TicTacToeGame()
            tk.mainloop()
            return
    def run(self):
        self.window.mainloop()
if os.path.isfile("users.txt"):
    registration_window = RegistrationWindow("users.txt")
else:
    myfile = open("users.txt", "x")
    registration_window = RegistrationWindow("users.txt")
registration_window.run()
