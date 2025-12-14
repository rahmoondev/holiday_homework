#​15. Rock, Paper, Scissors
#​Goal: Create a game where the user plays against the computer (which makes a random choice). The script keeps track of the score and declares a winner after 5 rounds.
#​Concepts: random module, complex if/elif/else logic.
import random
def game():
    choices=["rock","paper","scissors"]
    player=0
    computer=0
    tie=0
    rounds=5
    for round in range(rounds):
        user_choice=input("pick between rock, paper, or scissors : ").lower()
        if user_choice not in choices:
            print("invalid entery, try again")
        computer_choice= random.choice(choices)
        print(f"copmuter picked {computer_choice}")
        if user_choice==computer_choice:
            print("its a tie")
            tie+=1
        elif user_choice== "rock" and computer_choice == "scissors" or user_choice== "paper" and computer_choice == "rock" or user_choice== "scissors" and computer_choice == "paper":
            print("you won this round")
            player+=1
        else:
            print("the computer won this round")
            computer+=1
    print(f"final score is you: {player} computer: {computer} ties: {tie}")
    if player>computer:
        print("congrats you won the game!")
    elif computer>player:
        print("the computer won, better luck next time!")
    else:
        print("its a tie")


if __name__=="__main__":
    game()




