# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(word):
    if word.islower():
        for el in word:
            if not 96 < ord(el) < 123:
                return None
    else:
        return None
    return word.capitalize()


def int_func2(words=input('Введите несколь слов маленькими латинскими буквами: ')):
    words = words.split()
    new_lst = []
    for el in words:
        new_lst.append(int_func(el))
    if None in new_lst:
        return 'Вы неправильно ввели слово'
    else:
        return ' '.join(new_lst)


print(int_func2())
