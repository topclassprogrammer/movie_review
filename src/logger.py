import datetime
import logging

from src.configuration import Configuration


class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.config = Configuration('logger_config.yml').config
            self.format = self.config['format']
            self.level = self.config['level']
            self.logger = logging.getLogger()
            self.logger.setLevel(self.level)
            formatter = logging.Formatter(self.format)
            file_handler = logging.FileHandler(f'{datetime.datetime.today().date()}_elasticsearch.log')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            self.initialized = True



