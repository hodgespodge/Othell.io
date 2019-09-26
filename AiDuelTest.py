from Gameboard import *
from GreedyAI import *
import numpy as np

xmap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
        5: 'f', 6: 'g', 7: 'h'}

other_color = {'W': 'B', 'B': 'W'}

# dead_lock is flipped to True whenever a player cannot make a play.
# if the next player also cant play, the game is over.
dead_lock = False

def ai_turn(othello_board, color, Ai):
    global dead_lock

    if othello_board.board_not_full():

        Ai_move = Ai.play_turn(othello_board, color)

        if Ai_move is not None:
            print(color, xmap[Ai_move[0]], Ai_move[1] + 1)
            dead_lock = False
            othello_board.place_tile(color, Ai_move[0], Ai_move[1])
            return othello_board

        elif dead_lock == True:  # if there are no available moves and other player also had no available moves
            print(othello_board.scores()['B'])
            exit()

        else:
            # no available moves... skipping turn
            print(color)
            dead_lock = True
            return othello_board
    else:
        # AI claiming game over. Printing score of black.
        print(othello_board.scores()['B'])
        exit()

def main(debug=False):

    othello_board = Gameboard()
    if debug:
        othello_board.display_board()

    ai_1_color = 'B'
    ai_2_color = 'W'

    ai_1 = GreedyAi()
    ai_2 = GreedyAi()

    print("R", ai_1_color)
    print("R", ai_2_color)

    while (True):

        if debug:
            othello_board.display_board()

        # Ai goes first
        othello_board = ai_turn(othello_board, ai_1_color, ai_1)
        if debug:
            othello_board.display_board()
        othello_board = ai_turn(othello_board,ai_2_color, ai_2)

if __name__ == "__main__":
    main(debug=True)