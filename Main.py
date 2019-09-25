from Gameboard import *
from GreedyAI import *
import numpy as np

xmap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
xmapr = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
other_color = {'W':'B','B':'W'}

#dead_lock is flipped to True whenever a player cannot make a play.
#if the next player also cant play, the game is over.
dead_lock = False

def opponents_turn(color):
    global othello_board,dead_lock

    line = input().split()  # the input from the opponent
    if line[0] == color:
        if len(line) > 1:
            x, y = line[1], int(line[2])

            x = xmap[x]
            y = y - 1

            othello_board.place_tile(color, x, y)

            dead_lock = False
        else:
            dead_lock = True


    elif line[0] == 'C':
        None

    #Opponent claiming game over.
    elif line[0].isdigit():
        exit()

def ai_turn():
    global othello_board,Ai,dead_lock

    if othello_board.board_not_full():

        Ai_move = Ai.play_turn(othello_board)

        if Ai_move is not None:
            othello_board.place_tile(Ai.color, Ai_move[0], Ai_move[1])
            print(Ai.color, xmapr[Ai_move[0]], Ai_move[1] + 1)
            dead_lock == False
        elif dead_lock == True:
            print(othello_board.scores[0])
            exit()

        else:
            #no available moves... skipping turn
            print(Ai.color)
    else:
        #AI claiming game over. Printing score of black.
        print(othello_board.scores[0])
        exit()

def main(debug = False):

    othello_board = Gameboard()
    othello_board.display_board()

    line = input().split()
    ai_color = line[1]

    Ai = GreedyAI(color = ai_color)

    print("R",ai_color)

    while(True):

        if debug:
            othello_board.display_board()

        #Ai goes first
        if ai_color == 'B':
            ai_turn()
            if debug:
                othello_board.display_board()
            opponents_turn(other_color[ai_color])

        #opponent goes first
        else:
            opponents_turn(other_color[ai_color])
            if debug:
                othello_board.display_board()
            ai_turn()


if __name__ == "__main__":
    main(debug=True)