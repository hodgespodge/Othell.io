from Gameboard import *
import copy

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
        other_color = {'W': 'B', 'B': 'W'}

        corners = [(0, 0), (7, 0), (0, 7), (7, 7)]

        tl_corner_buffer = [(1, 0), (0, 1), (1, 1)]
        tr_corner_buffer = [(6, 0), (7, 1), (6, 1)]
        bl_corner_buffer = [(0, 6), (1, 7), (1, 6)]
        br_corner_buffer = [(6, 7), (7, 6), (6, 6)]


        quality = 0

        if (move[0], move[1]) in corners:  # in corner is the best move
            return 10
        elif (move[0], move[1]) in tl_corner_buffer and board.board[0][0] == '_': #this would give the enemy the corner
            quality -= 10
        elif (move[0], move[1]) in tr_corner_buffer and board.board[7][0] == '_': #this would give the enemy the corner
            quality -= 10
        elif (move[0], move[1]) in bl_corner_buffer and board.board[0][7] == '_': #this would give the enemy the corner
            quality -= 10
        elif (move[0], move[1]) in br_corner_buffer and board.board[7][7] == '_': #this would give the enemy the corner
            quality -= 10

        # In order to view state of board after move, board must be simulated
        resulting_board = copy.deepcopy(board)
        resulting_board.place_tile(color,move[0],move[1])

        resulting_ai_moves = resulting_board.available_moves(player=color)
        resulting_enemy_moves = resulting_board.available_moves(player=other_color[color])
        quality -= len(resulting_enemy_moves)   #the more moves the enemy has available the worse the play
        quality += len(resulting_ai_moves)      #the more moves the ai has available the better the play

        return quality


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
