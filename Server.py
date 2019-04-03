import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_bot import VkBot
from Messages import *

class Server(vk_api.VkApi):
    def __init__(self, ptoken):
        super().__init__(token = ptoken)
        self.longPoll = VkLongPoll(self)
        self.bot = VkBot()
        self.msgs = [RepeatMsg(self.bot), HelloMsg(self.bot), ByeMsg(self.bot), WhoIMsg(self.bot), IDontNow(self.bot)]

    def run(self):
        print(self.start_msg())
        for event in self.longPoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                self.msg_handler(event)
                print(self.msg_log(event, self.bot))
    
    def start_msg(self):
        return "Бот запущен!\n" + "--"*10  + "\n"

    def msg_handler(self, event):
        self.bot.setup(event)
        if event.to_me:
            self.msg_to_me(event)
               
    def msg_to_me(self, event):
        for msg in self.msgs:
            text = msg.get(event.text)
            if text != "":
                self.send_msg(event,text)
                break
        
    def send_msg(self, event, msg):
        self.method('messages.send', {'user_id': event.user_id, 'random_id': get_random_id(), 'message': msg})

    def msg_log(self, event, bot):
        log = 'Новое сообщение:\n'
        if event.from_me:
            log += 'От бота для: {0} '.format(bot.USERNAME)
        elif event.to_me:
            log +=  'Для бота от: {0} '.format(bot.USERNAME)
        if event.from_user:
            log +=  str(event.user_id)
        return log

    