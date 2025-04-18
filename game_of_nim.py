
from games import *
from alpha_beta_cutoff import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        moves = []
        for ix in range(len(board)):
            count = board[ix]
            if count != 0:
                for num in range(1, count + 1):
                    moves.append((ix, num))
                
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)
        
    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves
    
    def result(self, state, move):        
        row = move[0]
        number_to_remove = move[1]
        
        new_board = state.board.copy()
        new_board[row] -= number_to_remove
        
        new_moves = []
        for ix in range(len(new_board)):
                    count = new_board[ix]
                    if count != 0:
                        for num in range(1, count + 1):
                            new_moves.append((ix, num))

        new_to_move = ""
        if state.to_move == 'MAX':
            new_to_move = 'MIN'
        else:
            new_to_move = 'MAX'
        
        new_state = GameState(to_move=new_to_move, utility=0, board=new_board, moves=new_moves)
        new_utility = self.utility(new_state, new_state.to_move)
             
        return GameState(to_move=new_to_move, utility=new_utility, board=new_board, moves=new_moves)
    
    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if self.terminal_test(state):
            if player == state.to_move:
                return 1
            else:
                return -1
            
        return 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return all(count == 0 for count in state.board)

    def display(self, state):
        board = state.board
        print("board: ", board)
        
    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move
    
if __name__ == "__main__":
    nim = GameOfNim(board=[7, 5, 3, 1, 9]) # a much larger tree to search

    utility = nim.play_game(alpha_beta_cutoff_player, random_player)  # computer moves first

    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
    