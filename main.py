import random
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] # 10 J Q K 

def draw_card():
    return random.choice(deck); 

def total_in_hand(hand):
    total = sum(hand)
    ace_count = hand.count(1)

    while ace_count>0 and total+10 <=21:
        total+=10
        ace_count -=1
    return total

def is_soft(hand): #17
    total = sum(hand)
    return 1 in hand and (total +10) == 17

def player_turn(hand):
    while total_in_hand(hand) < 17:
        hand.append(draw_card())
    return hand

def dealer_turn(hand): 
    while total_in_hand(hand) < 17 and is_soft(hand):
        hand.append(draw_card)
    return hand

def play():
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]

    player = player_turn(player)

    if total_in_hand(player) > 21:
        return -1 # alr lose
    
    dealer = dealer_turn(dealer)

    player_total = total_in_hand(player)
    dealer_total = total_in_hand(dealer)

    if dealer_total > 21:
        return 1
    elif player_total > dealer_total:
        return 1
    elif player_total < dealer_total:
        return -1
    else:
        return 0
    
def blackjack_sim(n): # n times of sims
    wins = 0
    losses = 0
    draws = 0

    for _ in range(n):
        res = play()
        if res == 1:
            wins+=1
        elif res == 0:
            draws+=1
        elif res ==-1:
            losses +=1
    ev = (wins-losses)/n

    print("Games:", n)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Draws:", draws)
    print("Expected Payoff:", ev)


blackjack_sim(1000000) # 1 million
