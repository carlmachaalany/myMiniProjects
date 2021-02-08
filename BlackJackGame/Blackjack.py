from bj_utils import *

def double_action(card):
    
    choice = input("Do you want to double?")
    if choice == "yes":
        summation = card
        hit = hit_card()
            
def hit_action_and_results(card):
    
    """ (int)--> int
    This function does the hitting sequence 
    """
    
    hit = hit_card()
    summation = card + get_score_card(hit)
    while summation<21:
        print("Hit:",hit)
        print("You now have:", summation)
        choice = input("Hit again?")
        if choice == "yes":
            hit = hit_card()
            summation += get_score_card(hit)
        elif choice == "no":
            return summation
        
    print("Hit:",hit)
    print("You now have:",summation)
    print("Bust :(")
    return 22
          
            
def play():
    
    display_welcome_menu()
    
    money_wallet = float(input("Please enter your money here: "))
    money_bet = float(input("How much would you like to bet? "))
    
    if not can_play(money_wallet, money_bet):
        print("Insufficient fund. See you next time!")
        return
    
    first_card = hit_card()
    second_card = hit_card()
    dealer_card = hit_card()
    first_num = get_score_card(first_card)
    second_num = get_score_card(second_card)
    dealer_num = get_score_card(dealer_card)
    summation = first_num + second_num
    
    print("Your cards:",first_card,second_card)
    print("Dealer card:",dealer_card)
            
    choice = input("Hit, Stand, or Double?")
    if choice in ["hit","double"]:
        summation = hit_action_and_results(summation)
        if summation == 22:
            if choice == 'double':
                money_wallet -= 2*money_bet
            else:
                money_wallet -= money_bet
            print("Balance:", money_wallet)
            return
    
    dealer_hit = hit_card()
    dealer_summation = dealer_num + get_score_card(dealer_hit)
    print("Dealer's turn!\nDealer's hit:",dealer_hit)
    print("Dealer has now:",dealer_summation)
    
    while dealer_summation<17:
        dealer_hit = hit_card()
        dealer_summation += get_score_card(dealer_hit)
        print("Dealer's hit:",dealer_hit)
        print("Dealer has now:",dealer_summation)
    
    if dealer_summation >21:
        print("Dealer bust! You win!")
        if choice == 'double':
            money_wallet += 2*money_bet
        else:
            money_wallet += money_bet
        print("Balance:", money_wallet)
        return
    
    if dealer_summation > summation:
        print("Dealer has more, you lose :(")
        if choice == 'double':
            money_wallet -= 2*money_bet
        else:
            money_wallet -= money_bet
        print("Balance:", money_wallet)
        return
    
    elif dealer_summation < summation:
        print("You have more, you win!")
        if choice == 'double':
            money_wallet += 2*money_bet
        else:
            money_wallet += money_bet
        print("Balance:", money_wallet)
        return
    
    else:
        print("Push!")
        print("Balance:", money_wallet)
        return
        
        
    
        
            
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    

