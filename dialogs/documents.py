from messeges.document_messeges import *
import settings


class Documents():
    def run(self, state, server, event):
        if (state == "listDocsIsActiv"):
            if (eval(settings.DOCUMENTS + "()").get(server, event)):
                return True
            return False
