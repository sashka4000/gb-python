#Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield,
def odd_nums(value):
    for _ in range(1, value+1, 2):
        print(_)
        yield _


odd_to_15 = odd_nums(3)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
