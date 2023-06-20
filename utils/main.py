from utils.work_function import hh_function, sj_function


def main():
    print('Привет. давай поищем тебе работу')

    while True:
        first_question = input('Где будем искать?\n'
                               '1 - ХХ ру\n'
                               '2 - супер джаб\n')

        while True:
            keyword = input('По какому запросу ищем? (например: python)\n')
            if len(keyword.lower()) <= 2:
                print("Что то совсем коротко?")
                continue
            else:
                break

        while True:
            count_vacancy = input('Сколько ваканcий тебе показать?\n')
            if int(count_vacancy) <= 1:
                print("Что то мало?")
                continue
            else:
                break

        while True:
            city = input('В каком городе ищем?\n')
            if len(city.lower()) <= 2:
                print("Что то совсем коротко?")
                continue
            else:
                break

        keyword_end = keyword + ' ' + city

        if first_question == '1':
            hh_function(keyword_end, count_vacancy)

        elif first_question == '2':
            sj_function(keyword_end, count_vacancy)

        while True:
            answer_end = input('Давай поищем что то другое? Да/нет\n')
            if answer_end.lower() == 'да' or answer_end.lower() == 'lf':
                break
            elif answer_end.lower() == 'нет' or answer_end.lower() == 'ytn':
                print('Ок. Пока!')
                exit()

            else:
                print('Ой, не понимаю.')
                continue


if __name__ == '__main__':
    main()
