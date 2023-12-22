#Определить суммарную стоимость билетов мужчин , севших в порту Квинстаун, в возрастном интервале мода +- 15 позиций
import csv
from statistics import mode
with open('titanic.csv', 'r') as file:
    reader = csv.DictReader(file)
    fare_obsh = [] # Создаем списки
    ages = []
    for row in reader: # Читаем данные из файла и заполняем списки
        if row["Embarked"] == "Q" and row["Age"] != "" and row['Sex'] == "male" and row["Fare"] != "":
            age = float(row['Age'])
            ages.append(age)
            fare = float(row['Fare'])
            fare_obsh.append(fare)
    age_mode = mode(ages) #мода и возврастной интервал
    lower_limit = age_mode - 15
    upper_limit = age_mode + 15
    filter_fare_obsh = [stoimost for stoimost, age in zip(fare_obsh, ages) if lower_limit <= age <= upper_limit] # Фильтруем билеты в нужном возрастном интервале
    fare_konechnii = sum(filter_fare_obsh)
    print("Суммарная стоимость билетов:",fare_konechnii)
