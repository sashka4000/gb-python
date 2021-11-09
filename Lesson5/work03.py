# Есть два списка:
#  Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
gen_klass = ((tutors[t], klasses[t]) for t in range(len(tutors)))
print(type(gen_klass), *gen_klass)