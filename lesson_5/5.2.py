# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

create_file = open('file.txt', 'r')
content = create_file.read()
print(f'Содержимое файла: \n {content}')
create_file = open('file.txt', 'r')
content = create_file.readlines()
print(f'Количество строк в файле - {len(content)}')
create_file = open('file.txt', 'r')
content = create_file.readlines()
for i in range(len(content)):
    print(f'Символов  в {i + 1} - ой строки {len(content[i])}')
create_file = open('file.txt', 'r')
content = create_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
create_file.close()