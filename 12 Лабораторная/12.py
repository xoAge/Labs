#Вычислить сумму знакопеременного ряда (|х*n!|)/n!, где х-матрица ранга к (к и матрица задаются случайным образом),
#n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
#У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.
import numpy as np
def result_sum(random_matrix, t):
    n,fact,current_sum = 1,1,0
    matrix = random_matrix.copy()
    while True:
        fact = fact * n
        chislitel = np.linalg.det(matrix * fact)
        summa = chislitel / fact
        current_sum += -abs(summa) if n == 1 else summa * (-1) ** n
        n += 1
        if summa < t:
            break
    return current_sum
try:
    t = int(input("Введите желаемую точность вычислений (не равную нулю): "))
    while t > 50 or t < 1:
        t = int(input("Введите число t, большее или равное 1 и меньшее или равное 50:\n"))
    k = np.random.randint(2,10)
    np.set_printoptions(linewidth=200)
    random_matrix = np.random.uniform(-1, 1, (k, k))
    print("Сгенерирована матрица:\n", random_matrix)
    result = result_sum(random_matrix, t)
    prec_format = "{:." + str(int(t)) + "f}"
    print(f"Сумма знакопеременного ряда: {prec_format.format(result)}")
except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")
