import logging
import random
#normal configuration
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

#ignore the logged debug messages
logging.disable(logging.CRITICAL)

logging.debug('Start of program')

#holds the user's coin toss guess
guess = ''

#get users guess, must be heads or tails
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

#randomize an int to be heads or tails
toss = random.randint(0, 1)

#assign 0 as tails, 1 as heads
if toss == 0:
    result = 'tails'
elif toss == 1:
    result = 'heads'

logging.debug('Results = ' + result + ' guess = ' + guess)

#compare the result to the user's guess
if result == guess:
    logging.debug('Results = guess')
    print('You got it!')
else:
    #if first guess is wrong let user guess again
    logging.debug('Results != guess')
    print('Nope! Guess again!')
    guess = input()
    if result == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
