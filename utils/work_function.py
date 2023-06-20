import json

from utils.hhru_class import HHJobPlatform
from utils.sj_class import SuperJobPlatform
from utils.vacancy_class import Vacancy


def hh_function(keyword, count_vacancy):
    get_list = HHJobPlatform(keyword, count_vacancy)
    list_job = get_list.get_jobs()
    print(f'Нашлось {len(list_job)} вакансий.')

    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:
        print(str(item))
    print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')


def sj_function(keyword, count_vacancy):
    get_list = SuperJobPlatform(keyword, count_vacancy)
    list_job = get_list.get_jobs()
    print(f'Нашлось {len(list_job)} вакансий!')
    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:
        print(str(item))
    print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')
    answer_baby = input('Хочешь выведу только наименование вакансии, зарплату и ссылку? да/нет\n')
    if answer_baby.lower() == 'да' or answer_baby.lower() == 'lf':
        with open('vacancy_list_sjru.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                print('Вакансия:', i['title'])
                print('Ссылка:', i['link'])
                print('Зарплата: от', i['salary_min'], ' до', i['salary_max'], '\n')
                print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')
