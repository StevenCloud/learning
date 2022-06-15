import random
import sys
guess = 0
the_number = random.randint(1, 10)

while(int(guess) != the_number):
    guess = input('Guess a number:')

print('Great you guessed it!')