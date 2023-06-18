# Здесь будет основная функция работы программы
# приветствие
# спросить на какой платформе будем искать
# слово - ключ
import json
from pprint import pprint

from utils.hhru_class import HHJobPlatform
from utils.sj_class import SuperJobPlatform
from utils.vacancy_class import Vacancy


# какое кол-во ваканций

# Город

# фильтр по опыту

# фильтр по зарплате, показать где есть зп а где нет


# всё закинуть в цикл, с возможность вернуться в начало по слову start (например)
# озможность скачать файл в эксель


# вернуться на шаг назад
def main():
    print('Привет. давай поищем тебе работу')

    while True:
        first_question = input('Где будем искать?\n'
                               '1 - ХХ ру\n'
                               '2 - супер джаб\n')
        keyword = input('По какому запросу ищем? (например: Негр для сбора урожая)\n')
        count_vacancy = input('Сколько ваканcий тебе показать?\n')

        if first_question == '1':
            city = input('В каком городе ищем?\n')
            keyword_end = keyword + city
            get_list = HHJobPlatform(keyword_end, count_vacancy)
            list_job = get_list.get_jobs()
            print(f'Нашлось {len(list_job)} вакансий, вывести на экран?')
            Vacancy.class_vacancy_ex(list_job)
            for item in Vacancy.all_class_vacancy:
                print(str(item))
            print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически'
                  '\nДавай поищем что то другое?')

        elif first_question == '2':
            get_list = SuperJobPlatform(keyword, count_vacancy)
            list_job = get_list.get_jobs()
            print(f'Нашлось {len(list_job)} вакансий, вывести на экран?')
            Vacancy.class_vacancy_ex(list_job)
            for item in Vacancy.all_class_vacancy:
                print(str(item))

            answer_baby = input('Хочешь выведу только наименование вакансии, зарплату и ссылку? да\нет\n')
            if answer_baby.lower() == 'да' or answer_baby.lower() == 'lf':
                with open('vacancy_list_sjru.json', 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    for i in data:
                        print('Вакансия:', i['title'])
                        print('Ссылка:', i['link'])
                        print('Зарплата: от', i['salary_min'], ' до', i['salary_max'], '\n')
                # print(Vacancy.all_class_vacancy)
                #for item in Vacancy.all_class_vacancy:
                    #print(item)


            else:
                continue



            print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически'
                  '\nДавай поищем что то другое?')


        else:
            pass


if __name__ == '__main__':
    main()
