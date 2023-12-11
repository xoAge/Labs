import csv #Инициализация словарей для хранения данных
counter_data = {'Q': {'male': {'count': 0,'fare': 0}, 'female': {'count': 0,'fare': 0}},
                'S': {'male': {'count': 0,'fare': 0}, 'female': {'count': 0,'fare': 0}},
                'C': {'male': {'count': 0,'fare': 0}, 'female': {'count': 0,'fare': 0}},
                '': {'male': {'count': 0,'fare': 0}, 'female': {'count': 0,'fare': 0}}}
with open('titanic.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        embarked = row['Embarked']
        sex = row['Sex']
        fare = float(row['Fare'])
        age = row['Age']
        counter_data[embarked][sex]['count'] += 1
        counter_data[embarked][sex]['fare'] += fare
for embarked, gender_data in counter_data.items():
    for sex, data in gender_data.items():
        if embarked == 'Q':
            if sex == 'male':
                print(f"Порт {embarked}: {sex}  {data['count']}  {data['fare']}")



