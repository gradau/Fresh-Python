#Number guessing game
import random

print('Welcome to the number guessing game!')
print('I am thinking of a number between 1 and 100')

secretNum = random.randint(1,100)

for numGuesses in range(1,10):
    print('Take a guess!')
    userGuess = int(input()) #make users guess an int to be comparable to our secretnum

