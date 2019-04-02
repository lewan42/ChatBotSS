# -*- coding: utf-8 -*-
import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_bot import VkBot

'''
vk_session = vk_api.VkApi(token='b749257462cd73d0dc9670c4de06be5f692c862b612a5a0c77d29f486ad78ff7e58da213ac5fb7901105d')
'''

vk_session = vk_api.VkApi(token='c71283221733a6f323993735ad971575ff4fc92ded92812cb2fbf3159e79e5768d1fdef874348ac3a83fc')


def write_msg(user_id, random_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'random_id': random_id, 'message': message})


def main():
    _longPoll = VkLongPoll(vk_session)
    print("Бот запущен!")
    print("------------------------------")
    print()
    for event in _longPoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            bot = VkBot(event.user_id)
            if event.to_me:
                request = event.text
                if request == "Привет" or request == "привет":
                    write_msg(event.user_id, get_random_id(), "Ну привет, " + bot.USERNAME)
                elif request == "Не понял что ты написал":
                    write_msg(event.user_id, get_random_id(), "Не дразни")
                else:
                    write_msg(event.user_id, get_random_id(), "Не понял что ты написал")

            print('Новое сообщение:')
            if event.from_me:
                print('От бота для: ' + bot.USERNAME + ' ', end='')
            elif event.to_me:
                print('Для бота от: ' + bot.USERNAME + ' ', end='')
            if event.from_user:
                print(event.user_id)
            print('Текст: ', event.text)
            print("------------------------------")
            print()


if __name__ == '__main__':
    main()



