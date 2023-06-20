import json
from abc import ABC

import requests
from utils.abstract_class import AbstractJobPlatform


class SuperJobPlatform(AbstractJobPlatform, ABC):

    def __init__(self, keyword, count_vacancy):
        self.count_vacancy = count_vacancy
        self.keyword = keyword
        self.salary_min = None

    def connect(self):
        # Реализация подключения к API superjob.ru
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': 'v3.r.137618444.385d7dc2eee888ae32ad9fd4abc78ec6b3bf2792.4c3254ad9c1a28cb15b369f8ddae8d4e8b31cc24',
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {"count": self.count_vacancy, "page": None,
                  "keyword": self.keyword, "archive": False, }
        data = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        return data

    def get_jobs(self, **kwargs):
        # Получение вакансий с superjob.ru
        if self.connect().status_code == 200:
            data = self.connect().json()
            list_job = []
            for item in data['objects']:
                title = item['profession']
                link = item['link']

                if item['payment_from']:
                    salary_min = item['payment_from']
                    salary_max = item['payment_to']

                else:
                    salary_min = 'Не указана'
                    salary_max = 'Не указана'

                description = item['candidat']
                id_vacancy = item['id']

                jobs = {
                    'id': id_vacancy,
                    'title': title,
                    'link': link,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'description': description
                }
                list_job.append(jobs)

            self.write_file_vacancy(list_job)
            return list_job

    def write_file_vacancy(self, jobs):
        with open('vacancy_list_sjru.json', 'w', encoding='utf-8') as json_file:
            json.dump(jobs, json_file, sort_keys=False, indent=4, ensure_ascii=False)
