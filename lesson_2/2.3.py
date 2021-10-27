month = int(input('Введите номер месяца (от 1 до 12): '))

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    season = 'Зима'
if month in spring:
    season = 'Весна'
if month in summer:
    season = 'Лето'
if month in autumn:
    season = 'Осень'

# Решение через dict

# year = {
#     1: 'янв',
#     2: 'фев',
#     3: 'мар',
#     4: 'апр',
#     5: 'май',
#     6: 'июн',
#     7: 'июл',
#     8: 'авг',
#     9: 'сен',
#     10: 'окт',
#     11: 'ноя',
#     12: 'дек',
# }
# print(f'Вы ввели месяц: {year[month]}', это {season}')

# Решение через list

year = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
month -= 1

print(f'Вы ввели месяц: {year[month]}, это {season}')


