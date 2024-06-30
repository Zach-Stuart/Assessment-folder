import random
from random import randint

# initialise variables
rounds_played = 0
correct = 0
incorrect = 0
game_history = []


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid response from the following list: {valid_ans}"

    while True:

        # make sure user response is lowercase
        user_response = input(question).lower()
        for item in valid_ans:
            # check if user response is a word in the list
            if item == user_response:
                return item

            # check if user response is same as first letter of an item in list
            elif user_response == item[0]:
                return item

        # print error if user enters invalid response
        print(error)
        print()


# Checks for an integer ,more than 0
def int_checker(question):
    while True:

        error = "Please enter an integer that is 1 or higher"

        to_check = input(question)

        try:
            response = int(to_check)

            # Checks if integer is greater than or equal to 1
            if response < 1:
                print(error)
                print()
            else:
                return response

        except ValueError:
            print(error)
            print()


# display instructions
def instructions():
    print('''
    Instructions
    ------------
    You will be shown a pair of random numbers between 1 and 20.
    You'll have to figure out what those two numbers make when multiplied.
    Enter your answer and see how you did!
    
    Bottom Text
    ''')

    # generate two random numbers and answer


def num_gen():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    ans = a * b
    return a, b, ans


# main routine

# instructions

want_instructions = string_checker("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()
begin = string_checker("Alright, would you like to begin? ")
if begin == "yes":
    print("Okay, let's get started!")
else:
    print()
    print("Uh, okay.")

# game loop
while begin == "yes":
    # get user choice
    a, b, ans = num_gen()
    user_choice = int_checker(f"What is the product of {a} * {b}? ")
    print(f"You chose: {user_choice}")

    # tells user if they were right or wrong
    if user_choice == ans:
        round_result = "correct"
        correct += 1
        print("Congrats! You were correct!")
        print()
    else:
        round_result = "incorrect"
        incorrect += 1
        print(f"Sorry, you were incorrect. The correct answer was {ans}.")
        print()
    rounds_played += 1
    print(correct, incorrect, rounds_played)

    # asks user if they want to play again
    try_again = string_checker("Would you like to play again? ")
    if try_again == "no":
        print()
        break

    # Loop ends here


# ask if player wants to see statistics
if try_again == "no":
    stats = string_checker("Okay, would you like to see your game history / statistics before you go? ")
    if stats == "yes":
        # calculate statistics
        # if rounds_played > 0:
        percent_correct = correct / rounds_played * 100
        percent_incorrect = incorrect / rounds_played * 100
        # output game statistics
        print("\n*** Game Statistics ***")
        print(f"Correct: {percent_correct} \t"
              f"Incorrect: {percent_incorrect} \t")
    else:
        print("Okay. Thank you for playing!")
