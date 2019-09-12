from Gameboard import *

class GreedyAI:

    def __init__(self, color):
        self.color = color

    def play_turn(self,board):

        possible_moves = board.available_moves(player=self.color)

        if len(possible_moves) > 0:
            greedy_move = max(possible_moves,key=lambda item:item[2])
            return greedy_move[0],greedy_move[1]
        else:
            return None




