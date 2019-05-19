from modules.message import Message
from modules.xlsxparser import XLSXExporter

class MondayFirstSchedule(Message):
    def request(self):
        return "понедельник первая"
    def response(self):
        return XLSXExporter().getSchedule("documents/RIS16PosleVesna.xlsx", 1, 1)

class MondaySecondSchedule(Message):
    def request(self):
        return "понедельник вторая"
    def response(self):
        return XLSXExporter().getSchedule("documents/RIS16PosleVesna.xlsx", 1, 2)

class TuesdayFirstSchedule(Message):
    def request(self):
        return "вторник первая"
    def response(self):
        return XLSXExporter().getSchedule("documents/RIS16PosleVesna.xlsx", 2, 1)

class TuesdaySecondSchedule(Message):
    def request(self):
        return "вторник вторая"
    def response(self):
        return XLSXExporter().getSchedule("documents/RIS16PosleVesna.xlsx", 2, 2)