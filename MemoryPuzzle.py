import operator, sys, random, time

my_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
discovered = []
board_w = 4
board_h = 4

def check_if_ready(board):
    for x in range(0, board_w):
        for y in range(0, board_h):
            if board[x][y] == 0:
                return False
    
    return True

def init_board():
    my_new_board = []
    
    for x in range(0, board_w):
        new = []
        for y in range(0, board_h):
            new.append(0)
        my_new_board.append(new)
    
    while(not check_if_ready(my_new_board)):
        #print my_array
        fst_rand_loc_x = random.randrange(0, board_w)
        fst_rand_loc_y = random.randrange(0, board_h)
        sec_rand_loc_x = random.randrange(0, board_w)
        sec_rand_loc_y = random.randrange(0, board_h)
        
        if((my_new_board[fst_rand_loc_x][fst_rand_loc_y] == 0) and (my_new_board[sec_rand_loc_x][sec_rand_loc_y] == 0) and
            not(fst_rand_loc_x == sec_rand_loc_x and fst_rand_loc_y == sec_rand_loc_y)):
             
            letter = random.choice(my_array)
            my_new_board[fst_rand_loc_x][fst_rand_loc_y] = letter
            my_new_board[sec_rand_loc_x][sec_rand_loc_y] = letter
            my_array.remove(letter)
    
    return my_new_board


def print_board(board):
    for x in board:
        for y in enumerate(x):
            print(x[y[0]] + " ", end="")
        print("\n")

def print_stars(board):
    for x in board:
        for y in enumerate(x):
            print("* ", end="")
        print("\n")


def view_pos(my_new_board, pos_row, pos_col, temp):
    for x in enumerate(my_new_board):
        row = x[0]
        for y in enumerate(my_new_board[x[0]]):
            col = y[0]
            if((row == pos_row and col == pos_col) or  ([row, col] in discovered) or (temp[0] == row and temp[1] == col)):
                print(my_new_board[row][col] + " ", end=""),
            else:
                #print progress_board[row][col],
                print("* ", end="") 
        print("\n")
    
def loc_to_pos(loc):
    row = 0
    col = 0
    
    for i in range (0, loc):
        if(col == board_w-1):
            row += 1
            col = 0
        else:
            col += 1
    
    return row, col

def main():
    #beginning board
    start_time = time.time()
    my_new_board = init_board() #initilize new board
    winning_board = my_new_board  #set winning board to initilized board
    
    #print_board(my_new_board)
    print_stars(my_new_board)
    
    while len(discovered) < board_w*board_h: #loop as long as board hasn't been solved
        
        first_pos_row, first_pos_col = loc_to_pos(int(input("Enter first location to show: ")));
        
        view_pos(my_new_board, first_pos_row, first_pos_col, ["", ""])
        
        sec_pos_row, sec_pos_col = loc_to_pos(int(input("Enter second location to show: ")));
        
        view_pos(my_new_board, sec_pos_row, sec_pos_col, [first_pos_row, first_pos_col])
        
        if((my_new_board[first_pos_row][first_pos_col] == my_new_board[sec_pos_row][sec_pos_col]) and not(first_pos_row == sec_pos_row and first_pos_col == sec_pos_col)):
            print("Good!")
            discovered.append([first_pos_row, first_pos_col])
            discovered.append([sec_pos_row, sec_pos_col])
    
    duration = time.time() - start_time
    
    print("YOU WON")
    print("It took you " , duration , " seconds.")
    
if __name__ == "__main__":
    main()