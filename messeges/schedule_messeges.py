from modules.message import Message
from modules.xlsxparser import XLSXExporter

class Schedule(Message):
    def request(self):
        return "расписание"
    def response(self):    
        return XLSXExporter().export("documents/RIS16PosleVesna.xlsx")