import re
class Message:
    """ Класс сообщений """
    
    def __init__(self):
        self.server = None
        self.event = None
        self.user = None

    def setup(self, server, event):
        """ Настройка """
        self.server = server
        self.event = event
        self.user = self.server.get_user_info(self.event)
    
    def get(self, server, event):
        """ Выполнение запроса """
        self.setup(server, event)
        if re.match(self.request(), event.obj.text.lower()):
            return self.response()
        return ""

    def request(self):
        """ Запрос """
        return ""

    def response(self):
        """ Ответ """
        return ""