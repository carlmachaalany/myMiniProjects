'''
Paths:
- a function that 
- double
- split
- insurance
- side bets

'''

from random import *

def display_welcome_menu():
    
    """ (NoneType) -> NoneType

    This function displays the welcome menu
    
    """
    
    print("Hello! Welcome to the table of BlackJack!")
    
    
def hit_card():
    
    """ (NoneType) -> str
    
    This function hits a card 

    """
    
    cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♣', '♦', '♥', '♠']
    return choice(cards) + choice(suits)

def get_score_card(card):
    
    """ (str) -> int

    This function returns the value of the card
    
    """
    
    card = card[0]
    
    if card == 'A':
        return 11
    elif card in ['1','J','Q','K']:
        return 10
    
    return int(card)

def can_play(money_wallet, money_bet):
    
    """ (num, num) -> bool

    This function checks if the player has enough money to play
    
    """
    
    if 0.0 < money_bet <= money_wallet:
        return True
    
    return False

def split(first_num, second_num):
    
    """ (int, int) -> NoneType """
    
    if first_card == second_card:
        choice = input("Do you want to split?")
        if choice == 'yes':
            one = hit_action_and_results(first_num)
            two = hit_action_and_results(second_num)
            return [one, two]
        elif choice == 'no':
            return
        
            
            
            
    
    return False



    
    
    
    