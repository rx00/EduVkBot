from message import Message


def main_handler(message: Message):
    if message.body.startswith("Мур"): # в message.body хранится текст полученного сообщения
        return "Mяу"  # если функция вернет str, то бот ответит простым сообщением
    else:
        return 46  # если функция вернет int, то бот ответит пользователю id стикера
