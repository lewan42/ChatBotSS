import botServerBase
import settings
from docxtpl import DocxTemplate
from messages import *


class BotServer(botServerBase.BotServerBase):
    def __init__(self):
        super().__init__(settings.GROUP_TOKEN, settings.GROUP_ID)
        self.modules = settings.MODULES
    
    def newMessage(self, event):
        super().newMessage(event)

        ok = False
        for module in self.modules:
            print("Check")
            msg = eval(module+"()")
            text = msg.get(self, event)
            print("Check2")
            if text != "":
                ok = True
                self.send_message(event,text)   
            
        print("Check3")        
        if not ok:
            self.send_message(event, IDontNow().get(self, event))

    def doc_gen(self, src_file, values, out_File):
        "Генерация документа"
        doc = DocxTemplate(src_file)
        doc.render(values)
        doc.save(out_File)
    
    def upload_gen_document(self, event, file, values, title = "out"):
        "Генерация и загрузка документа"
        self.doc_gen(file, values, "out.doc")
        self.upload_document(event, "out.doc", title)
    
