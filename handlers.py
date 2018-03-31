from message import Message


def main_handler(message: Message):
    if message.body.startswith("Мур"):
        return "Mяу"
    else:
        return 46
