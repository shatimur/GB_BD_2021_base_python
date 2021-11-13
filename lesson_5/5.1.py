# Создать программно файл в текстовом формате, записатьв него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

create_file = open('pr_file.txt', 'w')
line = input('Введите текст \n')
while line:
    create_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

create_file.close()
create_file = open('pr_file.txt', 'r')
content = create_file.readlines()
print(content)
create_file.close()
