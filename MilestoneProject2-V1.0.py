#WAR GAME
import random
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
suits = ("Clubs","Diamons","Hearts","Spades")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")

#CARD CLASS
#Suit, Rank, Value
class CARD:
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    
#Deck Class
#52 Cards Deck
class DECK:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = CARD(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#Player Class
class PLAYER:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type({}):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return self.name + " tiene " + str(len(self.all_cards)) + " cartas"

#Game Logic


#Testing Area
two_hearts = CARD("Hearts", "Two")
three_clubs = CARD("Clubs","Three")
a = two_hearts.value < three_clubs.value 
print(a)
mydeck = DECK()
b = mydeck.all_cards[-1]
print("guia")
print(b)
print("guia")
mydeck.shuffle()
c = mydeck.all_cards
for x in c:
    print(x)
numero = len(mydeck.all_cards)
print (numero)
carta1 = mydeck.deal_one()
print (carta1)
numero2 = len(mydeck.all_cards)
print (numero2)
newplayer = PLAYER("Diego")
print (newplayer)
newplayer.add_cards(two_hearts)
newplayer.add_cards(three_clubs)
print(newplayer)
print(newplayer.all_cards[1])
newplayer.remove_card()
print(newplayer)

#testing github again hehehe greetings
