# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(word=input('Введите слово маленькими латинскими буквами: ')):
    if word.islower():
        for el in word:
            if not 96 < ord(el) < 123:
                return 'Вы неправильно ввели слово'
    else:
        return 'Вы неправильно ввели слово'
    return word.capitalize()


print(int_func())
