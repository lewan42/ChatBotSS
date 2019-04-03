import requests
from bs4 import BeautifulSoup

class VkBot:

    def setup(self, event):
        self.USER_ID = event.user_id
        self.USERNAME = self._get_user_name_from_vk_id(self.USER_ID)

    def _get_user_name_from_vk_id(self, user_id):
        url = "https://vk.com/id" + str(user_id)
        bs = BeautifulSoup(requests.get(url).text, "html.parser")
        _titleTag = bs.html.head.title
        print(_titleTag)

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

