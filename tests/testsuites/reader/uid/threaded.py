import time
from reader import reader

def threaded_read_uid(dev, delta):
    Reader = reader.Reader(dev)

    Reader.createObserver()

    time.sleep(delta)

    Reader.removeObserver()
