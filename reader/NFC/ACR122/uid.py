from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString

import sys
from reader import observer

class ReadUidObserver(observer.GenericObserver):
    def __init__(self):
        # Declaration
        self.__cards = None # Inserted cards

        # Initialization
        self.__cards = [] 

    def readUid(self, card):
        # follow http://downloads.acs.com.hk/drivers/en/API-ACR122U-2.02.pdf
        GETDATA = [0xFF, 0xCA, 0x00, 0x00, 0x00]

        card.connection = card.createConnection()
        card.connection.connect()

        resp, sw1, sw2 = card.connection.transmit(GETDATA)
        print('{0} {1:.2x} {2:.2x}'.format(resp, sw1, sw2))


    def insert_action(self, card):
        print('+Inserted: {0}'.format(toHexString(card.atr)))
        if card not in self.__cards:
            self.__cards += [card]
            self.readUid(card)

    def remove_action(self, card):
        print('-Removed: {0}'.format(toHexString(card.atr)))
        if card in self.__cards:
            self.__cards.remove(card)
