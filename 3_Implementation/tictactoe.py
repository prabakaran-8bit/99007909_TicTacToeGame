"""TIC TAC TOE"""
import time
class Game():
    """Game class"""
    DISPLAY = ["-", "-", "-",
               "-", "-", "-",
               "-", "-", "-"]
    GAME_RUNNING = True
    WINNER = None
    GAME_PLAYER = "X"

    def error_else(self):
        """this method is when the error doest meet the exception case"""
        print("You have met with an undefined error starting the game again")
        self.start_game()

    def start_game(self):
        """this method is to start game"""

        self.board()
        try:
            while self.GAME_RUNNING:
                self.turn_change()

                self.game_end_condition()

                self.change_player()

            if self.WINNER in ("X","O"):
                print(self.WINNER + " won.")
            elif self.WINNER is None:
                print("Tie.")
        except Exception as e_start:
            print("you have an error startgame ", e_start)

    def board(self):
        """this method is to display the board"""

        print("\n")
        print(self.DISPLAY[0] + " | " + self.DISPLAY[1] + " | " + self.DISPLAY[2] + "    "
                                                                                    " 1 | 2 | 3")
        print(self.DISPLAY[3] + " | " + self.DISPLAY[4] + " | " + self.DISPLAY[5] + "    "
                                                                                    " 4 | 5 | 6")
        print(self.DISPLAY[6] + " | " + self.DISPLAY[7] + " | " + self.DISPLAY[8] + "   "
                                                                                    "  7 | 8 | 9")
        print("\n")

    def turn_change(self):
        """this method is to turn change"""

        print( self.GAME_PLAYER + "'s chance.")
        user_input = input("Enter a number from 1-9 the number corresponds to "
                           "the position given in the side display: ")

        input_validation = False
        try:
            while not input_validation:

                while user_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    user_input = input(
                        "Enter a number from 1-9 the number corresponds "
                        "to the position given in the side display: ")

                user_input = int(user_input) - 1

                if self.DISPLAY[user_input] == "-":
                    input_validation = True
                else:
                    print("You can't go there. Go again.")
        except Exception as e_turn:
            print("you have an error turn change", e_turn)


        self.DISPLAY[user_input] = self.GAME_PLAYER

        self.board()

    def game_end_condition(self):
        """this method is to end game"""

        self.end_winner_condition()
        self.end_tie_condition()

    def end_winner_condition(self):
        """this method is to find the winner"""
        r_winner = self.row_winning_condition()
        c_winner = self.column_winning_condition()
        d_winner = self.diagonal_winning_condition()
        try:
            if r_winner:
                self.WINNER = r_winner
            elif c_winner:
                self.WINNER = c_winner
            elif d_winner:
                self.WINNER = d_winner
            else:
                self.WINNER = None
        except Exception as e_win:
            print("You have an error  endwinner", e_win)


    def row_winning_condition(self):
        """this method is to find row winner"""
        r_1 = self.DISPLAY[0] == self.DISPLAY[1] == self.DISPLAY[2] != "-"
        r_2 = self.DISPLAY[3] == self.DISPLAY[4] == self.DISPLAY[5] != "-"
        r_3 = self.DISPLAY[6] == self.DISPLAY[7] == self.DISPLAY[8] != "-"
        try:
            if r_1 or r_2 or r_3:
                self.GAME_RUNNING = False
            if r_1:
                return self.DISPLAY[0]
            elif r_2:
                return self.DISPLAY[3]
            elif r_3:
                return self.DISPLAY[6]
            else:
                return None
        except Exception as e_row:
            print("you have an error in row winner ", e_row)
        else:
            print("error row winning")

    def column_winning_condition(self):
        """this method is to find column winner"""
        col_1 = self.DISPLAY[0] == self.DISPLAY[3] == self.DISPLAY[6] != "-"
        col_2 = self.DISPLAY[1] == self.DISPLAY[4] == self.DISPLAY[7] != "-"
        col_3 = self.DISPLAY[2] == self.DISPLAY[5] == self.DISPLAY[8] != "-"
        try:
            if col_1 or col_2 or col_3:
                self.GAME_RUNNING = False
            if col_1:
                return self.DISPLAY[0]
            elif col_2:
                return self.DISPLAY[1]
            elif col_3:
                return self.DISPLAY[2]
            else:
                return None
        except Exception as e_col:
            print("you have an error in column", e_col)
        else:
            print("columnwinning")

    def diagonal_winning_condition(self):
        """this method is to find diagonal winner"""
        diag_1 = self.DISPLAY[0] == self.DISPLAY[4] == self.DISPLAY[8] != "-"
        diag_2 = self.DISPLAY[2] == self.DISPLAY[4] == self.DISPLAY[6] != "-"
        try:
            if diag_1 or diag_2:
                self.GAME_RUNNING = False
            if diag_1:
                return self.DISPLAY[0]
            elif diag_2:
                return self.DISPLAY[2]
            else:
                return None
        except Exception as e_diag:
            print("you have an exception diagonal", e_diag)
        else:
            print("error in diagonal")

    def end_tie_condition(self):
        """this method is to find tie or not"""

        try:
            if "-" not in self.DISPLAY:
                self.GAME_RUNNING = False
                return True
            else:
                return False
        except Exception as e_tie:
            print("you have an error tie ", e_tie)
        else:
            print("error in tie condition")

    def change_player(self):
        """this method is used to change player"""
        try:
            if self.GAME_PLAYER == "X":
                self.GAME_PLAYER = "O"
            elif self.GAME_PLAYER == "O":
                self.GAME_PLAYER = "X"
        except Exception as e_change:
            print("you have the error change player", e_change)

class Startup(Game):
    """startup class"""

    def __init__(self):
        time_stamp=time.strftime("%H:%M %p")
        print(time_stamp)
        print("Welcome to tic tac toe game")
        game_g = Game()
        game_g.start_game()
        print("If you want to play further input Y/N :")
        replay=input()
        if replay=="Y":
            Startup()
        else:
            print("Game ended")

if __name__=='__main__':

    MAIN_GAME=Startup()
