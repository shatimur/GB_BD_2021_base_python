# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.

from itertools import count
from itertools import cycle
from sys import argv

name, num1, user_list = argv

# первый итератор
num1 = int(num1)
for i in count(num1):
    if i > num1 + 20:
        break
    else:
        print(i)

# второй итератор - честно сказать, не понял условие задачи (), наугад вот так:
count = 0
for item in cycle(user_list):
    if count > 3: # почему-то срабатывает всего один раз, а не сколько указано
        break
    print(item)
    count += 1