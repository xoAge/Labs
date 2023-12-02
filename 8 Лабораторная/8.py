#Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации
# (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую
# библиотеку питона.  Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
# В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.
from tkinter import *
from tkinter import messagebox

class muzei:
    def __init__(self, zali):
        self.zali = zali           #ссылаемся на список залов

        self.raschet = Tk()
        self.raschet.title('Похождение по 3 залам')
        self.raschet.geometry('450x370')
        self.raschet.resizable(False, False)

        self.zadacha_label = Label(self.raschet, width=45, text='Отберите похождение по 3 залам\n с допустимым минимальным уровнем\n рейтинга и со стоимостью не больше\n указанного бюджета', font='Arial 15')
        self.zadacha_label.pack()

        self.min_reiting_label = Label(self.raschet, text='Введите минимальный рейтинг\n зала (от 2 до 5):', font='Arial 13')
        self.min_reiting_label.pack()

        self.min_reiting_entry = Entry(self.raschet, font='Arial 12')
        self.min_reiting_entry.pack()

        self.max_budget_label = Label(self.raschet, text='Введите максимальный бюджет \nдля похождения по 3 залам \n(начиная от 200 рублей):', font='Arial 13')
        self.max_budget_label.pack()

        self.max_budget_entry = Entry(self.raschet, font='Arial 12')
        self.max_budget_entry.pack()

        self.raschet_btn = Button(self.raschet, text='Найти', command=self.find_best_trio)
        self.raschet_btn.pack(padx=10, pady=20)
        self.raschet.mainloop()

    def vihod(self):
        self.resultat.destroy()

    def find_best_trio(self): # Перебираем методом все возможные комбинации похождения по трем залам
        try:
            min_reiting = int(self.min_reiting_entry.get())
            if min_reiting < 2 or min_reiting > 5:
                messagebox.showerror('Некорректное число', 'Введите натуральное число больше 2, но меньше 5')
                return
            max_budget = int(self.max_budget_entry.get())
            if max_budget < 200:
                messagebox.showerror('Некорректное число', 'Введите натуральное число больше 200')
                return
            best_trio = None
            max_sum_reiting = 0

            for i in range(len(self.zali)):
                for j in range(i + 1, len(self.zali)):
                    for k in range(j + 1,len(self.zali)):  # Проверяем, что все выбранные залы удовлетворяют условиям
                        trio = [self.zali[i], self.zali[j], self.zali[k]]
                        if all(zal.reiting >= min_reiting and zal.stoimost <= max_budget for zal in trio):
                            sum_reiting = sum(zal.reiting for zal in trio)
                            if sum(zal.stoimost for zal in trio) <= max_budget and sum_reiting >= min_reiting:
                                if sum_reiting > max_sum_reiting or (sum_reiting == max_sum_reiting and sum(
                                        zal.stoimost for zal in trio) < min_stoimost):
                                    best_trio = trio
                                    max_sum_reiting = sum_reiting
                                    min_stoimost = sum(zal.stoimost for zal in trio)
            if best_trio:
                self.resultat = Tk()  # открытие окна с результатом
                self.raschet.destroy()
                self.resultat.title('Полученный результат')
                self.resultat.geometry('300x250')
                self.resultat.resizable(False, False)

                self.resultat_label = Label(self.resultat, width=55, height=10)
                self.resultat_label.pack()

                self.resultat_btn = Button(self.resultat, text='Закрыть', command=self.vihod)
                self.resultat_btn.pack()
                resultat_text = " Лучшее похождение по 3 залам\n"
                for zal in best_trio:
                    resultat_text += f"зал: {zal.nomer}, рейтинг: {zal.reiting}, стоимость: {zal.stoimost}\n"
                final_stoimost = sum(zal.stoimost for zal in best_trio)
                final_reiting = sum(zal.reiting for zal in best_trio)
                resultat_text += f"\nобщая стоимость: {final_stoimost}\n общий рейтинг: {final_reiting}"
                self.resultat_label.config(text=resultat_text, font='Arial 13')
            else:
                messagebox.showerror("Результат", "Нет подходящих трех залов для похождения.")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите натуральные числа!")

class zal:
    def __init__(self, nomer, reiting, stoimost):
        self.nomer = nomer
        self.reiting = reiting
        self.stoimost = stoimost
zali = [zal("1", 4, 200), zal("2", 5, 800),
                    zal("3", 3, 100), zal("4", 3, 100), zal("5", 2, 50),
                    zal("6", 4, 200), zal("7", 5, 800), zal("8", 5, 800),
                   zal("9", 4, 200), zal("10", 2, 50)]
muzei = muzei(zali)








