



from random import choice

def determine_winner(user_choice, computer_choice):
    
    """
    This function is designed to determine the winner of a game of rock, paper, scissors between the user and a computer
    The required parameters are
    
    """
    
    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice
    #return "OOPS"



if __name__ == "__main__":

    #
    # USER SELECTION
    #



    choices = ["rock", "paper", "scissors"]

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(choices)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    #if u == "rock" and c == "rock":
    #    print("It's a tie!")
    #elif u == "rock" and c == "paper":
    #    print("The computer wins")
    #elif u == "rock" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "paper" and c == "rock":
    #    print("The computer wins")
    #elif u == "paper" and c == "paper":
    #    print("It's a tie!")
    #elif u == "paper" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "scissors" and c == "rock":
    #    print("The computer wins")
    #elif u == "scissors" and c == "paper":
    #    print("The user wins")
    #elif u == "scissors" and c == "scissors":
    #    print("It's a tie!")


winner = determine_winner(u,c)

if winner == u:
    print("You won!")
elif winner == c:
    print("The computer won.")
else:
    print("It's a tie.")