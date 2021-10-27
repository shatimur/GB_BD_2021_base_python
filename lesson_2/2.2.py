# my_list = [11, 12, 13, 14, 15]
my_list = (input("Введите элементы списка через пробел: ")).split()
print(f'Ваш список: {my_list}')

if len(my_list) % 2: #  определяем четность длины списка и соответственно верхнюю границу цикла for
    a = len(my_list)-2
else:
    a = len(my_list)-1

for i in range(0, a, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    
print(f'Ваш список после преобразования  {my_list}')
