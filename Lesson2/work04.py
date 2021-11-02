# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать из этих имён и вывести на экран фразы вида:
# 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка,
# как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

main_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for _item in main_lst:
    _parts = _item.split(' ')
    print(f'Привет, {_parts[len(_parts)-1].capitalize()}!')