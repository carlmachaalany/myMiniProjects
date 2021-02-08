# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#

from random import shuffle
from time import sleep

# Two useful variables for creating Cards.
SUITE = ['♣', '♦', '♥', '♠']
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
d = {'2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
the_deck = [x+" "+y for x in SUITE for y in RANKS]

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.list_of_cards = the_deck

    def shuffle_deck(self):
        shuffle(self.list_of_cards)

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, half_deck):
        self.hand = half_deck

    def remove_card(self):
        if len(self.hand)!=0:
            return self.hand.pop(0)
        else:
            raise IndexError("No cards left for the player to remove")

    def add_card(self, card):
        self.hand.append(card)

    def add_cards(self, added_cards):
        for card in added_cards:
            self.hand.append(card)

    def __str__(self):
        return str(self.hand)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    # def add_word_card(self, card):
    #     self.health += 1
    #     self.hand.add_card(card)

    def __init__(self, name, hand, health):
        self.name = name
        self.hand = hand
        self.health = health

    def remove_war_card(self):
        if (self.health==0):
            print("\n" + self.name + " WON THE GAME!")
            exit()
        else:
            self.health-=1
            return self.hand.remove_card()

    def add_word_cards(self, added_cards):
        self.health += len(added_cards)
        self.hand.add_cards(added_cards)

    def __str__(self):
        return "Name: " + self.name + "\n" + "Number of cards: " + str(self.health) + "\n" + str(self.hand)

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
player1_name = input("First player, enter your name: ")
player2_name = input("Second player, enter your name: ")

deck = Deck()
deck.shuffle_deck()

p1_hand = Hand(deck.list_of_cards[:27])
player1 = Player(player1_name, p1_hand, 26)

p2_hand = Hand(deck.list_of_cards[27:])
player2 = Player(player2_name, p2_hand, 26)

input("ENTER TO START WAR")
while (player1.health!=0 and player2.health!=0):

    player1_card = player1.remove_war_card()
    player2_card = player2.remove_war_card()
    cards_on_ground = [player1_card, player2_card]

    print("\n" + player1.name + "'s hit: " + player1_card)
    sleep(1)
    print(player2.name + "'s hit: " + player2_card + "\n")
    sleep(1)

    if (d[player1_card[2:]] > d[player2_card[2:]]):
        print(player1.name + " wins the round!" + "\n")
        player1.add_word_cards(cards_on_ground)
    elif(d[player1_card[2:]] < d[player2_card[2:]]):
        print(player2.name + " wins the round!" + "\n")
        player2.add_word_cards(cards_on_ground)

    else:
        print("WE")
        sleep(1)
        print("HAVE")
        sleep(1)
        print("GOT")
        sleep(1)
        print("A BIG")
        sleep(1)
        print("BAD")
        sleep(1)
        print("FREAKING")
        sleep(1)
        print("WAR")
        sleep(1)

        input(player1_name + ", enter for your card show ")
        player1_extra_card = player1.remove_war_card()
        cards_on_ground += [player1_extra_card, player1.remove_war_card(), player1.remove_war_card(), player1.remove_war_card()]
        print("\n" + player1_extra_card + " !!\n")

        input(player2_name + ", enter for your card show ")
        player2_extra_card = player2.remove_war_card()
        cards_on_ground += [player2_extra_card, player2.remove_war_card(), player2.remove_war_card(), player2.remove_war_card()]
        print("\n" + player2_extra_card + " !!\n")
        sleep(1)

        if (d[player1_extra_card[2:]] > d[player2_extra_card[2:]]):
            print(player1.name + " wins the round!!" + "\n")
            player1.add_word_cards(cards_on_ground)
        else:
            print(player2.name + " wins the round!" + "\n")
            player2.add_word_cards(cards_on_ground)

    sleep(1)
    print(player1.name + "'s number of cards:" + str(player1.health))
    print(player2.name + "'s number of cards:" + str(player2.health))
    sleep(1)
    input("ENTER TO START NEXT WAR")



# Use the 3 classes along with some logic to play a game of war!
