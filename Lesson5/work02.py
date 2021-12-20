# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

max_value = 3
odd_to_15 = (_ for _ in range(1, max_value+1, 2))
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)