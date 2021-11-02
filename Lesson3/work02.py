#2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.

def num_translate_adv(value):
    digit_names = {
       'one': 'один',
       'two': 'два',
       'three': 'три',
       'four': 'четыре',
       'five': 'пять'
    }
    if value.capitalize() == value:
        return digit_names.setdefault(value.lower(), 'None').capitalize()
    else:
        return digit_names.get(value.lower())


print(num_translate_adv('Five'))
print(num_translate_adv('five'))
print(num_translate_adv('six'))