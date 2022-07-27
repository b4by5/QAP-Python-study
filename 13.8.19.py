guest_num = int(input('Введите количество билетов: '))
L = []
summa = 0
for n in range(guest_num):
    L.append(int(input(f'Введите возраст посетителя {n+1}: ')))
for age in L:
    if 18 <= age < 25:
        summa += 990
    elif age >= 25:
        summa += 1390
if guest_num > 3:
    summa *= 0.9
print(f'Стоимость билетов: {summa} руб.')
