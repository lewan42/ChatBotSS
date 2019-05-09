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
        text = "Не понял, что ты написал"
        Message.past_msg = text.lower()
        return text

class GiveMeMoney(Message):
    def request(self):
        return "заявление на стипендию"
    def response(self):
        values = {
            "course" : "",
            "group" : "",
            "fio" : self.user.last_name + " " + self.user.first_name[0],
            "mobile" : "",
            "active" : ""}

        self.server.upload_gen_document(self.event, "documents/SchApp.docx", values, "Степуха!")

        return  "Готово!"

class Schedule(Message):
    def request(self):
        return "расписание"
    def response(self):    
        return XLSXExporter().export("documents/RIS16PosleVesna.xlsx")
