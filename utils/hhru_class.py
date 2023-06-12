import json
from abc import ABC
from pprint import pprint

import requests

from utils.get_hh_info import AbstractJobPlatform

class JobListing:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"Title: {self.title}Link: {self.link}Salary: {self.salary}Description: {self.description}"


class HHJobPlatform= str(JobListing(title, link, salary, description))(AbstractJobPlatform, ABC):

    def __init__(self, keyword):
        self.keyword = keyword

    def connect(self, params=None):
        # Реализация подключения к API hh.ru
        #base_url = f"https://hh.ru/search/vacancy?text={self.keyword}"
        # self.headers = {"https://hh.ru/search/vacancy": self.keyword}
        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.keyword, 'area': 1, "per_page": 10}
        headers = {
            "User-Agent": "50355527",  # Replace with your User-Agent header
        }

        response = requests.get(url, params=params, headers=headers)


        #response = requests.get(base_url, params=params)

        return response

    def get_jobs(self):
        # Получение вакансий с hh.ru
        # url = 'https://api.hh.ru/vacancies'
        # params = {'text': query, 'area': 1}
        # response = requests.get(url, params=params)
        if self.connect().status_code == 200:
            data = self.connect().json()
            jobs = []
            for item in data['items']:
                title = item['name']
                link = item['url']
                salary = item['salary']['from'] if item['salary'] and 'from' in item['salary'] else None
                description = item['snippet']['requirement'] if item['snippet'] and 'requirement' in item[
                    'snippet'] else None
                job = str(JobListing(title, link, salary, description))
                jobs.append(job)
            return jobs


        else:
            print(f"Request failed with status code: {self.connect().status_code}")


huemoe = HHJobPlatform('python')
pprint(huemoe.get_jobs())
#print(huemoe.get_jobs())

#hfhf = JobListing('title', 'link', 'salary', 'description')
#print(str(hfhf))




