amount = (int(input('Сколько билетов необходимо Вам? \n')))
sum = 0
ages = []
ages.append(int(input('Возраст каков посетителя? \n')))
while len(ages) < amount:
    ages.append(int(input('Возраст каков посетителя? \n')))
for i in ages:
    if i < 18:
        sum += 0
    elif 18 <= i < 25:
        sum += 990
    elif i >= 25:
        sum += 1390
if amount > 3:
    print('Сумма к оплате со скидкой 10%', sum*0.9 , 'рублей/ля')
else:
    print('Сумма к оплате', sum, 'рублей/ля')