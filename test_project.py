import pytest
from project import TicTacToe, HumanPlayer, RandomComputerPlayer, gameplay, play_again



def test_initial_board():
    game = TicTacToe()
    assert all(symbol == ' ' for symbol in game.board)
    assert game.current_winner is None

def test_make_move():
    game = TicTacToe()
    assert game.make_move(0, 'x')
    assert game.board[0] == 'x'
    assert game.current_winner is None
    assert game.make_move(1, 'o')
    assert game.board[1] == 'o'
    assert game.current_winner is None

def test_winner():
    game = TicTacToe()
    game.make_move(0, 'x')
    game.make_move(4, 'o')
    game.make_move(8, 'x')
    assert game.winner(0, 'x') is False
    assert game.winner(4, 'o') is False
    assert game.winner(8, 'x') is False




if __name__ == "__main__":
    pytest.main()