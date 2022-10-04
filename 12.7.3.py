per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму: "))

deposit = [round(money/100*per_cent['ТКБ']), round(money/100*per_cent['СКБ']), round(money/100*per_cent['ВТБ']),
           round(money/100*per_cent['СБЕР'])]
# для значений более 300

"""deposit = [round((money/100*per_cent['ТКБ']), 3), round((money/100*per_cent['СКБ']), 3),
 round((money/100*per_cent['ВТБ']), 3), round((money/100*per_cent['СБЕР']), 3) ]
Для значений до 300"""

print(deposit)

print("Максимальная сумма, которую вы можете заработать —", max(deposit))
