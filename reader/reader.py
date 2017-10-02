from reader.NFC.ACR122 import ACR122

class Reader:
    def __init__(self, dev = ACR122.ACR122):
        self.dev = dev()

    def createObserver(self):
        self.dev.attachObserver()
    
    def removeObserver(self):
        self.dev.detachObserver()
