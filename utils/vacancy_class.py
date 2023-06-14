
class Vacancy:
    """Класс создающий экземпляры класса вакансий"""
    def __init__(self, title, link, salary_min, salary_max, description):
        self.title = title
        self.link = link
        self.description = description
        self.salary_min = salary_min
        self.salary_max = salary_max


    def __str__(self):
        return f"Заголовок вакансии: {self.title} " \
               f"Ссылка на вакансию: {self.link} " \
               f"Зарплата от {self.salary_min} до {self.salary_max} " \
               f"Описание вакансии: {self.description}"
