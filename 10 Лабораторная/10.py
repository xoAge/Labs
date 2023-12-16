#Крестики-нолики для игры с компьютером
import tkinter as tk
from tkinter import messagebox
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
game = TicTacToeGame()
tk.mainloop()
