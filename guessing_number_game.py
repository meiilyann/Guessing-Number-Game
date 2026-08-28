import random

start = 1

print("Welcome to the guessing number game !")
print("I am thinking of a number between 1 and 100")
print("Good luck to find it !")
number = random.randint(1, 100)
while start == 1:
    guess = int(input("Please guess a number between 1 and 100: "))
    if guess == number:
        print("You guessed correctly")
        start = 0
    elif guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
