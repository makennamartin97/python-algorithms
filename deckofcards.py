import random

class Card:
    def __init__(self, symbol, letter):
        self.symbol = symbol
        self.letter = letter
        

class Deck:
    def __init__(self):
        self.cards = {
            "Club":['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], 
            "Diamond": ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], 
            "Heart": ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            "Spade": ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q']
        }
    def shuffle(self):
        a = randint(self.cards["Club"])
        return a

deck1 = Deck()
print(type(deck1).__name__)
print(len(deck1.cards))