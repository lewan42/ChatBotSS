import requests
from bs4 import BeautifulSoup

class VkBot:

    def __init__(self, user_id):
        self.USER_ID = user_id
        self.USERNAME = self._get_user_name_from_vk_id(user_id)

    def _get_user_name_from_vk_id(self, user_id):
        url = "https://vk.com/id" + str(user_id)
        bs = BeautifulSoup(requests.get(url).text, "html.parser")
        _titleTag = bs.html.head.title

        return self._clean_all_tag_from_str(_titleTag)

    @staticmethod
    def _clean_all_tag_from_str(string):
        result = ""
        not_skip = True
        for i in list(string):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

