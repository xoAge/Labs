#Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
#В программе должны быть реализованы минимум один класс, три атрибута, два метода

#Задание. В музее 10 залов.  У каждого зала есть номер, рейтинг, стоимость.
#Отобрать похождение по 3 залам с допустимым минимальным уровнем рейтинга и со стоимостью не больше указанного бюджета.


try:
    class muzei:
        def __init__(self, zali):
            self.zali = zali           #ссылаемся на список залов
        def find_best_trio(self, min_reiting, max_budget): # Перебираем методом все возможные комбинации похождения по трем залам
            best_trio = None
            max_sum_reiting = 0
            for i in range(len(self.zali)):
                for j in range(i + 1, len(self.zali)):
                    for k in range(j + 1, len(self.zali)):              # Проверяем, что все выбранные залы удовлетворяют условиям
                        trio = [self.zali[i], self.zali[j], self.zali[k]]
                        if all(zal.reiting >= min_reiting and zal.stoimost <= max_budget for zal in trio):
                            sum_reiting = sum(zal.reiting for zal in trio)
                            if sum(zal.stoimost for zal in trio) <= max_budget and sum_reiting >= min_reiting:
                                if sum_reiting > max_sum_reiting or (sum_reiting == max_sum_reiting and sum(zal.stoimost for zal in trio) < min_stoimost):
                                    best_trio = trio
                                    max_sum_reiting = sum_reiting
                                    min_stoimost = sum(zal.stoimost for zal in trio)
            return best_trio                                    #возвращаем в конце лучший вариант
    class zal:
        def __init__(self, nomer, reiting, stoimost):
            self.nomer = nomer
            self.reiting = reiting
            self.stoimost = stoimost
    zali = [zal("1", 4, 200), zal("2", 5, 800),
                    zal("3", 3, 100), zal("4", 3, 100), zal("5", 2, 50),
                    zal("6", 4, 200), zal("7", 5, 800), zal("8", 5, 800),
                   zal("9", 4, 200), zal("10", 2, 50)]
    muzei = muzei(zali) # Создаем объект класса музея и передаем список залов
    min_reiting = int(input('\nВведите минимальный рейтинг зала (от 2 до 5):'
                       '\n рейтинг 2 - 50 рублей''\n рейтинг 3 - 100 рублей''\n рейтинг 4 - 200 рублей''\n рейтинг 5 - 800 рублей\n Введите рейтинг: '))
    while min_reiting < 2 or min_reiting > 5:
        min_reiting = int(input('\nВведите натуральное число больше 2, но меньше 5:\n'))
    max_budget = int(input('\nВведите максимальный бюджет стоимости залов (начиная от 200 рублей): '))
    while max_budget < 200:
        max_budget = int(input('\nВведите натуральное число больше 200:\n'))
    best_trio = muzei.find_best_trio(min_reiting, max_budget)
    if best_trio:
        print("Лучшие 3 зала")
        for zal in best_trio:
            print(f"зал: {zal.nomer}, рейтинг: {zal.reiting}, стоимость: {zal.stoimost}")
        final_stoimost = sum(zal.stoimost for zal in best_trio)
        final_reiting = sum(zal.reiting for zal in best_trio)
        print("\nобщая стоимость:", final_stoimost, ", общий рейтинг:", final_reiting)
    else:
        print("Нет подходящих залов, удовлетворяющих условиям.")
except ValueError:
    print('\nПерезапустите программу и введите натуральное число.')
