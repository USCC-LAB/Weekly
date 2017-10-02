import smartcard
import time
from smartcard.CardMonitoring import CardMonitor, CardObserver

from reader.NFC.ACR122 import uid

class ACR122():
    def __init__(self, obs_impl = uid.ReadUidObserver):
        self.monitor = CardMonitor()
        self.observer = obs_impl() #XXX: Extend to mutiple observer

    def attachObserver(self):
        self.monitor.addObserver(self.observer)

    def detachObserver(self):
        self.monitor.deleteObserver(self.observer)
