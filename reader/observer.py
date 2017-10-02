from smartcard.CardMonitoring import CardObserver

class GenericObserver(CardObserver):
    def __init__(self):
        pass

    def insert_action(self, card):
        pass

    def remove_action(self, card):
        pass

    def update(self, observable, actions):
        (insertedcards, removedcards) = actions
        for card in insertedcards:
            self.insert_action(card)

        for card in removedcards:
            self.remove_action(card)
