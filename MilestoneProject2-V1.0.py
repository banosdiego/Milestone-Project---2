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
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        pass

    def add_cards(self):
        pass

    def __str__(self):
        return self.name + " tiene " + str(len(self.all_cards)) + " cartas"
#2 players with 26 Cards Each
#Game Logic


#Testing Area
two_hearts = CARD("Hearts", "Two")
three_clubs = CARD("Clubs","Three")
a = two_hearts.value < three_clubs.value 
print(a)
mydeck = DECK()
b = mydeck.all_cards[-1]
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
newplayer = Player("Diego")
print (newplayer)

#testing github again hehehe greetings
