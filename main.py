
#Rules I followed
#https://bicyclecards.com/how-to-play/blackjack
import random

ranks = ('Two', 'Three','Four','Five','Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Cards:
    def __init__(self,rank):
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' is worth ' + str(self.value)

    def get_value(self):
        return int(self.value)

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(4):
            for rank in ranks:
                self.deck.append(Cards(rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def pass_out_cards(self,player):
        for card in range(2):
            player.hand_one.append(self.deck.pop(card))

class Player:
    def __init__(self,name):
        self.name = name

        self.balance = 0

        self.hand_one = []
        self.hand_two = []

    def get_hand_one(self,deck):
        pass

    def hit(self,deck):
        self.hand_one.append(deck.pop(0))

    def stand(self):
        pass

    def double_down(self):
        pass

    def split(self):
        self.hand_two.append(self.hand_one.pop())

    def clear_hands(self):
        self.hand_one.clear()
        self.hand_two.clear()

    def print_name(self):
        return str(self.name)


new_deck = Deck()
new_deck.shuffle()
playing = True

name = input("What is your name? ")
player_1 = Player(input)

print('Welcome to BlackJack ' + name + "!")

new_deck.pass_out_cards(player_1)

hand = player_1.get_hand_one(new_deck)

#Trying to display the current value of cards in hand
print("Your current hand is " + str(hand))



