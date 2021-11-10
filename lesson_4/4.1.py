from sys import argv
name, p1, p2, p3 = argv
try:
    salary = (int(p1)*int(p2)) + int(p3)
    print(salary)
except ValueError:
    print('Вы ввели неверные значения!')
 # поймать исключение при неверном количестве аргументов у меня не получилось, хотя ошибка тоже ValueErrorr
