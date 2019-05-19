from modules.message import Message
from modules.xlsxparser import XLSXExporter

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