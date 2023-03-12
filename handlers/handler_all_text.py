from settings import config
from settings.message import MESSAGES
from handlers.handler import Handler


class HandlerAllText(Handler):
    def __init__(self, bot):
        super().__init__(bot)
        self.step = 0

    def pressed_btn_info(self, message):
        self.bot.send_message(message.chat.id,
                              MESSAGES['trading_store'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.info_menu())

    def pressed_btn_settings(self, message):
        self.bot.send_message(message.chat.id,
                              MESSAGES['var'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.settings_menu())

    def pressed_btn_back(self, message):
        self.bot.send_message(message.chat.id,
                              f'you come back',
                              reply_markup=self.keyboards.start_menu())

    def pressed_btn_category(self, message):
        self.bot.send_message(message.chat.id,
                              f'Category menu',
                              reply_markup=self.keyboards.remove_menu())
        self.bot.send_message(message.chat.id,
                              f'Make your choose',
                              reply_markup=self.keyboards.category_menu())

    def pressed_btn_product(self, message, product):
        self.bot.send_message(message.chat.id,
                              f'Category {config.KEYBOARD[product]}',
                              reply_markup=self.keyboards.set_select_category(config.CATEGORY[product]))
        self.bot.send_message(message.chat.id,
                              f'OK',
                              reply_markup=self.keyboards.category_menu())

    def handle(self):
        @self.bot.message_handler(func=lambda message:True)
        def handle(message):
            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)
            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)
            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)
            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')
            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')
            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')