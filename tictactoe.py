class game:


    def __init__(self):
        self.board = [
            ["-", "-", "-"], 
            ["-", "-", "-"], 
            ["-", "-", "-"]
        ]
        self.validation_text =  "\nPlease type in a number between 0 and 3\n"
        self.value_error_text = "\nPlease type in an integer!\n"


    def display_board(self):
        for i in range(3):
            print(self.board[i][0], "  ", self.board[i][1], "  ", self.board[i][2], "\n")


    def check_taken(self, x, y):
        if self.board[x - 1][y - 1] != "-":
            return True
        else:
            return False

    
    def map_input_X(self):

        x = 0
        y = 0

        while True:
            try:
                while x < 1 or x > 3:
                    x = int(input("Type in the row (horizontal layer) number player X:\n"))
                    if x < 1 or x > 3:
                        print(self.validation_text)
                        self.display_board()
                    else:
                        break
            except ValueError:
                print(self.value_error_text)
            except EOFError:
                quit()
            else:
                break

        while True:
            try:
                while y < 1 or y > 3:        
                    y = int(input("Type in the column (vertical layer) number player X:\n"))
                    if y < 1 or y > 3:
                        print(self.validation_text)
                        self.display_board()
                    else:
                        break
            except ValueError:
                print(self.value_error_text)
                self.display_board()
            except EOFError:
                quit()
            else:
                break

        if self.check_taken(x, y):
            print("\nPlease pick an empty cell.\n")
            self.display_board()
            self.map_input_X()
        else:
            self.board[x - 1][y - 1] = "x"
            self.display_board()


    def map_input_O(self):

        x = 0
        y = 0

        while True:
            try:
                while x < 1 or x > 3:
                    x = int(input("Type in the row (horizontal layer) number player O:\n"))
                    if x < 1 or x > 3:
                        print(self.validation_text)
                        self.display_board()
                    else:
                        break
            except ValueError:
                print(self.value_error_text)
            except EOFError:
                quit()
            else:
                break


        while True:
            try:
                while y < 1 or y > 3:        
                    y = int(input("Type in the column (vertical layer) number player O:\n"))
                    if y < 1 or y > 3:
                        print(self.validation_text)
                        self.display_board()
                    else:
                        break
            except ValueError:
                print(self.value_error_text)
                self.display_board()
            except EOFError:
                quit()
            else:
                break

        if self.check_taken(x, y):
            print("\nPlease pick an empty cell.\n")
            self.display_board()
            self.map_input_O()
        else:
            self.board[x - 1][y - 1] = "o"
            self.display_board()


    def check_full(self):
        full = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    full = False
                    break
            if full == False:
                break
        return full

    
    def check_winner_X(self):
        for i in range(3):
            if self.board[i][0] == "x" and self.board[i][1] == "x" and self.board[i][2] == "x":
                return True
        
        for i in range(3):
            if self.board[0][i] == "x" and self.board[1][i] == "x" and self.board[2][i] == "x":
                return True

        if self.board[0][0] == "x" and self.board[1][1] == "x" and self.board[2][2] == "x":
            return True
        
        if self.board[0][2] == "x" and self.board[1][1] == "x" and self.board[2][0] == "x":
            return True

        
    def check_winner_O(self):
        for i in range(3):
            if self.board[i][0] == "o" and self.board[i][1] == "o" and self.board[i][2] == "o":
                return True
        
        for i in range(3):
            if self.board[0][i] == "o" and self.board[1][i] == "o" and self.board[2][i] == "o":
                return True

        if self.board[0][0] == "o" and self.board[1][1] == "o" and self.board[2][2] == "o":
            return True
        
        if self.board[0][2] == "o" and self.board[1][1] == "o" and self.board[2][0] == "o":
            return True


    def main(self):
        print("You may press ctrl + D to exit at anytime ")
        self.display_board()
        while True:
            self.map_input_X()
            self.check_winner_X()
            if self.check_winner_X():
                print("\nPlayer X is the winner!\n")
                break
            if self.check_full():
                print("\nThe game is a Tie!\n")
                break
            self.map_input_O()
            self.check_winner_O()
            if self.check_winner_O():
                print("\nPlayer O is the winner!\n")
                break


game1 = game()
game1.main()
