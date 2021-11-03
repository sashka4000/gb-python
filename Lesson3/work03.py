# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имён,
# а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*names):
    name_dict = dict()
    for _item in names:
        if not name_dict.get(_item[0]):
            name_dict[_item[0]] = list([_item])
        else:
            name_dict[_item[0]].append(_item)
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
