from Gameboard import *
from Ai import *
import numpy as np

xmap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
other_color = {'W':'B','B':'W'}

#dead_lock is flipped to True whenever a player cannot make a play.
#if the next player also cant play, the game is over.
dead_lock = False

def opponents_turn(othello_board,color):
    global dead_lock

    line = input().split()  # the input from the opponent
    if line[0] == color:
        if len(line) > 1:
            x, y = line[1], int(line[2])

            x = xmap[x]
            y = y - 1

            dead_lock = False
            othello_board.place_tile(color, x, y)
            return othello_board

        else:
            dead_lock = True
            return othello_board


    elif line[0] == 'C':
        opponents_turn(othello_board,color)

    #Opponent claiming game over.
    elif line[0].isdigit():
        exit()

def ai_turn(othello_board,color,Ai):
    global dead_lock

    if othello_board.board_not_full():

        Ai_move = Ai.play_turn(othello_board,color)

        if Ai_move is not None:
            print(color, xmap[Ai_move[0]], Ai_move[1] + 1)
            dead_lock = False
            othello_board.place_tile(color, Ai_move[0], Ai_move[1])
            return othello_board

        elif dead_lock == True:#if there are no available moves and other player also had no available moves
            print(othello_board.scores()['B'])
            exit()

        else:
            #no available moves... skipping turn
            print(color)
            dead_lock = True
            return othello_board
    else:
        #AI claiming game over. Printing score of black.
        print(othello_board.scores()['B'])
        exit()

def main(debug = False):

    othello_board = Gameboard()
    if debug:
        othello_board.display_board()

    line = input().split()
    ai_color = line[1]

    Ai = GreedyAi()

    print("R",ai_color)

    while(True):

        if debug:
            othello_board.display_board()

        #Ai goes first
        if ai_color == 'B':
            othello_board = ai_turn(othello_board,ai_color,Ai)
            if debug:
                othello_board.display_board()
            othello_board = opponents_turn(othello_board, other_color[ai_color])

        #opponent goes first
        else:
            othello_board = opponents_turn(othello_board, other_color[ai_color])
            if debug:
                othello_board.display_board()
            othello_board = ai_turn(othello_board,ai_color,Ai)

if __name__ == "__main__":
    main(debug=True)