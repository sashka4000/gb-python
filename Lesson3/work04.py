# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.

def thesaurus(*names):
    name_dict = dict()
    for _item in names:
        if not name_dict.get(_item[0]):
            name_dict[_item[0]] = list([_item])
        else:
            name_dict[_item[0]].append(_item)
    return name_dict


def thesaurus_adv(*names):
    name_dict = dict()
    for _item in names:
        firstname, lastname = _item.split(' ')
        if not name_dict.get(lastname[0]):
            name_dict[lastname[0]] = dict(thesaurus(_item))
        else:
            name_dict[lastname[0]].update(thesaurus(_item))
    return name_dict


values_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(values_dict)

for _item in sorted(values_dict):
    print(_item, ':', values_dict[_item])