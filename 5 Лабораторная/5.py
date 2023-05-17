#Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить (смоделировать) границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и
#графической форме в виде отчета по лабораторной работе.
#F(1) = F(2) = 1, F(n) = F(n - 1) - (n + 2)!, при n > 2

import math
import matplotlib.pyplot as plt
import timeit
def iter(n):              # итеративный подход
    iter = 1
    for i in range(3, n+1):
        iter -= math.factorial(i + 2)
    return iter
def rek(n): #рекурсивный подход
    if n == 1 or n == 2:
        return 1
    else:
        return rek(n - 1) - math.factorial(n + 2)
try:
    n = int(input('\nВведите натуральное число n для функции F(1) = F(2) = 1, F(n) = F(n - 1) - (n + 2)!:'))
    while n <= 2: #ошибка
        n = int(input('\nВы ввели не правильное число. Введите число n > 2:\n'))
    step = int(input('Введите шаг изменения числа для построения таблицы:'))
    while step < 1:
        step= int(input('\nШаг должен быть натуральным числом, введите натуральное число:\n'))

    rek_times = []              # создание списков для построения таблицы
    rek_values = []
    iter_times = []
    iter_values = []
    n_values = list(range(1, n + 1, step))

    for n in n_values:          # заполнение списков данными
        start = timeit.default_timer()
        rek_values.append(rek(n))
        end = timeit.default_timer()
        rek_times.append(end - start)
        start = timeit.default_timer()
        iter_values.append(iter(n))
        end = timeit.default_timer()
        iter_times.append(end - start)
    table = []                                      # заполнение таблицы
    for i, n in enumerate(n_values):
        table.append([n, rek_times[i], iter_times[i], rek_values[i], iter_values[i]])
    print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)','Значение рекурсии', 'Значение итерации'))  # вывод таблицы
    print('-' * 110)
    for data in table:
        print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format(data[0], data[1], data[2], data[3], data[4]))
    plt.plot(n_values, rek_times, label ='Рекурсия')        # вывод графиков
    plt.plot(n_values, iter_times, label ='Итерация')
    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение рекурсивного и итерационного подхода')
    plt.legend()
    plt.show()
    print("\nРабота программы завершена.\n")
except ValueError:
    print('\nПерезапустите программу и введите натуральное число')
except RecursionError:
    print('\nВы превысили глубину рекурсии. Перезапустите программу и введите меньшее число')
