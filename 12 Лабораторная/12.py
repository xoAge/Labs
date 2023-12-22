#Вычислить сумму знакопеременного ряда (|х*n!|)/n!, где х-матрица ранга к (к и матрица задаются случайным образом),
#n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
#У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.
import numpy as np
from decimal import Decimal, getcontext
def count_summ(matrix, t):
    t = 1 / (10 ** t)
    result_matrix = matrix.copy()
    n, fact_n, summa, result_sum = 1, 1, 1, 0
    while abs(summa) > t:           # Цикл для вычисления суммы ряда
        fact_n *= n
        result_matrix = np.dot(np.dot(result_matrix, matrix), matrix)
        matrix_det = Decimal(np.linalg.det(result_matrix))
        summa = (matrix_det*Decimal(fact_n)) / Decimal(fact_n)
        result_sum += -abs(summa) if n == 1 else summa * (-1) ** n
        n += 1
    print(f"Количество итераций: {n - 1}")
    return result_sum
try:        # Ввод точности t
    t = int(input("Введите точность, число t (количество знаков после запятой): "))
    while t > 100 or t < 1:  # Проверка допустимости введенной точности
        t = int(input("Введите число t, большее или равное 1 и меньшее 100:\n"))
    rank = np.random.randint(2, 10) # Генерация случайной матрицы
    matrix = np.random.uniform(-1,1, size = (rank, rank))
    np.set_printoptions(linewidth=200)
    Rang = np.linalg.matrix_rank(matrix)  # Вычисление ранга матрицы x.
    print(f"Сгенерированная матрица:\n {matrix} \nРанг матрицы: {Rang}")
    summa_tot = count_summ(matrix, t)
    rounded_summa = round(summa_tot, t)
    print(f'Заданная точность: {t}')
    print(f"Сумма ряда: {rounded_summa}")
except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")
