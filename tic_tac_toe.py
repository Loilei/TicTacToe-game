import sys
import random
import time


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    
    grid_rowA = [ '.','.','.' ]
    grid_rowB = [ '.','.','.' ]
    grid_rowC = [ '.','.','.' ]

    board = [ grid_rowA, grid_rowB, grid_rowC ]
    return board, grid_rowA, grid_rowB, grid_rowC


def get_move(board, valid_coordinate_input):
    
    imput_successful = True 

    while imput_successful:
        coordinates_input = input("Please insert a coordinate or 'quit' if you want to exit the game: ")
        if coordinates_input == "quit":
            sys.exit(0)
        if coordinates_input.upper() in valid_coordinate_input.keys() and board[valid_coordinate_input[coordinates_input.upper()][0]][valid_coordinate_input[coordinates_input.upper()][1]] == ".":
            row, col = valid_coordinate_input[coordinates_input.upper()]
            del valid_coordinate_input[coordinates_input.upper()]
            return row, col, valid_coordinate_input
        else:
            print()
            print(" " + coordinates_input + " is NOT a Valid Location Choice. Valid Choices are as follows: ")
            print(" " + str(valid_coordinate_input.keys()))
            print()


def is_winning_row(board, player):
    for i in board:
        if i.count(player) == 2 and i.count(".") == 1:
            return True
            
    return False


def column_generator(L,player):
    for i in L:
        if i != player:
            col = L.index(i)
            return col


def winning_row(board, player):
    for i in board:
            if i.count(player) == 2:
                row = board.index(i)
                col = column_generator(i,player)
                x = row, col
                return x


def is_winning_col_diag(board, player):
    rowA,rowB,rowC = board
    new_board = rowA+rowB+rowC
    cond1 = (new_board[0] == new_board[3] == player and new_board[6] == ".") or (new_board[3] == new_board[6] == player and new_board[0] == ".") or (new_board[0] == new_board[6] == player and new_board[3] == ".")
    cond2 = (new_board[1] == new_board[4] == player and new_board[7] == ".") or (new_board[4] == new_board[7] == player and new_board[1] == ".") or (new_board[1] == new_board[7] == player and new_board[4] == ".")
    cond3 = (new_board[2] == new_board[5] == player and new_board[8] == ".") or (new_board[5] == new_board[8] == player and new_board[2] == ".") or (new_board[2] == new_board[8] == player and new_board[5] == ".")
    diag1 = (new_board[0] == new_board[4] == player and new_board[8] == ".") or (new_board[4] == new_board[8] == player and new_board[0] == ".") or (new_board[0] == new_board[8] == player and new_board[4] == ".")
    diag2 = (new_board[2] == new_board[4] == player and new_board[6] == ".") or (new_board[4] == new_board[6] == player and new_board[2] == ".") or (new_board[2] == new_board[6] == player and new_board[4] == ".")
    if cond1 or cond2 or cond3 or diag1 or diag2 == True:
        return True
    else:
        return False


def winning_col_diag(board,player):
    rowA,rowB,rowC = board
    new_board = rowA+rowB+rowC
    coordinate_dict = {"A0":(0,0), "A1":(0,1), "A2":(0,2), "B0":(1,0), "B1":(1,1), "B2":(1,2), "C0":(2,0), "C1":(2,1), "C2":(2,2)}
    cond1 = new_board[0] == new_board[3] == player
    cond2 = new_board[3] == new_board[6] == player
    cond3 = new_board[0] == new_board[6] == player
    cond4 = new_board[1] == new_board[4] == player
    cond5 = new_board[4] == new_board[7] == player
    cond6 = new_board[1] == new_board[7] == player
    cond7 = new_board[2] == new_board[5] == player
    cond8 = new_board[5] == new_board[8] == player
    cond9 = new_board[2] == new_board[8] == player
    diag1 = new_board[0] == new_board[4] == player
    diag2 = new_board[4] == new_board[8] == player
    diag3 = new_board[0] == new_board[8] == player
    diag4 = new_board[2] == new_board[4] == player
    diag5 = new_board[4] == new_board[6] == player
    diag6 = new_board[2] == new_board[6] == player

    if cond1 == True:
        ai_input = "C0"
        row, col = coordinate_dict["C0"]
        return ai_input, row, col
    elif cond2 == True:
        ai_input = "A0"
        row, col = coordinate_dict["A0"]
        return ai_input, row, col
    elif cond3 == True:
        ai_input = "B0"
        row, col = coordinate_dict["B0"]
        return ai_input, row, col
    elif cond4 == True:
        ai_input = "C1"
        row, col = coordinate_dict["C1"]
        return ai_input, row, col
    elif cond5 == True:
        ai_input = "A1"
        row, col = coordinate_dict["A1"]
        return ai_input, row, col
    elif cond6 == True:
        ai_input = "B1"
        row, col = coordinate_dict["B1"]
        return ai_input, row, col
    elif cond7 == True:
        ai_input = "C2"
        row, col = coordinate_dict["C2"]
        return ai_input, row, col
    elif cond8 == True:
        ai_input = "A2"
        row, col = coordinate_dict["A2"]
        return ai_input, row, col
    elif cond9 == True:
        ai_input = "B2"
        row, col = coordinate_dict["B2"]
        return ai_input, row, col
    elif diag1 == True:
        ai_input = "C2"
        row, col = coordinate_dict["C2"]
        return ai_input, row, col
    elif diag2 == True:
        ai_input = "A0"
        row, col = coordinate_dict["A0"]
        return ai_input, row, col
    elif diag3 == True:
        ai_input = "B1"
        row, col = coordinate_dict["B1"]
        return ai_input, row, col
    elif diag4 == True:
        ai_input = "C0"
        row, col = coordinate_dict["C0"]
        return ai_input, row, col
    elif diag5 == True:
        ai_input = "A2"
        row, col = coordinate_dict["A2"]
        return ai_input, row, col
    elif diag6 == True:
        ai_input = "B1"
        row, col = coordinate_dict["B1"]
        return ai_input, row, col


def get_ai_move(board, valid_coordinate_input, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    coord_list_keys = list(valid_coordinate_input.keys())
    coord_list_values = list(valid_coordinate_input.values())
    if is_winning_row(board, player) == True:
        ai_input_coord = winning_row(board,player)
        coord_position = coord_list_values.index(ai_input_coord)
        row, col = ai_input_coord
    elif is_winning_col_diag(board,player) == True:
        ai_input, row, col = winning_col_diag(board,player)
    else:
        ai_input = random.choice(list(valid_coordinate_input.keys()))
        row, col = valid_coordinate_input[ai_input]
        del valid_coordinate_input[ai_input]
    return row, col, valid_coordinate_input


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    
    board[row][col] = player
    grid_rowA = board[0]
    grid_rowB = board[1]
    grid_rowC = board[2]
    print_board(grid_rowA, grid_rowB, grid_rowC)

    return board, grid_rowA, grid_rowB, grid_rowC    


def has_won(board, player):
    """Returns True if player has won the game."""
    
    if board[0][0] == board[0][1] == board[0][2] == player or board[1][0] == board[1][1] == board[1][2] == player or board[2][0] == board[2][1] == board[2][2] == player or board[0][0] == board[1][0] == board[2][0] == player or board[0][1] == board[1][1] == board[2][1] == player or board[0][2] == board[1][2] == board[2][2] == player or board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    else:
        return False


def is_full(board):
    """Returns True if board is full."""
    if any("." in sublist for sublist in board):
        return False
    else:
        return True


def print_board(grid_rowA, grid_rowB, grid_rowC):
    """Prints a 3-by-3 board on the screen with borders."""
    print("\n")
    print("\t 0\t1     2")
    print(" ")
    print("\t     |     |")
    print(" " + "A" + "\t" + " " + str(grid_rowA[0]) + "   |" + "  " + str(grid_rowA[1]) + "  |" + "  " + str(grid_rowA[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print(" " + "B" + "\t" + " " + str(grid_rowB[0]) + "   |" + "  " + str(grid_rowB[1]) + "  |" + "  " + str(grid_rowB[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print(" " + "C" + "\t" + " " + str(grid_rowC[0]) + "   |" + "  " + str(grid_rowC[1]) + "  |" + "  " + str(grid_rowC[2]))
    print("\t     |     |")
    print("\n")


def print_result(winner, player):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == True and player == "X":
        print("X has won!")
    elif winner == True and player == "O":
        print("O has won!")
    else:
        print("It's a tie!")        


def change_player(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player


def tictactoe_game_1():
    player = "X"
    board, grid_rowA, grid_rowB, grid_rowC = init_board()
    print_board(grid_rowA, grid_rowB, grid_rowC)
    valid_coordinate_input = {"A0": (0,0), "A1":(0,1), "A2":(0,2), "B0":(1,0), "B1":(1,1), "B2":(1,2), "C0": (2,0), "C1":(2,1), "C2":(2,2)}
    while is_full(board) == False:
        row, col, valid_coordinate_input = get_move(board, valid_coordinate_input) #tuple of coordinates (row, col)
        board, grid_rowA, grid_rowB, grid_rowC = mark(board, player, row, col)
        if has_won(board, player) == True:
            break
        player = change_player(player)

    winner = has_won(board, player)
    print_result(winner, player) 


def tictactoe_game_2a():
    player = "X"
    board, grid_rowA, grid_rowB, grid_rowC = init_board()
    print_board(grid_rowA, grid_rowB, grid_rowC)
    valid_coordinate_input = {"A0": (0,0), "A1":(0,1), "A2":(0,2), "B0":(1,0), "B1":(1,1), "B2":(1,2), "C0": (2,0), "C1":(2,1), "C2":(2,2)}
    while is_full(board) == False:
        if player == "X":
            time.sleep(1)
            row, col, valid_coordinate_input = get_ai_move(board, valid_coordinate_input, player) #tuple of coordinates (row, col)
        else:
            row, col, valid_coordinate_input = get_move(board, valid_coordinate_input)    
        board, grid_rowA, grid_rowB, grid_rowC = mark(board, player, row, col)
        if has_won(board, player) == True:
            break
        player = change_player(player)

    winner = has_won(board, player)
    print_result(winner, player)  


def tictactoe_game_2b():
    player = "X"
    board, grid_rowA, grid_rowB, grid_rowC = init_board()
    print_board(grid_rowA, grid_rowB, grid_rowC)
    valid_coordinate_input = {"A0": (0,0), "A1":(0,1), "A2":(0,2), "B0":(1,0), "B1":(1,1), "B2":(1,2), "C0": (2,0), "C1":(2,1), "C2":(2,2)}
    while is_full(board) == False:
        if player == "X":
            row, col, valid_coordinate_input = get_move(board, valid_coordinate_input) #tuple of coordinates (row, col)
        else:
            time.sleep(1)
            row, col, valid_coordinate_input = get_ai_move(board, valid_coordinate_input, player)    
        board, grid_rowA, grid_rowB, grid_rowC = mark(board, player, row, col)
        if has_won(board, player) == True:
            break
        player = change_player(player)

    winner = has_won(board, player)
    print_result(winner, player)


def tictactoe_game_3():
    player = "X"
    board, grid_rowA, grid_rowB, grid_rowC = init_board()
    print_board(grid_rowA, grid_rowB, grid_rowC)
    valid_coordinate_input = {"A0": (0,0), "A1":(0,1), "A2":(0,2), "B0":(1,0), "B1":(1,1), "B2":(1,2), "C0": (2,0), "C1":(2,1), "C2":(2,2)}
    while is_full(board) == False:
        time.sleep(1)
        row, col, valid_coordinate_input = get_ai_move(board, valid_coordinate_input, player) #tuple of coordinates (row, col)
        board, grid_rowA, grid_rowB, grid_rowC = mark(board, player, row, col)
        if has_won(board, player) == True:
            break
        player = change_player(player)

    winner = has_won(board, player)
    print_result(winner, player) 


def play_again():
    again = input("Do you want to play again? Yes/No : ")
    if again.lower() == "yes":
        main_menu()
    elif again.lower() == "no":
        sys.exit(0)


def main_menu():
    print("**** WELCOME TO TIC-TAC-TOE!****")
    game_mode = input("""Please select game mode:
    A: HUMAN-HUMAN
    B: AI-HUMAN
    C: HUMAN-AI
    D: AI-AI
     """)
    game_on = True 
    while game_on == True:  
        if game_mode == "a" or game_mode == "A":
            tictactoe_game_1()
            break
        elif game_mode == "b" or game_mode == "B":
            tictactoe_game_2a()
            break
        elif game_mode == "c" or game_mode == "C":
            tictactoe_game_2b()
            break
        elif game_mode == "d" or game_mode == "D":
            tictactoe_game_3()
            break
        else:
            print("Not a valid input, please try again! ")

    play_again()
    
main_menu()

