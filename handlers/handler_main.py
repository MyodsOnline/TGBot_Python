from handlers.handler_com import HandlerCommands


class HandlerMain:
    def __init__(self, bot):
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)

    def handle(self):
        print('BOT HANDLER STARTED')
        self.handler_commands.handle()
