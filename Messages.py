class Message:
    past_msg = "ttt"
    
    def __init__(self, bot):
        self.bot = bot
    
    def request(self):
        return ""

    def response(self):
        return ""

    def get(self, prequest):
        print(prequest, ":", Message.past_msg)
        if self.request() in prequest.lower():
            Message.past_msg = self.response().lower()
            return self.response()
        return ""

class HelloMsg(Message):
    def request(self):
        return "привет"
    def response(self):
        return  "Ну привет, {0}".format(self.bot.USERNAME)
        
class ByeMsg(Message):
    def request(self):
        return "пока"
    def response(self):
        return  "Ну пока!"

class WhoIMsg(Message):
    def request(self):
        return "кто я"
    def response(self):
        return  "Ты, {0}".format(self.bot.USERNAME)

class RepeatMsg(Message):
    def request(self):
        return Message.past_msg
    def response(self):
        return  "Не дразни!"

class IDontNow(Message):
    def get(self, prequest):
        text = "Не понял что ты написал"
        Message.past_msg = text.lower()
        return text

