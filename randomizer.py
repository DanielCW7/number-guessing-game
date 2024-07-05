import random

# ask for user to guess, as long as variable isn't the guessed number, keep asking. ask 10 times.
# define a function that runs as long as either the guesses are 10 or less, or a correct guess


def begin_test():

    count = 10
    print("i'm thinking of a number between 1 and 100. you have 10 guesses to get it right! \n")
    random_number = random.randint(1,100)

    while count > 0:
        
        response = input(f"What's your guess? you have {count} guesses remaining. \n ")
        converted_response = int(response)

        if converted_response == random_number:   
            print(f"Correct! the answer was {random_number}")
            break
        elif converted_response > random_number:
            print("======================================================== \n Too high.")
        elif converted_response < random_number:
            print("======================================================== \n Too low.")
        else:
            print("There was an error, please try again")
            continue

        count -= 1

    
    if count == 0:
        print(f" ======================================================== \n you have run out of guesses! {converted_response} was the right answer \n ======================================================== ")

        

begin_test()