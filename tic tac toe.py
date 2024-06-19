board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#printing tic tac toe board
def print_board (board):
    print()
    for row in board:
        for column in row:
            print("| " + str(column) +" ", end = "")
        print("|\n")

def replace_number (input, xo):
    row = (input - 1)//3 #e.g. input = 6, 6//3 = 2 which will be in the wrong row| input = 5, 5//3 = 1 | input = 4, (4-1)//3 = 1
    column = input % 3 - 1     
    board[row][column] = xo

#winning the game   
def win (board): 
    #check win by the row
    for row in board:
        statement = all(box == row[0] and box != int for box in row ) #the all() function checks if all the elements in the list are the same (if same, returns true)
        if statement == True:
            return statement, row[0]

    #check win by the column
    check_col = []
    for column in range(0, 3):
        for row in range (0, 3):
            check_col.append(board[row][column])
        statement = all(box == check_col[0] and box != int for box in check_col)
        if statement == True:
            return statement, check_col[0]
        check_col.clear() #no need put else
        

    #check win by diagonal \
    check_diagonal_top = []
    for i in range(0, 3):
        check_diagonal_top.append(board[i][i]) #diagonal \ are all board[0][0] board[1][1], board[2][2]
    statement = all(box == check_diagonal_top[0] and box != int for box in check_diagonal_top)
    if statement == True:
        return statement, check_diagonal_top[0]
    check_diagonal_top.clear() #no need put else
    
    #check win by diagonal /
    check_diagonal_bot = []
    for i in range(0, 3):
        check_diagonal_bot.append(board[i][2 - i])    
    statement = all(box == check_diagonal_bot[0] and box != int for box in check_diagonal_bot)
    if statement == True:
        return statement, check_diagonal_bot[0]
    check_diagonal_bot.clear() #no need put else
        


#main game
game_won = True
print_board(board)

while game_won == True:
    #player 1's input
    p1_input = int(input("\nEnter your move (x): "))

    replace_number(p1_input, "x")
    print_board(board)
    win_bool = win(board) #returning more than 1 are in tuple

    #Game has been won
    if win_bool != None:
        win_check = win_bool[0]
        player = win_bool[1] # separating the tuple

        if win_check == True:
            if player == 'x':
                [print("Player 1 has won!")]
            elif player == 'o':
                [print("Player 2 has won!")]
            game_won = False
            break

    #Game has been tied, all boxes filled
    game_filled_list = []
    for row in board:
        for box in row:
                game_filled_list.append(isinstance(box, int)) #isinstance checks if the box is an int
    #game_filled = all(box is int for row in board for box in row )
    if all(check == False for check in game_filled_list) == True:
        print("The game is tied!")
        game_won = False

    #player 2's input
    p2_input = int(input("\nEnter your move (o): "))

    replace_number(p2_input, "o")
    print_board(board)
    win_bool = win(board) #returning more than 1 are in tuple
    
    #Game has been won
    if win_bool != None:
        win_check = win_bool[0]
        player = win_bool[1] # separating the tuple

        if win_check == True:
            if player == 'x':
                [print("Player 1 has won!")]
            elif player == 'o':
                [print("Player 2 has won!")]
            game_won = False