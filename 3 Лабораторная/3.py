# С клавиатуры вводится два числа K и N. Квадратная матрица3 А(N,N),
# состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
# случайным образом целыми числами в интервале [-10,10].
# Для тестирования использовать не случайное заполнение, а целенаправленное.
# Формируется матрица F следующим образом: если в С количество нулей по периметру области 2 больше,
# чем произведение чисел по периметру области 4, то поменять в Е симметрично области 1 и 4 местами,
# иначе С и В поменять местами несимметрично. При этом матрица А не меняется.
# После чего вычисляется выражение: ((К*A T)*(F+А)-K* F T .
# Выводятся по мере формирования А, F и все матричные операции последовательно.
# порядок                        1
# E  B                        4     2
# D  C                           3

import random
def print_matr(matr):                                           # вывод матрицы
    matr1 = list(map(list, zip(*matr)))
    for i in range(len(matr1)):
        k = len(max(list(map(str, matr1[i])), key=len))
        matr1[i] = [f'{elem:{k}d}' for elem in matr1[i]]
    matr1 = list(map(list, zip(*matr1)))
    for ryad in matr1:
        print(*ryad)
    print()
def paste_matr(matrF, matr, index, ryad_index):
    a = index
    for ryad in matr:
        for element in ryad:
            matrF[ryad_index][index] = element
            index += 1
        ryad_index += 1
        index = a
try:
    k = int(input("Введите число K, являющееся коэффициентом при умножении: "))
    n = int(input("Введите число N, большее или равное 8: "))
    while n < 8:                                                              # ошибка, слишком малый порядок матрицы
        n = int(input("Число не подходит по условию, введите число N, большее или равное 8:\n"))
    print("Матрица А изначальная:")
    matrA = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]   # создаем матрицу размером nxn, заполненную случайными числами
    #matrA = [[i+j*n for i in range(n)] for j in range(n)]                      # задание матрицы для тестирования
    #matrA = [[(0) for i in range(n)] for j in range(n)]                     # задание матрицы для тестирования нулями
    print_matr(matrA)
    print('E   B       1')
    print('D   C    4     2')
    print('            3')
    delit_n = n // 2
    fix = delit_n
    if n % 2 != 0:
        fix += 1
    matrA_p = [[elem for elem in raw] for raw in matrA]               # резервная копия матрицы A для дальнейших операций
    matrA_tr = [[0 for i in range(n)] for j in range(n)]              # заготовка под транспонированную матрицу A
    print("Матрица A транспонированная:")
    for i in range(n):                                                # произведение транспонирования матрицы A
        for j in range(n):
            matrA_tr[i][j] = matrA_p[j][i]
    print_matr(matrA_tr)                                              # вывод транспонированной матрицы A

    print("Матрица F изначально равная матрице A:")                   # создание матрицы F, равной матрице A
    matrF = [[elem for elem in ryad] for ryad in matrA]
    print_matr(matrF)
    E = [[0 for i in range(delit_n)] for j in range(delit_n)]         # формируем подматрицу E
    for i in range(delit_n):
        for j in range(delit_n):
            E[i][j] = matrF[i][j]
    B = [[0 for i in range(delit_n)] for j in range(delit_n)]         # формируем подматрицу B
    for i in range(delit_n):
        for j in range(fix, n):
            B[i][j - (fix)] = matrF[i][j]
    D = [[0 for i in range(delit_n)] for j in range(delit_n)]         # формируем подматрицу D
    for i in range(delit_n, n):
        for j in range(delit_n):
            D[i - (fix)][j] = matrF[i][j]
    C = [[0 for i in range(delit_n)] for j in range(delit_n)]         # формируем подматрицу C
    for i in range(fix, n):
        for j in range(fix, n):
            C[i - (fix)][j - (fix)] = matrF[i][j]
    print("Подматрица C матрицы F:")                                  # Выводим подматрицу С
    print_matr(C)
    print("\nПодматрица E матрицы F:")                                # Выводим подматрицу E
    print_matr(E)
    print("\nПодматрица B матрицы F:")                                # Выводим подматрицу B
    print_matr(B)
    obl2_quant = 0      # количество нулей по области 2 подматрицы C матрицы F
    obl2 = []
    obl4_quant = 0  # количество нулей по области 2 подматрицы C матрицы F
    obl4 = []
    for i in range(delit_n):
        for j in range(delit_n):
            if ((i + j + 1) >= delit_n) and (i <= j) and C[i][j] == 0 :
                obl2_quant += 1
                obl2.append(C[i][j])
    pro = 1
    for i in range(delit_n):
        for j in range(delit_n):
            if (i >= j) and ((i + j + 1) <= fix) :
                obl4_quant += 1
                obl4.append(C[i][j])
                pro *= C[i][j]
    print('Количество нулей по периметру в области 2 => ', obl2_quant, obl2)
    print('Произведение чисел по периметру в области 4 => ', pro, obl4_quant, obl4)
    if obl2_quant > pro:         # проверка условия
        print("Количество 0 в области 2 больше, чем произведение чисел в области 4, \n меняем в E, области 1 и 4 симметрично местами.")
        for j in range(0,delit_n):
            for i in range(0+j,delit_n-j):
                E[i][j], E[j][i] = E[j][i], E[i][j]
    else:
        print('Количество 0 в области 2 не больше, чем произведение чисел в области 4, '
              '\n меняем подматрицы B и C местами несимметрично.\nЕсли порядок матрицы нечетный, центральный элемент не меняется.\n')
        C, B = B, C
    print('\nСозданная по условию матрица F:')
    paste_matr(matrF, B, fix, 0)
    paste_matr(matrF, C, fix, fix)
    paste_matr(matrF, E, 0, 0)
    paste_matr(matrF, D, 0, fix)
    print_matr(matrF)                       # выводим уже сформированную матрицу F из подматриц
    matrF_p = [[elem for elem in row] for row in matrF]
    matrF_tr = [[0 for i in range(n)] for j in range(n)]  # заготовка под транспонированную матрицу F
    print("Матрица F транспонированная:")
    for i in range(n):                          # произведение транспонирования матрицы F
        for j in range(n):
            matrF_tr[i][j] = matrF_p[j][i]
    print_matr(matrF_tr)
    print("Результат умножения (K * Atr) на (F + A):")
    pervoe = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            pervoe[i][j] = matrA_tr[i][j] * k
    print("(K * Atr) =")
    print_matr(pervoe)
    vtoroe = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            vtoroe[i][j] = matrF[i][j] + matrA[i][j]
    print("(F + A) =")
    print_matr(vtoroe)
    tretie = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            tretie[i][j] = pervoe[i][j] * vtoroe[i][j]
    print("(K * Atr) * (F + A) =")
    print_matr(tretie)
    print("Результат умножения Ftr на коэффициент K:")
    chetvertoe = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            chetvertoe[i][j] = k * matrF_tr[i][j]
    print("K * Ftr =")
    print_matr(chetvertoe)
    print("Конечный результат (K * Atr)* (F + A) - K * Ftr =:")
    pyatoe = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            pyatoe[i][j] = tretie[i][j] - chetvertoe[i][j]
    print_matr(pyatoe)
    print("Работа программы завершена.")
except ValueError:  # ошибка на случай введения не числа в качестве порядка или коэффициента
    print("\nВведенный символ не является числом. "
          "Перезапустите программу и введите число.")