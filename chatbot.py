def main():
    intro()
    while True:
        get_user_input1()
        get_user_input2()
        get_user_input3()
        get_user_input4()
        get_user_input5()
        AskRockPaperScissors()
        answer = input("Guess the color that I am thinking of.")
        process_input(answer)
        print("Good job! You guessed it!")
        GoodbyeMessage()
        exit()

def isValid(user_input):
    valid = ["red", "blue", "yellow"]
    return user_input in valid

def process_input(user_input):
    while not isValid(user_input):
        user_input = input("Try again.")
    while isValid:
        user_input
        break

def GoodbyeMessage():
    print("It was fun talking to you today! Goodbye!")

def AskRockPaperScissors():
    userResponse = input("Do you want to play a game of Rock, Paper, Scissors?")
    if userResponse == "no":
        exit()
    elif userResponse == "yes":
        RockPaperScissors()

from random import *
def RockPaperScissors():
    userMove = input("Type your answer (i.e. rock, paper, scissors)")
    Game = ["Rock", "Paper", "Scissors"]
    aRandomIndex = randint(0,len(Game)-1)
    print(Game[aRandomIndex])

    if (Game[aRandomIndex]) == "Scissors" and userMove == "paper":
        print("I win!")

    if (Game[aRandomIndex]) == "Paper" and userMove == "rock":
        print("I win!")

    if (Game[aRandomIndex]) == "Rock" and userMove == "scissors":
        print("I win!")

    if (Game[aRandomIndex]) == "Paper" and userMove == "scissors":
        print("You win!")

    if (Game[aRandomIndex]) == "Scissors" and userMove == "rock":
        print("You win!")

    if (Game[aRandomIndex]) == "Rock" and userMove == "paper":
        print("You win!")

    if (Game[aRandomIndex]) == "Paper" and userMove == "paper":
        print("Tie!")

    if (Game[aRandomIndex]) == "Scissors" and userMove == "scissors":
        print("Tie!")

    if (Game[aRandomIndex]) == "Rock" and userMove == "rock":
        print("Tie!")

def intro():
    print("Welcome to the chatbot!")
    userName = input("What is your name? ")
    print("Hi",userName,"! My name is LiLxFirecracker.")


def get_user_input1():
    FavFood = input("What is your favorite food? ")
    print("I like", FavFood, "too.")

def get_user_input2():
    FavDessert = input("What is your favorite dessert? ")
    print("Wow! I love", FavDessert, "too!")

def get_user_input3():
    FavDrink = input("What is your favorite thing to drink? ")
    print("That's cool. My favorite drink is Cherry Coke.")

def get_user_input4():
    FavAnimal = input("What is your favorite animal? (input plural form)")
    print(FavAnimal, "are cool. My favorite animal is a dolphin.")

def get_user_input5():
    FavBookSeries = input("What is your favorite book series? ")
    print("The",FavBookSeries, "is awesome. My favroite book series is The Giver series.")


if __name__ == "__main__":
    main()
# def say_default_message():
#  print("Hi!")


# intro():
# say_default_message()
