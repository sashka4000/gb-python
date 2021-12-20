# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем должность) с сайтов HH и/или Superjob. Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия.

from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

#https://hh.ru/search/vacancy?text=VACANCY

vacancy_name = input('Название вакансии: ')

main_url = 'https://hh.ru'
params = {'text': vacancy_name}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

response = requests.get(main_url+'/search/vacancy/', params=params, headers=headers)

if response.ok:
    dom = bs(response.text, 'html.parser')
    blocks = dom.find_all('div', {'class': ['vacancy-serp-item', 'vacancy-serp-item_premium']})
    vac_list = []
    for _vac in blocks:
        vacancy = {}
        info = _vac.find('a', {'class': 'bloko-link'})
        vacancy['page'] = main_url
        vacancy['name'] = info.text
        vacancy['href'] = info.attrs['href']
        vacancy['currency'] = None
        vacancy['min'] = None
        vacancy['max'] = None
        salary = _vac.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
        try:
            vacancy['currency'] = salary.contents[len(salary.contents)-1]
            if salary.contents[0].strip() == 'от':
                vacancy['min'] = int(salary.contents[2].replace('\u202f', ''))
            elif salary.contents[0].strip() == 'до':
                vacancy['max'] = int(salary.contents[2].replace('\u202f', ''))
            else:
                _ = salary.contents[0].replace('\u202f', '').split()
                vacancy['min'] = int(_[0])
                vacancy['max'] = int(_[2])

        except:
            pass
        vac_list.append(vacancy)
pprint(vac_list)