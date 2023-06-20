from abc import ABC, abstractmethod


class AbstractJobPlatform(ABC):
    """Абстрактный класс , обязывающий создание методов в классах наследниках"""
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_jobs(self, query):
        pass

    @abstractmethod
    def write_file_vacancy(self, jobs):
        pass
