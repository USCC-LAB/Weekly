from reader.NFC.ACR122 import ACR122

class Reader:
    def __init__(self, dev = ACR122.ACR122):
        self.__dev = dev()

    def createObserver(self):
        self.__dev.attachObserver()
    
    def removeObserver(self):
        self.__dev.detachObserver()
