from numbers import Number
import random

guesses = 0

def game():
    print("Welcome player. \nLet's play a game where I pick a number between 1 and 100 and you try to guess it.")
    ready = input("Are you ready to get started? Y/N\n")
    ready = ready.lower()

    if ready == 'n' or ready == 'exit' or ready == 'quit':
        print("Come back when you're ready to play")
        exit()

    elif ready == 'y':
        print("Let's get started!")
        number = random.randint(0, 100)

        def game_time():
            guess = input("What number am I thinking of?\n")
            guess = int(guess)
            global guesses

            if guess == number:
                guesses = guesses + 1
                print(f"That's my number! You guessed it!\nIt took you {str(guesses)} guesses to get it.")
                guesses = 0
                again = input("\nWould you like to play again? Y/N\n")
                again = again.lower()
                
                if again == 'y':
                    game()
                else:
                    exit()

            elif guess < 1 or guess > 100:
                print("The number is between 1-100. Choose a correct number\n")
                game_time()
            
            else:
                if guess > number:
                    print("You guessed a number that's too high")
                    guesses = guesses + 1
                    game_time()
                else:
                    print("You guessd a number that's too low")
                    guesses = guesses + 1
                    game_time()




        game_time()
    else:
        print("You have to say yes, no, or exit.\nTry again...\n")
        game()


game()