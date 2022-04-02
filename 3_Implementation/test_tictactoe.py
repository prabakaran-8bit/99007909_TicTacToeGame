import pytest
import tictactoe as t
import time

def test_start_game():
    assert t.Game.start_game()=="- | - | -     1 | 2 | 3\n" \
                                "- | - | -     4 | 5 | 6\n" \
                                "- | - | -     7 | 8 | 9\n" \
                                "\n" \
                                "X's chance." \
                                "\nEnter a number from 1-9 the number corresponds to the position given in the side display:"
def test_error_else():
    assert t.Game.error_else()=="You have met with an undefined error starting the game again"
def test_board():
    assert t.Game.board()=="\n" \
                           "- | - | -     1 | 2 | 3\n" \
                                "- | - | -     4 | 5 | 6\n" \
                                "- | - | -     7 | 8 | 9\n" \
                                "\n"

def test_turn_change():
    assert t.Game.turn_change()=="X's chance."
    assert t.Game.turn_change() == "O's chance."

def test_game_end_condition():
    assert t.Game.game_end_condition() == "X won."
    assert t.Game.game_end_condition() == "O won."
    assert t.Game.game_end_condition() == "Tie."

def test_end_winner_condition():
    assert t.Game.game_end_condition() == 1
    assert t.Game.game_end_condition() == 2
    assert t.Game.game_end_condition() == 3

def test_row_winning_condition():
    assert t.Game.row_winning_condition()==1
    assert t.Game.row_winning_condition() ==2
    assert t.Game.row_winning_condition()==3

def test_column_winning_condition():
    assert t.Game.column_winning_condition()==1
    assert t.Game.column_winning_condition() == 2
    assert t.Game.column_winning_condition() == 3

def test_diagonal_winning_condition():
    assert t.Game.diagonal_winning_condition() == 1
    assert t.Game.diagonal_winning_condition() == 2

def test_end_tie_condition():
    assert t.Game.end_tie_condition()==True
    assert t.Game.end_tie_condition() == False

def test_change_player():
    assert t.Game.change_player()== "X"
    assert t.Game.change_player()== "O"

def test_Startup():
    assert t.Start_up.__init__()==f"{time.strftime()}"\
           "Welcome to tic tac toe game\n"


















