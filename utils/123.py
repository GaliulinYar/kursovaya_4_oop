import requests
from bs4 import BeautifulSoup


class Vacancy:
    def __init__(self, title, url, salary, requirements):
        self.title = title
        self.url = url
        self.salary = salary
        self.requirements = requirements

    def __str__(self):
        return f"Название вакансии: {self.title}\nURL: {self.url}\nЗарплата: {self.salary}\nТребования: {self.requirements}\n"

class HhVacancyParser:
    def __init__(self, search_query):
        self.search_query = search_query
        self.base_url = f"https://api.hh.ru/vacancies"

    def parse_vacancies(self):
        # Вставьте свой API ключ HH.ru в заголовок запроса
        headers = {
            "User-Agent": "Your User Agent",
            "Authorization": "Bearer Your API Key"
        }

        params = {
            "text": self.search_query
        }

        response = requests.get(self.base_url, headers=headers, params=params)
        response.raise_for_status()

        vacancies_data = response.json()

        vacancies = []
        for item in vacancies_data['items']:
            title = item['name']
            url = item['alternate_url']
            salary = item['salary']['from'] if item['salary'] and item['salary']['from'] else 'Зарплата не указана'
            requirements = item['snippet']['requirement']

            vacancy = Vacancy(title, url, salary, requirements)
            vacancies.append(vacancy)

        return vacancies

# Пример использования
search_query = "python"
parser = HhVacancyParser(search_query)
vacancies = parser.parse_vacancies()

for vacancy in vacancies:
    print(vacancy)