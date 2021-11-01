# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

time = int(input('Введите время в секундах >>> '))
k_list = [86400, 3600, 60, 1]
names_list = ['дн', 'час', 'мин', 'сек']
values_list = [0, 0, 0, 0]

for i in range(len(values_list)):
    values_list[i] = time
    for j in range(i):
        values_list[i] = values_list[i] % k_list[j]
    values_list[i] = values_list[i] // k_list[i]
print('duration =', time)
res_str = ''
for i in range(len(values_list)):
    if values_list[i] > 0:
        res_str = res_str + str(values_list[i]) + ' ' + names_list[i] + ' '
print(res_str)
