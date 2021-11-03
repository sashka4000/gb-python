# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
import random


def get_jokes(num, flag):
    """ Function description hear """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if (flag == 1) and (num > len(nouns)):
        print(f'Param num must be less {len(nouns)}')
        return
    if flag == 1:
        w1 = random.sample(nouns, k=num)
        w2 = random.sample(adverbs, k=num)
        w3 = random.sample(adjectives, k=num)
    else:
        w1 = random.choices(nouns, k=num)
        w2 = random.choices(adverbs, k=num)
        w3 = random.choices(adjectives, k=num)
    l = list([])
    for i in range(num):
        l.append(f'{w1[i]} {w2[i]}  {w3[i]}')
    return l

print(get_jokes(5,1))
