#2 часть – усложнить написанную программу, введя по своему усмотрению в условие
#минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.

#У каждого зала есть номер, рейтинг, стоимость, экскурсия проходит только по четным залам.
#Сформировать вариант прохода экскурсии по 2 залам с минимальной стоимостью, соответственно с наименьшим рейтингом.

import random
from random import randint

K = int(input("Введите количество залов, от 3 до 50: "))
while K < 3 or K > 50:
    K = int(input("Введите количество залов, от 3 до 50: "))
ekskursia = []
min_reiting = min_cost = 10000
zal_1 = zal_2 = 0
nomer = []
while len(nomer) < K:
    nome = randint(1, 101)
    if nome not in nomer and nome % 2 == 0:
        nomer.append(nome)
        print("\nНомер зала: |",nome,"|")
        reiting = random.randint(1, 10)
        print("Рейтинг зала: ", reiting)
        cost = random.randint(100, 200)
        print("Стоимость зала: ", cost)
        ekskursia.append((nome, reiting, cost))
for i in range(K):
    for j in range(K):
        if i != j:
            cost_sum = ekskursia[i][2] + ekskursia[j][2]
            reiting_sum = ekskursia[i][1] + ekskursia[j][1]
            if reiting_sum < min_reiting and cost_sum < min_cost:
                min_cost = cost_sum
                max_reiting = reiting_sum
                zal_1 = ekskursia[i][0]
                zal_2 = ekskursia[j][0]
print("\nЭкскурсия по", zal_1, "и", zal_2, "залу ")
