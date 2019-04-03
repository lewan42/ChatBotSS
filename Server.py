import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_bot import VkBot
from Messages import *
import json

class Server(vk_api.VkApi):
    """ Сервер бота """
    def __init__(self, ptoken):
        super().__init__(token = ptoken)
        self.longPoll = VkLongPoll(self)
        self.msgs = [RepeatMsg(), HelloMsg(), WhoIMsg(), WhoYouMsg(), ByeMsg()]

    def run(self):
        """ Основной цикл сервера """
        print(self.start_msg())
        for event in self.longPoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                self.msg_handler(event)
                print(self.msg_log(event))
    
    def start_msg(self):
        """ Начальное сообщение """
        return "Бот запущен!\n" + "--"*10  + "\n"

    def msg_handler(self, event):
        """ Обработчик сообщений """
        if event.to_me:
            self.msg_to_me(event)
               
    def msg_to_me(self, event):
        """ Сообщение серверу """
        ok = False
        for msg in self.msgs:
            text = msg.get(self, event)
            if text != "":
                ok = True
                self.send_msg(event,text)
        if not ok:
            self.send_msg(event, IDontNow().get(self, event))

                
        
    def send_msg(self, event, msg):
        """ Отправить сообщение """
        self.method('messages.send', {'user_id': event.user_id, 'random_id': get_random_id(), 'message': msg})

    def get_user_info(self, event):
        """ Получить информацию о пользователе в данной сессии """
        return self.method('users.get', {'user_ids': event.user_id, "fields" :'sex, bdate, city, country, home_town'})[0]

    def msg_log(self, event):
        """ Журнал """
        log = 'Новое сообщение:\n'
        info = self.get_user_info(event)

        if event.from_me:
            log += "От бота для: {first_name} {last_name} ".format(**info)
        elif event.to_me:
            log +=  "Для бота от: {first_name} {last_name} ".format(**info)
        if event.from_user:
            log +=  str(event.user_id)
        return log

    