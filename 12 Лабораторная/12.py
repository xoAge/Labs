#Вычислить сумму знакопеременного ряда (|х*n!|)/n!, где х-матрица ранга к (к и матрица задаются случайным образом),
#n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
#У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.
import numpy as np
from decimal import Decimal, getcontext
def count_summ(matrix, t):
    t = 1 / (10 ** t)
    result_matrix = matrix.copy()
    i, fact_n, summa, result_num = 1, 1, 1, 0
    while abs(summa) > t:           # Цикл для вычисления суммы ряда
        fact_n *= i
        result_matrix = np.dot(np.dot(result_matrix, matrix), matrix)
        matrix_det = Decimal(np.linalg.det(result_matrix))
        summa = (matrix_det*Decimal(fact_n)) / Decimal(fact_n)
        result_num += -abs(summa) if i == 1 else summa * (-1) ** i
        i += 1
    print(f"Количество итераций: {i - 1}")
    return result_num
try:        # Ввод точности t
    t = abs(int(input("Введите точность, число t (количество знаков после запятой): ")))
    rank = np.random.randint(2, 10) # Генерация случайной матрицы
    matrix = np.random.uniform(-1,1, size = (rank, rank))
    getcontext().prec = t + 100
    np.set_printoptions(linewidth=200)
    Rang = np.linalg.matrix_rank(matrix)  # Вычисление ранга матрицы x.
    print(f"Сгенерированная матрица:\n {matrix} \nРанг матрицы: {Rang}")
    summa_tot = count_summ(matrix, t)
    print(f'Заданная точность: {t}')
    print(f"Сумма ряда: {summa_tot}")
except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")
