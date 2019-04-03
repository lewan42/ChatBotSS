class Message:
    """ Класс сообщений """
    past_msg = "ttt"
    
    def __init__(self):
        self.event = None
        self.server = None
    
    def request(self):
        """ Запрос """
        return ""

    def response(self):
        """ Ответ """
        return ""

    def setup(self, server, event):
        """ Настройка """
        self.server = server
        self.event = event

    def get(self, server, event):
        """ Выполнение запроса """
        self.setup(server, event)
        if self.request() in event.text.lower():
            Message.past_msg = self.response().lower()
            return self.response()
        return ""

    def get_info(self):
        """ Информация о пользователе """
        return self.server.get_user_info(self.event)

class HelloMsg(Message):
    def request(self):
        return "привет"
    def response(self):
        return  "Ну привет, {first_name} {last_name}".format(**self.get_info())
        
class ByeMsg(Message):
    def request(self):
        return "пока"
    def response(self):
        return  "Ну пока!"

class WhoIMsg(Message):
    def request(self):
        return "кто я"
    def response(self):
        info = self.get_info()
        text = "Ты, {first_name} {last_name}\n".format(**info)
        if info.get("sex", False):
            text += "Пол: {}\n".format("Мужской" if info["sex"] == 2 else "Женский")
        if info.get("bdate", False):
            text += "Дата рождения: {}\n".format(info["bdate"])
        if info.get("country", False):
            text += "Страна: {}\n".format(info["country"]["title"])
        if info.get("city", False):
            text += "Город: {}\n".format(info["city"]["title"])
        
        return  text

class WhoYouMsg(Message):
    def request(self):
        return "кто ты"
    def response(self):
        return  "Я, Секретарша студента 😃"

class RepeatMsg(Message):
    def request(self):
        return Message.past_msg
    def response(self):
        return  "Не дразни!"

class IDontNow(Message):
    def get(self, server, event):
        self.setup(server, event)
        text = "Не понял, что ты написал"
        Message.past_msg = text.lower()
        return text

