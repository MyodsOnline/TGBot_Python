from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from settings import config
from database.dbalchemy import DBManager


class Keyboards:
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD[name])

    @staticmethod
    def remove_menu():
        return ReplyKeyboardRemove()

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_back = self.set_btn('<<')
        self.markup.row(itm_btn_back)
        return self.markup

    def settings_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_back = self.set_btn('<<')
        self.markup.row(itm_btn_back)
        return self.markup

    def category_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup
