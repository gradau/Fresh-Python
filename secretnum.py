#Number guessing game
import random

print('Welcome to the number guessing game!')
print('I am thinking of a number between 1 and 100')

secretNum = random.randint(1,100)

for numGuesses in range(1,10):
    print('Take a guess!')
    userGuess = int(input()) #make users guess an int to be comparable to our secretnum

    if userGuess < secretNum :  #user guessed too low
        print('Your guess is too low.')
    elif userGuess > secretNum :    #user guessed too high
        print('Your guess is too high')
    else:
        break #user guessed correctly

if userGuess == secretNum:
    print('You guessed correctly! You guessed the number in ' + str(numGuesses) + ' guesses.')
else:
    print('Sorry, the number I was thinking of was ' + str(secretNum) +'.')