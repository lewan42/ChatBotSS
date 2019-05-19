from modules.message import Message
from modules.xlsxparser import XLSXExporter

class HelloMsg(Message):
    def request(self):
        return "привет"
    def response(self):
        return  "Ну привет, {} {}".format(self.user.first_name, self.user.last_name)
        
class ByeMsg(Message):
    def request(self):
        return "пока"
    def response(self):
        return  "Ну пока!"

class WhoIMsg(Message):
    def request(self):
        return "кто я"
    def response(self):    
        return  self.user.get_full_info()

class WhoYouMsg(Message):
    def request(self):
        return "(кто ты)|(ты кто)"
    def response(self):
        return  "Я, Секретарша студента 😃"

class IDontNow(Message):
    def get(self, server, event):
        self.setup(server, event)
        return "Не понял, что ты написал 🤔"




