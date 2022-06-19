amount = (int(input('Сколько билетов необходимо Вам? \n')))
sum = 0
count = 1
age = (int(input('Возраст каков посетителя?\n')))
while amount > count:
    count += 1
    if age < 18:
        sum += 0
    elif 18 <= age < 25:
        sum += 990
    elif age >= 25:
        sum += 1390
    age = (int(input('Возраст каков посетителя?\n')))
if amount > 3:
    print('Сумма к оплате со скидкой 10%', sum*0.9 , 'рублей')
else:
    print('Сумма к оплате', sum, 'рублей')