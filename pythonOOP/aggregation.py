

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def list_cards(self):
        for c in self.cards:
            print(f"Card is the {c.number} of {c.suit}")

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

d1 = Deck("Bicycle Playing Cards")

c1 = Card(7, "Hearts")
c2 = Card(3, "Spades")
c3 = Card(10, "Diamonds")
c4 = Card(8, "Clubs")

d1.add_card(c1)
d1.add_card(c2)
d1.add_card(c3)
d1.add_card(c4)

d1.list_cards()