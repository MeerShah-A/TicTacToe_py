import os, pickle

# Binary file to save game progress
filePath = "TicTacToeData.dat"

class game:
    def __init__(self):
        if os.path.exists(filePath): # if user chose to save the game, load the save
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
        else:   # load an initialised board
            self.board = [
                ["-", "-", "-"], 
                ["-", "-", "-"], 
                ["-", "-", "-"]
            ]
            self.x_count = 0 # number of x's on the board
            self.o_count = 0 # number of o's on the board

        self.validation_text =  "\nPlease type in a number between 0 and 3\n"
        self.value_error_text = "\nPlease type in an integer!\n"

    
    def clear_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)



    def display_board(self):
        for i in range(3):
            if i == 2: # don't print a horizontal line at the end
                print(" " + self.board[i][0], " | ", self.board[i][1], " | ", self.board[i][2], "\n")
            else: # print a horizontal line after
                print(" " + self.board[i][0], " | ", self.board[i][1], " | ", self.board[i][2], "\n", "-------------")


    def check_taken(self, x, y): # checks if the square chosen is occupied
        if self.board[x - 1][y - 1] != "-":
            return True
        else:
            return False

    
    def map_input_X(self): # takes row and column inputs, validates them and updates the board with x

        x = 0
        y = 0

        while True:
            try:
                while x < 1 or x > 3: # checks if row is in correct range
                    x = int(input("Type in the row (horizontal layer) number player X:\n"))
                    if x < 1 or x > 3:
                        self.clear_console()
                        self.display_board()                        
                        print(self.validation_text)
                    else:
                        break
            except ValueError: # ensures that values entered are integers
                self.clear_console()
                self.display_board()
                print(self.value_error_text)
            except EOFError: # if the user decides to quit the game
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
                input("Press enter to exit.")
                quit()
            else:
                break

        while True: # similar validation for column input
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
                input("Press enter to exit.")
                quit()
            else:
                break

        if self.check_taken(x, y): # checks if the users choice is taken
            self.clear_console()
            self.display_board()            
            print("\nPlease pick an empty cell.\n")
            self.map_input_X()
        else:
            self.board[x - 1][y - 1] = "x" # updates the board
            self.x_count += 1
            self.clear_console()
            self.display_board()


    def map_input_O(self): # same as map_input_X but for player O

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
                print("Press enter to exit.")
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
                input("Press enter to exit.")
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


    def check_full(self): # checks if the board is full
        full = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    full = False
                    break
            if full == False:
                break
        return full

    
    def check_winner_X(self): # checks if player x has won
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

        
    def check_winner_O(self): # checks if player o has won 
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


    def main(self): # the flow of the game
        print("You may press ctrl + D on linux or ctrl + z and enter on windows to exit at anytime ")
        self.display_board() # displays the board at save or initialised

        while True:
                if self.x_count > self.o_count: # if the number of x's is greater that the number of o's
                    self.map_input_O()
                    if self.check_winner_O():
                        print("\nPlayer O is the winner!\n") 
                        if not os.path.exists(filePath):
                            os.mknod(filePath) # makes file if not present to prevent errors
                        os.remove(filePath)
                        break
                if self.x_count == self.o_count: # if the number of x's is equal to the number of o's
                    self.map_input_X()
                    if self.check_winner_X():
                        print("\nPlayer X is the winner!\n")
                        input("Press enter to exit.")
                        if not os.path.exists(filePath):
                            os.mknod(filePath)
                        os.remove(filePath)
                        break
                    if self.check_full(): # check if board is full only after x as O cannot be last play
                        print("\nThe game is a tie!")
                        input("Press enter to exit.")
                        if not os.path.exists(filePath):
                            os.mknod(filePath)
                        os.remove(filePath)
                        break
                if self.x_count < self.o_count: # number of x's can never be less than number of o's
                    print("FATAL ERROR! Game file corrupted. \nRestart of game required.") # initialised board has no such problem
                    os.remove(filePath) # remove corrupted file
                    input("Press enter to exit.")
                    quit()


game1 = game() # make object
game1.main() # run the game