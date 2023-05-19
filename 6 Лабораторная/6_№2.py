#2 часть – усложнить написанную программу, введя по своему усмотрению в условие
#минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.

#У каждого зала есть номер, рейтинг, стоимость, экскурсия проходит только по четным залам.
#Сформировать вариант прохода экскурсии по 2 залам с минимальной стоимостью, соотвественно с минимальным рейтингом.
K = int(input("Введите количество залов, от 3: "))
while K < 3:
    K = int(input("Введите количество залов, от 3: "))
ekskursia = []
for i in range(1, K + 1):
    nomer = int(input("\nВведите номер зала, экскурсии только по четным залам: "))
    while nomer % 2 != 0 or nomer == 0:
        nomer = int(input("Введите четный номер зала: "))
    reiting = int(input("Введите рейтинг зала: "))
    cost = int(input("Введите стоимость посещения этого зала, посещение не может стоить больше 200: "))
    while cost > 200:
        cost = int(input("Посещение не может стоить больше 200: "))
    ekskursia.append((nomer, reiting, cost))
max_reiting = 1000
zal_1 = zal_2 = 0
max_cost = 1000
for i in range(K):
    for j in range(K):
        if i != j:
            cost_sum = ekskursia[i][2] + ekskursia[j][2]
            reiting_sum = ekskursia[i][1] + ekskursia[j][1]
            if reiting_sum < max_reiting and cost_sum < max_cost:
                max_cost = cost_sum
                max_reiting = reiting_sum
                zal_1 = ekskursia[i][0]
                zal_2 = ekskursia[j][0]
print("\nЭкскурсия по", zal_1, "и", zal_2, "залу ")
