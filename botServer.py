from modules.botServerBase import BotServerBase
from modules.gendoc import GenDoc
import settings
from messages import *

class BotServer(BotServerBase):
    def __init__(self):
        super().__init__(settings.GROUP_TOKEN, settings.GROUP_ID)
        self.modules = settings.MODULES
    
    def newMessage(self, event):
        super().newMessage(event)

        ok = False
        for module in self.modules:
            msg = eval(module+"()")
            text = msg.get(self, event)
            if text != "":
                ok = True
                self.send_message(event,text)        
        if not ok:
            self.send_message(event, IDontNow().get(self, event))
    
    def upload_gen_document(self, event, file, values, title = "out"):
        "Генерация и загрузка документа"
        self.GenDoc().get(file, values, "out.doc")
        self.upload_document(event, "out.doc", title)
    
