import smartcard
import time
from smartcard.CardMonitoring import CardMonitor, CardObserver

from reader.NFC.ACR122 import uid

class ACR122():
    def __init__(self, obs_impl = uid.ReadUidObserver):
        # Declaration
        self.__monitor = None
        self.__observer = None

        # Initialization
        self.__monitor = CardMonitor()
        self.__observer = obs_impl() #XXX: Extend to mutiple observer

    def attachObserver(self):
        self.__monitor.addObserver(self.__observer)

    def detachObserver(self):
        self.__monitor.deleteObserver(self.__observer)
