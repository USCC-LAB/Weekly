from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString

import sys
from reader import observer

class ReadUidObserver(observer.GenericObserver):
    def __init__(self):
        self.cards =[] # Inserted Card

    def readUid(self, card):
        # follow http://downloads.acs.com.hk/drivers/en/API-ACR122U-2.02.pdf
        GETDATA = [0xFF, 0xCA, 0x00, 0x00, 0x00]

        card.connection = card.createConnection()
        card.connection.connect()

        resp, sw1, sw2 = card.connection.transmit(GETDATA)
        print(resp, "%.2x %.2x" %(sw1, sw2))


    def insert_action(self, card):
        print('+Inserted: ', toHexString(card.atr))
        if card not in self.cards:
            self.cards += [card]
            self.readUid(card)

    def remove_action(self, card):
        print('-Removed: ', toHexString(card.atr))
        if card in self.cards:
            self.cards.remove(card)
