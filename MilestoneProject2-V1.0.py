#WAR GAME

#52 Cards Deck
#2 players with 26 Cards Each
#Card Class
#Deck Class
#Player Class
#Game Logic

#CARD CLASS
#Suit, Rank, Value
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
suits = ("Clubs","Diamons","Hearts","Spades")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
class CARD:
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    
two_hearts = CARD("Hearts", "Two")
three_clubs = CARD("Clubs","Three")
a = two_hearts.value < three_clubs.value 
print(a)

#Test from ipad, created on ipad to see if its update the whole git project.