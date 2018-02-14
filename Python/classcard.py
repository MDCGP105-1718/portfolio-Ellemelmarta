import random

Suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
Numbers = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Card(object):
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
        self.card = self.suit, self.number
#    def BuildCards(self):
#        for cardnumber in range (1,13):
#            for cardsuit in (Heart,Spades,Clubs,Diamonds):
#                print (cardsuit + cardnumber)

    def __str__ (self):
        return self.number + ' of ' + self.suit

# put this into another class called deck
# for cardnumber in range (1,14):
#     for suitname in (H, S, C, D):
