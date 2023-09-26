
import time
import random

def main():
    while True:
        x_player = HumanPlayer('x')
        o_player = RandomComputerPlayer('o')
        t = TicTacToe()
        tictactoe_game = gameplay(t, x_player, o_player, print_game=True)
        tictactoe_game
        if play_again():
            continue
        else:
            break


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None


    def print_board (self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_number_board():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, symbol):
        if self.board[square] == ' ':
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            return True
        return False


    def winner(self, square, symbol):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1) *3 ]
        if all(spot == symbol for spot in row):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == symbol for spot in column]):
            return True

        if square % 2  == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all ([spot == symbol for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all ([spot == symbol for spot in diagonal2]):
                return True
        return False


    def available_moves(self):
        return[i for i , spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')




def gameplay(game, x_player, o_player, print_game=True):
        if print_game:
            game.print_number_board()

        symbol = 'x'
        while game.empty_squares():
            if symbol == 'o':
                square = o_player.get_move_player(game)
            else:
                square = x_player.get_move_player(game)

            if game.make_move(square, symbol):
                if print_game:
                    print(symbol + ' makes a move to square {}'.format(square))
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(symbol + 'wins!')
                    return symbol

                symbol = 'o' if symbol == 'x' else 'x'

            time.sleep(0.8)
        if print_game:
            print('It\'s a tie!')

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

class player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move_player(self,game):
        pass

class RandomComputerPlayer(player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move_player(self,game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(player):
    def __init__(self,symbol):
        super().__init__(symbol)

    def get_move_player(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.symbol + '\'s turn. INput move(0-8):')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

if __name__ == '__main__':
    main()

