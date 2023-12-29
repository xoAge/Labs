#Вычислить сумму знакопеременного ряда (|х*n!|)/n!, где х-матрица ранга к (к и матрица задаются случайным образом),
#n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
#У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.
import numpy as np
def result_sum(det_x, t):
    n,fact,current_sum = 1,1,0
    chislitel = det_x * (fact*n)
    while True:
        fact = fact*n 
        summa = chislitel / fact 
        current_sum += -abs(summa) if n == 1 else summa * (-1) ** n
        n += 1
        if summa < t: 
            break
    return current_sum
try:
    t = int(input("Введите желаемую точность вычислений (не равную нулю): "))
    while t > 50 or t < 1:
        t = int(input("Введите число t, большее или равное 1 и меньшее 50:\n"))
    k = np.random.randint(2, 9)
    np.set_printoptions(linewidth=200)
    random_matrix = np.random.uniform(-1, 1, (k, k))
    print("Сгенерирована матрица:\n", random_matrix)
    det_x = np.linalg.det(random_matrix)
    result = result_sum(det_x, t)
    precision_format = "{:." + str(int(t)) + "f}"
    print(f"Сумма знакопеременного ряда: {precision_format.format(result)}")
except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")
