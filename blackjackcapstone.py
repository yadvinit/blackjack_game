import random

from blackjacklogo import logo


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    choose_card = random.choice(cards)

    return choose_card

def calculate_score(cards):
    if sum(cards)==21  and len(cards) ==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)    
    return sum(cards)

def compare(card1,card2):

    if card1 == card2:
        return "draw"
        
    elif card2 == 0 :
        return "you loose computer has blackjack"
    
    elif card1 == 0 :
        return "you won and you  have blackjack"
    
    elif card1> 21:
        return "you went over. You Lose "
    
    elif card2 > 21:
        return "Opponent went over.You won" 

    elif card1 >card2 :
        return "You won"
    
    else:
        return "You lose"


def Playgame():
    print(logo)
    computer = []
    player =[] 
    is_gameover = False

    for  i  in range(2):
        computer.append(deal_card())
        player.append(deal_card())

    while not is_gameover:

        computer_score = calculate_score(computer)
        player_score = calculate_score(player)


        print(f"player cards {player},  current score is {player_score}")
        print(f"computer first card is  {computer[0]}")

        if player_score ==0 or computer_score == 0 or player_score >21:
            is_gameover = True

        else :
            new_card =input("you want to draw one more card yes or no")

            if new_card == "yes":
                player.append(deal_card())
                
            else:
                is_gameover = True

    while computer_score !=0 and computer_score <17:

        computer.append(deal_card())
        computer_score = calculate_score(computer)
        
    print(f"The final deck of player is :{player}, score is :{player_score}")
    print(f"The final deck of computer is :{computer}, score is :{computer_score}")

    print(f"{compare(player_score,computer_score)}")


while  input("Do you want to play the blackjack game yes or no ").lower() == "yes":
    print("\n"*20)
    Playgame()
        