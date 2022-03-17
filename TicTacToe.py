import os, pickle

filePath = "TicTacToeData.dat"

class game:
    def __init__(self):
        if os.path.exists(filePath):
            file2 = open(filePath, "rb")
            self.board = pickle.load(file2)
            self.x_count = 0
            self.o_count = 0
            for j in range(3):
                for i in self.board[j]:
                    if i == "x":
                        self.x_count += 1
                    elif i == "o":
                        self.o_count += 1
        else:    
            self.board = [
                ["-", "-", "-"], 
                ["-", "-", "-"], 
                ["-", "-", "-"]
            ]
            self.x_count = 0
            self.o_count = 0

        self.validation_text =  "\nPlease type in a number between 0 and 3\n"
        self.value_error_text = "\nPlease type in an integer!\n"

    
    def clear_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)



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
                        self.clear_console()
                        self.display_board()                        
                        print(self.validation_text)
                    else:
                        break
            except ValueError:
                self.clear_console()
                self.display_board()
                print(self.value_error_text)
            except EOFError:
                while True:
                    save = input("Would you like to save(Y/n)? ")
                    if save.lower() == "y":
                        file1 = open(filePath, "wb")
                        pickle.dump(self.board, file1)
                        break
                    elif save.lower() == "n":
                        os.remove(filePath)
                        break
                    else:
                        print("Please type in y or n.")
                quit()
            else:
                break

        while True:
            try:
                while y < 1 or y > 3:        
                    y = int(input("Type in the column (vertical layer) number player X:\n"))
                    if y < 1 or y > 3:
                        self.clear_console()
                        self.display_board()                        
                        print(self.validation_text)
                    else:
                        break
            except ValueError:
                self.clear_console()
                self.display_board()
                print(self.value_error_text)
            except EOFError:
                quit()
            else:
                break

        if self.check_taken(x, y):
            self.clear_console()
            self.display_board()            
            print("\nPlease pick an empty cell.\n")
            self.map_input_X()
        else:
            self.board[x - 1][y - 1] = "x"
            self.x_count += 1
            self.clear_console()
            self.display_board()


    def map_input_O(self):

        x = 0
        y = 0

        while True:
            try:
                while x < 1 or x > 3:
                    x = int(input("Type in the row (horizontal layer) number player O:\n"))
                    if x < 1 or x > 3:
                        self.clear_console()
                        self.display_board()                        
                        print(self.validation_text)
                    else:
                        break
            except ValueError:
                self.clear_console()
                self.display_board()
                print(self.value_error_text)
            except EOFError:
                while True:
                    save = input("Would you like to save(Y/n)? ")
                    if save.lower() == "y":
                        file1 = open(filePath, "wb")
                        pickle.dump(self.board, file1)
                        break
                    elif save.lower() == "n":
                        os.remove(filePath)
                        break
                    else:
                        print("Please type in y or n.")
                quit()
            else:
                break


        while True:
            try:
                while y < 1 or y > 3:        
                    y = int(input("Type in the column (vertical layer) number player O:\n"))
                    if y < 1 or y > 3:
                        self.clear_console()
                        self.display_board()
                        print(self.validation_text)
                    else:
                        break
            except ValueError:
                self.clear_console()
                self.display_board()
                print(self.value_error_text)
            except EOFError:
                quit()
            else:
                break

        if self.check_taken(x, y):
            self.clear_console()
            self.display_board()
            print("\nPlease pick an empty cell.\n")
            self.map_input_O()
        else:
            self.board[x - 1][y - 1] = "o"
            self.o_count += 1
            self.clear_console()
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
                if self.x_count > self.o_count:
                    self.map_input_O()
                    self.check_winner_O()
                    if self.check_winner_O():
                        print("\nPlayer O is the winner!\n")
                        os.mknod("TicTacToeData.dat")
                        if not os.path.exists(filePath):
                            os.mknod(filePath)
                        os.remove(filePath)
                        break
                if self.x_count == self.o_count:
                    self.map_input_X()
                    self.check_winner_X()
                    if self.check_winner_X():
                        print("\nPlayer X is the winner!\n")
                        if not os.path.exists(filePath):
                            os.mknod(filePath)
                        os.remove(filePath)
                        break
                    if self.check_full():
                        print("\nThe game is a tie!")
                        if not os.path.exists(filePath):
                            os.mknod(filePath)
                        os.remove(filePath)
                        break

game1 = game()
game1.main()