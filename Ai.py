from Gameboard import *

class GreedyAi():

    def play_turn(self,board,color):

        possible_moves = board.available_moves(player=color)

        if len(possible_moves) > 0:
            greedy_move = max(possible_moves,key=lambda item:len(item[2])) #The move with the most tiles flipped.
            return greedy_move[0],greedy_move[1]
        else:
            return None

class QualityAi():

    def quality_of_move(self,board,color,move):
        corners = [(0, 0), (7, 0), (0, 7), (7, 7)]
        corner_buffers = [(1, 0), (0, 1), (1, 1), (6, 0), (7, 1), (6, 1), (0, 6), (1, 7), (1, 6), (6, 7), (7, 6),
                          (6, 6)]

        if (move[0], move[1]) in corners:  # in corner is best move
            return 10
        #     best_move = move[0], move[1]
        #     break
        #
        # elif (move[0], move[1]) in corner_buffers:  # bad move

        return -1


    def play_turn(self,board,color):

        possible_moves = board.available_moves(player=color)
        if len(possible_moves) > 0:

            best_move = (possible_moves[0], self.quality_of_move(board, color, possible_moves[0])) #base case best move

            for move in possible_moves:

                quality = self.quality_of_move(board,color,move)

                if quality > best_move[1]:
                    best_move = (move,quality)


            return best_move[0][0],best_move[0][1]

        else:
            return None
