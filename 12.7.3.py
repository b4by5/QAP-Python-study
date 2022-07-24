per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#print(per_cent.get())
money = float(input('Введите сумму вклада: '))
deposit = [int(money * per_cent['ТКБ']/100),
           int(money * per_cent['СКБ']/100),
           int(money * per_cent['ВТБ']/100),
           int(money * per_cent['СБЕР']/100)]
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))
