import vk
import time
from message import Message, MessageParsingError
from handlers import main_handler

TOKEN = "## ваш токен ##"

API = vk.API(vk.Session(access_token=TOKEN))
API_VERSION = 5.67
LAST_MSG_ID = 0


def handle_message(message: Message):
    answer = main_handler(message)
    if answer is None:
        return
    if isinstance(answer, str):
        API.messages.send(user_id=message.user_id, message=answer, v=API_VERSION)
        time.sleep(0.33)
    elif isinstance(answer, int):
        API.messages.send(user_id=message.user_id, sticker_id=answer, v=API_VERSION)
        time.sleep(0.33)
    else:
        print("Не удалось отправить сообщение, "
              "тк main_handler вернул некорректный ответ! (ожидался <int> или <str>, получен {})".format(type(answer)))


def make_bot_request():
    global LAST_MSG_ID
    try:
        request = API.messages.get(count=50, v=API_VERSION, last_message_id=LAST_MSG_ID)  #
        # ожидается, что бот будет получать не более 50 сообщений в секунду)
        if "error" in request:
            raise MessageParsingError("Ошибка API ({})".format(request["error"]))
        if not LAST_MSG_ID:
            LAST_MSG_ID = Message.from_json(request["items"][0]).id
            return
        for message in (msg for msg in map(Message.from_json, request["items"][::-1]) if msg.id > LAST_MSG_ID):
            LAST_MSG_ID = message.id
            print("Found new message from (https://vk.com/id{})!".format(message.user_id))
            handle_message(message)
    except MessageParsingError as e:
        raise MessageParsingError(e)
    except KeyError as e:
        raise MessageParsingError("Не удалось найти объект по запрошенному индексу {}".format(e))
    except Exception as e:
        raise MessageParsingError("Совсем потрачено ({})".format(e))


print("Bot started...")
while True:
    try:
        make_bot_request()
        time.sleep(1) # опрос api раз в секунду (не чаще, иначе могут забанить бота %) )
    except KeyboardInterrupt:
        print("Останавливаем бота...")
        exit()
    except Exception as err:
        print("Случилась какая-то ошибка ()".format(err))
