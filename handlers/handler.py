from abc import ABC, abstractmethod
from database.dbalchemy import DBManager
from markup.markup import Keyboards


class Handler(ABC):
    def __init__(self, bot):
        self.bot = bot
        self.keyboards = Keyboards()
        self.DB = DBManager()

    def handle(self):
        pass
