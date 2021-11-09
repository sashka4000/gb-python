# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_set = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_set.add(el)
    else:
        unique_set.discard(el)
    tmp.add(el)

unique_lst = [el for el in src if el in unique_set]
print(unique_lst)
