import os
from emoji import emojize


TOKEN = '6196031317:AAEBEJT05W1ogVhyi4T4nAnMzXN17-w-anU'
DBASE_NAME = 'ods_seller_bot.sqlite'
AUTHOR = 'user'
VERSION = '0.0.1'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:/' + BASE_DIR, DBASE_NAME)

COUNT = 0

KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

COMMANDS = {
    'START': "start",
    'HELP': "help",
}


if __name__ == '__main__':
    print(DATABASE)
    for k, v in KEYBOARD.items():
        print(v)