import abc
from database.dbalchemy import DBManager
from markup.markup import Keyboards


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, bot):
        # get a bot object
        self.bot = bot
        # button layout
        self.keyboards = Keyboards()
        # manager for working with the database
        self.DB = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
