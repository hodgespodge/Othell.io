from Gameboard import *
from Ai import *
import numpy as np

xmap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
        5: 'f', 6: 'g', 7: 'h'}

other_color = {'W': 'B', 'B': 'W'}

# dead_lock is flipped to True whenever a player cannot make a play.
# if the next player also cant play, the game is over.
dead_lock = False

def ai_turn(board, color, Ai,turn):
    global dead_lock

    if board.board_not_full():

        Ai_move = Ai.play_turn(board = board, color =color,turn = turn)

        if Ai_move is not None:
            print(color, xmap[Ai_move[0]], Ai_move[1] + 1)
            dead_lock = False
            board.place_tile(color, Ai_move[0], Ai_move[1])
            return board

        elif dead_lock == True:  # if there are no available moves and other player also had no available moves
            print(board.scores()['B'])
            return

        else:
            # no available moves... skipping turn
            print(color)
            dead_lock = True
            return board
    else:
        # AI claiming game over. Printing score of black.
        print(board.scores()['B'])
        return

def run_ai_duel(debug=False,black_player = GreedyAi,white_player = GreedyAi):

    results = {'turn':[0],'Black':[2],'White':[2]}

    board = Gameboard()
    if debug:
        board.display_board()

    print("R B")
    print("R W")

    turn = 1
    while (True):

        if debug:
            board.display_board()

        # Ai goes first
        board = ai_turn(board = board, color = 'B', Ai = black_player,turn = turn)
        if debug:
            board.display_board()
        if board == None:
            break

        results['turn'].append(turn)
        results['Black'].append(board.scores()['B'])
        results['White'].append(board.scores()['W'])

        turn += 1

        board = ai_turn(board = board,color = 'W', Ai = white_player,turn = turn)
        if board == None:
            break


        results['turn'].append(turn)
        results['Black'].append(board.scores()['B'])
        results['White'].append(board.scores()['W'])

        turn += 1

    return results
