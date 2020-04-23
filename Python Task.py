## Modified number guessing game
import random


def getUserNum():
    user_num = int(input("Please enter your number: "))
    return user_num


def generateRandomNumber(n):
    num = random.randint(1, n)
    return num


def guessingGame(n, allowedGuesses, userGuess, correctGuess):
    numberOfGuesses = 0
    num = generateRandomNumber(n)
    print(num)  # You can delete this, just kept it in for test purposes.

    while numberOfGuesses < allowedGuesses:
        if num != userGuess:
            print("You guessed wrong. You have to guess again...")
            userGuess = getUserNum()
            numberOfGuesses += 1
            print("You have", allowedGuesses - numberOfGuesses, "guesses left!")
        else:
            print("Congratulations! You guessed correctly after ", numberOfGuesses, " guesses!")
            correctGuess = True

            break

    if not correctGuess:
        print("You failed after ", numberOfGuesses, " number of tries?")  # You can recompose my error messages


if __name__ == '__main__':
    print("Enter 1 for easy ")
    print("Enter 2 for medium ")
    print("Enter 3 for difficult ")

    level = int(input("Please choose a difficulty level."))

    user_guess = getUserNum()
    print(user_guess)

    if level == 1:
        guessingGame(10, 6, user_guess, False)
    elif level == 2:
        guessingGame(20, 4, user_guess, False)
    elif level == 3:
        guessingGame(50, 3, user_guess, False)
    else:
        print("You have to choose something valid! ")
