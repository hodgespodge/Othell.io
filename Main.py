from Gameboard import *
from GreedyAI import *
import numpy as np

def main(debug = False):

    xmap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    xmapr = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}

    othello_board = Gameboard()
    othello_board.display_board()

    line = input().split()
    color = line[1]

    Ai = GreedyAI(color = color)

    print("R",color)

    while(True):
        opponent_pass = False
        line = input().split()
        if line[0] == 'W' or line[0] =='B':
            if len(line) > 1:
                x,y = line[1],int(line[2])

                x = xmap[x]
                y = y - 1

                othello_board.place_tile(line[0],x,y)
            else:
                opponent_pass = True

        elif line[0] =='C':
            None

        elif line[0].isdigit():
            break

        othello_board.display_board()

        Ai_move = Ai.play_turn(othello_board)

        if Ai_move is not None:
            othello_board.place_tile(Ai.color,Ai_move[0],Ai_move[1])
            print(Ai.color, xmapr[Ai_move[0]],Ai_move[1]+ 1)
        elif opponent_pass == True:
            #Claim end of game
            print(othello_board.scores()['B'])
            break
        else:
            print(Ai.color)

        othello_board.display_board()

if __name__ == "__main__":
    main(debug=True)