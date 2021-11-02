# Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(value):
    digit_names = {
       'one': 'один',
       'two': 'два',
       'three': 'три',
       'four': 'четыре',
       'five': 'пять'
    }
    return digit_names.get(value)


print(num_translate('five'))
print(num_translate('six'))
