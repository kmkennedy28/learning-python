import random, sys

print('ROCK, PAPER, SCISSORS')

#number of wins, loses, & ties
wins = 0
losses = 0
ties = 0

#loop the game
while True:  
    #print stats
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    #loop to validate input or exit
    while True:  
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('>')
        if player_move == 'q':
            sys.exit()  # Quit game
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break #break the loop if input is r p or s
        print('Type one of r, p, s, or q.')

    # display players move
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    #randomize the computers move
    move_number = random.randint(1, 3)
    #print computer move
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # display results
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
