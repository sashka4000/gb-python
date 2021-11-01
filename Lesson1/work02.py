# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел
# из этого списка, сумма цифр которых делится нацело на 7.
#* Решить задачу под пунктом b, не создавая новый список.

pow3_list = []
for i in range (1, 1001, 2):
    pow3_list.append(i ** 3)
for step in [1, 2]:
    add_value = 0
    if step == 2:
        add_value = 17
    total_sum = 0
    for i in range (len(pow3_list)):
        pow3_list[i] += add_value
        local_sum = 0
        item = pow3_list[i]
        while item != 0:
            local_sum += item % 10
            item //= 10
        if local_sum % 7  == 0:
            total_sum += pow3_list[i]
    print ('step =', step, ' total_sum = ', total_sum)
