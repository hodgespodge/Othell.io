#Othello Code created by Samuel Hodges
#Gameboard class deals only with simulating the game.

import numpy as np

class Gameboard:

    def __init__(self,start_board = None):

        if start_board is None:
            self.board = np.full(shape=(8, 8),fill_value= '_',dtype = str)

            self.board[3][4] = 'B'
            self.board[4][3] = 'B'

            self.board[3][3] = 'W'
            self.board[4][4] = 'W'
        else:
            self.board = start_board

    def display_board(self):
        print("  A B C D E F G H")
        for y in range(0,8):
            print(y+1,"",end='')
            for x in range(0,8):
                print(self.board[x][y],"|",end='',sep = '')
            print("")

    #Does the square exist on the board?
    def _on_board(self,x,y):
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    #If the move is valid, return the tiles that would be flipped
    def valid_move(self,player,x,y):

        all_tiles_flipped = []

        #Is the space already occupied? Is the space on the board?
        if self.board[x][y] != '_' or not self._on_board(x,y):
            return all_tiles_flipped

        #Check every adjacent space
        for x_direc, y_direc in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:

            adjacent_x = x + x_direc
            adjacent_y = y + y_direc


            #A space is considered invalid if it would score no points.
            #Every adjacent space must be checked to determine if there exist any paths which may score points
            #There are 3 obvious conditions for which an adjacent space would be eliminated:

            if not self._on_board(adjacent_x,adjacent_y): #if the adjacent tile is off the board
                continue
            if self.board[adjacent_x][adjacent_y] == player: #if the adjacent tile is owned by the player
                continue
            if self.board[adjacent_x][adjacent_y] == '_': #if the adjacent tile is empty
                continue

            #at this point we know the adjacent tile must be owned by the enemy
            #now we continue in a straight line to see if the path connects to any pieces owned by the player

            tiles_flipped_in_direction = []

            while(True):

                tiles_flipped_in_direction.append((adjacent_x,adjacent_y))

                if not self._on_board(adjacent_x, adjacent_y): #If the straight line search is off board
                    break
                if self.board[adjacent_x][adjacent_y] == '_': #If the straight line search reached an empty tile
                    break
                if self.board[adjacent_x][adjacent_y] == player: #If the straight line search found a tile owned by player

                    #the flipped tiles are added to the list but more directions must be checked for flipped tiles
                    all_tiles_flipped.extend(tiles_flipped_in_direction)
                    break

                adjacent_x += x_direc
                adjacent_y += y_direc

        return all_tiles_flipped

    #check all tiles for valid moves
    #returns a list of tuples containing the x and y of available moves
    # and the number of tiles flipped for each move
    def available_moves(self,player):
        it = np.nditer(self.board, op_flags=['readwrite'], flags=['multi_index'])

        moves = []

        for tile in it:

            if tile != '_':
                continue

            x,y = it.multi_index[0],it.multi_index[1]

            changed_tiles = self.valid_move(player,x,y)

            if len(changed_tiles) > 0:
                moves.append((x,y,len(changed_tiles)))

        return moves

    #calculate and return the scores of each player as a dictionary
    def scores(self):
        score = {}
        B,W = 0,0
        for tile in np.nditer(self.board):
            if tile == '_':
                continue
            if tile == 'B':
                B += 1
            else:
                W += 1

        score['B'],score['W'] = B,W
        return score

    def _flip_tiles(self,player,changed_tiles):
        for tile in changed_tiles:

            self.board[tile[0]][tile[1]] = player

    def place_tile(self, player, x, y):
        changed_tiles = self.valid_move(player,x,y)

        if len(changed_tiles) < 0:
            print("ERROR: INVALID PLAY")
            return False

        self._flip_tiles(player,changed_tiles)
        self.board[x][y] = player
        return True
