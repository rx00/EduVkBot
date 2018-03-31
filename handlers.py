from message import Message


def main_handler(message: Message):
    if message.body.startswith("Мур"):
        return "Mяу"  # если функция вернет str, то бот ответит простым сообщением
    else:
        return 46  # если функция вернет int, то бот ответит пользователю id стикера
