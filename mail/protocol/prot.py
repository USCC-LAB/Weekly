from abc import ABCMeta
from abc import abstractmethod


class Prot(metaclass=ABCMeta):

    @abstractmethod
    def login(self, account, passwd):
        pass

    @abstractmethod
    def send(self, frm, to, subject, content):
        pass

    @abstractmethod
    def quit(self):
        pass
