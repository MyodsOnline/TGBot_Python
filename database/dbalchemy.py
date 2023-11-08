from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.dbcore import Base

from settings import config
from models.product import Products
from models.category import Category


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance


class DBManager(metaclass=Singleton):
    def __init__(self):
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if self._session:
            print('success')

        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)
            print('DATABASE CREATED')

    def select_all_products_category(self, category):
        print('We are here')
        result = self._session.query(Products).filter_by(category_id=category).all()
        if result:
            print(result)
        else:
            print('NO RESULT')
        self.close()
        return result

    def close(self):
        self._session.close()



if __name__ == '__main__':
    db = DBManager()
    # db.select_all_products_category(1)