from datetime import datetime


class Message:
    def __init__(self, msg_id, date, out, user_id, body, is_from_user):
        self.id = msg_id
        self.date = datetime.fromtimestamp(date)
        self.out = out
        self.user_id = user_id
        self.body = body
        self.is_from_user = bool(int(is_from_user))

    @staticmethod
    def from_json(json):
        return Message(json["id"], json["date"], json["out"], json["user_id"], json["body"], json["out"])

    def __eq__(self, other):
        return isinstance(other, Message) and self.id == other.id

    def __hash__(self):
        return self.id


class MessageParsingError(Exception):
    pass
