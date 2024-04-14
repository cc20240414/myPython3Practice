import random

# Project is referenced from https://www.geeksforgeeks.org/number-guessing-game-in-python/

def aNumberGuessGame():

#     It is a function to generate a guess number. Detail as below:
#         1. Ask user input a guess number
#         2  Check the guess number is valid
#         3. If number is valid, return the guess number. Otherwise, go to step and repeat the step.
#     """

    min_number=1
    max_number=100
    boom_number=random.randint(min_number+1,max_number-1)
    guess=0
    count=1
    # print(boom_number)
    
    while guess != boom_number:
        guess = input(f"Please input a number between {min_number} to {max_number}\t: ")
        
        try:
            guess = int(guess)
            if guess == boom_number:
                print(f"\nCongratulations you did it in {count} try.")
                break
            elif guess > boom_number and guess < max_number:
                max_number = guess
            elif guess < boom_number and guess > min_number:
                min_number = guess        
            else:
                print(f"The number range is out of range!!!")
                continue
            count+=1
        except ValueError:
            print(f"It is not a number. Please try agin!!!")
        except:
            print("Unknown error.")
            raise Exception
            
aNumberGuessGame()  