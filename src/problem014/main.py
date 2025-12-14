#​14. Simple Guessing Game
# Goal: The script randomly selects a number between 1 and 100. The user has to guess the number. The script should tell them if their guess is too high or too low until they get it right.
# Concepts: random module, while loops.
import random
def gussing_game():
    number=random.randint(1,100)
    guess_count=0
    while True:
        guess=int(input("guess a number between 1 and 100: "))
        guess_count+=1
        if guess<number:
            print("too low")
        elif guess>number:
            print("too high")
        else:
            print(f"congratulations! you guessed the number {number} in {guess_count} attempts")
            break

if __name__=="__main__":
    gussing_game()
