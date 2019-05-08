''' Класс пользователя '''


class User():
    def __init__(self, user_info):
        print(user_info)
        self.id =  user_info["id"]
        self.first_name = user_info["first_name"]
        self.last_name = user_info["last_name"]
        self.sex = user_info["sex"]

        self.bdayte = ""
        if 'bdate' in user_info:
            self.bdate = user_info["bdate"]
        
        self.city = ""
        if 'city' in user_info:
            self.city = user_info["city"]["title"]
        
        self.country = ""
        if 'country' in user_info:
           self.country = user_info["country"]["title"]

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name) 

    def get_full_info(self):
        ''' Вся информация '''
        text = self.__str__()+"\n"
        if self.bdate != "":
            text += "Дата рождения: {}\n".format(self.bdate)
        if self.country != "":
            text += "Страна: {}\n".format(self.country)
        if self.city != "":
            text += "Город: {}\n".format(self.city)
        return text
        

