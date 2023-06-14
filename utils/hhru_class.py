import json
from abc import ABC
import requests
from utils.get_hh_info import AbstractJobPlatform


class HHJobPlatform(AbstractJobPlatform, ABC):

    def __init__(self, keyword):
        self.keyword = keyword
        self.salary_min = None

    def __gt__(self, other):
        return int(self.salary_min) > int(other.salary_min)

    def __ge__(self, other):
        return int(self.salary_min) >= int(other.salary_min)

    def __lt__(self, other):
        return int(self.salary_min) < int(other.salary_min)

    def __le__(self, other):
        return int(self.salary_min) <= int(other.salary_min)

    def __eq__(self, other):
        return int(self.salary_min) == int(other.salary_min)

    def connect(self, params=None):
        # Реализация подключения к API hh.ru

        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.keyword,  # Ключевое слово для поиска ваканчий
                  'area': 1,  # Индекс города для поиска 1(Москва)
                  "per_page": 10  # Кол-во вакансий на странице
                  }
        headers = {
            "User-Agent": "50355527",  # Replace with your User-Agent header
        }

        response = requests.get(url, params=params, headers=headers)

        return response

    def get_jobs(self, **kwargs):
        # Метод создания словаря вакансий
        if self.connect().status_code == 200:
            data = self.connect().json()
            jobs = {}
            for item in data['items']:
                title = item['name']
                link = item['alternate_url']

                if item['salary']:
                    salary_min = item['salary']['from']
                    salary_max = item['salary']['to']

                else:
                    salary_min = None
                    salary_max = None

                description = item['snippet']['requirement'] if item['snippet'] and 'requirement' in item[
                    'snippet'] else None

                jobs = {
                    'title': title,
                    'link': link,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'description': description
                }
                print(jobs)
                self.write_file_vacancy(jobs)
            return jobs

        else:
            print(f"Request failed with status code: {self.connect().status_code}")

    def write_file_vacancy(self, jobs):
        with open('vacancy_list.json', 'a', encoding='utf-8') as json_file:
            json.dump(jobs, json_file, ensure_ascii=False)

