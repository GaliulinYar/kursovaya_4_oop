import json
import os
from abc import ABC
from pprint import pprint

import requests
from utils.get_hh_info import AbstractJobPlatform


class SuperJobPlatform(AbstractJobPlatform, ABC):

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

    def connect(self):
        # Реализация подключения к API superjob.ru
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': os.getenv('API_KEY'),
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {"count": 1, "page": None,
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
                    salary_min = None
                    salary_max = None

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


ads = SuperJobPlatform('менеджер')
pprint(ads.get_jobs())
print(ads.connect())


