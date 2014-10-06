# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui

secret_num = 0
remaining_guess = 0
lower_range = 0
higher_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_num, remaining_guess
    secret_num = random.randrange(lower_range, higher_range)
    remaining_guess = int(math.ceil(math.log(higher_range - lower_range + 1, 2)))
    print "Lets try  secret number, ranging from 0 to ", int(higher_range)
    print "You have", int(remaining_guess),"guesses remaining.\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global lower_range, higher_range
    lower_range = 0
    higher_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global lower_range, higher_range
    lower_range = 0
    higher_range = 1000
    new_game()

    
def input_guess(guess):
    # main game logic goes here	
    global remaining_guess
    remaining_guess =remaining_guess - 1
    guessed_num = int(guess)
    if int(remaining_guess) > 0 :
        print 'You guessed : ',guessed_num
        print 'You have ', remaining_guess, ' chances remaining.',
        if int(guess) == secret_num and higher_range==100:
            print '\nCorrect, You have WON :-)...\n'
            max_guess = math.ceil(math.log(higher_range+1,2))
            range100()
        
        elif int(guess) == secret_num and higher_range==1000:
            print '\nCorrect, You have WON :-)...\n'
            max_guess = math.ceil(math.log(higher_range+1,2))
            range1000()
        
        elif int(guess) < secret_num:
            print '\nTry Higher number\n'
            
        else:	
            print '\nTry Lower number\n'
    else:        
        if int(guess) == secret_num :
            if higher_range==100:
                print '\nCorrect, You have WON :-)...\n'
                max_guess = math.ceil(math.log(higher_range+1,2))
                range100()
            else:
                print '\nCorrect, You have WON :-)...\n'
                max_guess = math.ceil(math.log(higher_range+1,2))
                range1000()
        else:
            if higher_range==1000:
                print 'Sorry, all chances over, Unfortunately you loose.. :-('
                print 'The secret number was: ', secret_num
                max_guess = math.ceil(math.log(higher_range+1,2))
                range1000()
            else :
                print 'Sorry, all chances over, Unfortunately you loose.. :-('
                print 'The secret number was: ', int(secret_num)
                max_guess = math.ceil(math.log(higher_range+1,2))
                range100()    
      
    if remaining_guess <= 0:
        print 'Sorry, all chances over, Unfortunately you loose.. :-('
        new_game()


    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button('Range: 0 - 100', range100)
frame.add_button('Range: 0 - 1000', range1000)
frame.add_input('Enter Your guess', input_guess,200)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
