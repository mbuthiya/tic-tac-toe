the_board = {'tl':' ','tm':' ','tr':' ',
'ml':' ','mm':' ','mr':' ',
'bl':' ','bm':' ','br':' ',}

def define_board(board):
    # Defining each section of the board
    top_side = board['tl']+" | "+board['tm']+" | "+board['tr']
    middle_side = board['ml']+" | "+board['mm']+" | "+board['mr']
    bottom_side = board['bl']+" | "+board['bm']+" | "+board['br']
    # Getting the length of the board so that we can  create a border
    length = len(top_side)

    # Defining the board
    print(top_side)
    print("-" * length)
    print(middle_side)
    print("-" * length)
    print(bottom_side)

def check_match(board,turns):
    #  Checking rows
    check_top = board['tl'] == turns and board['tm'] == turns and  board['tr'] == turns
    check_middle = board['ml'] == turns and board['mm'] == turns and board['mr'] == turns
    check_bottom = board['bl'] == turns and board['bm'] == turns and board['br'] == turns

    #  Checking columns
    check_left = board['tl'] == turns and  board['ml'] == turns and board['bl'] == turns
    check_middle = board['tm'] == turns and  board['mm'] == turns and board['bm'] == turns
    check_right = board['tr'] == turns and  board['mr'] == turns and board['br'] == turns

    # checking diagonals
    front_diagonal = board['bl'] == turns and board['mm'] == turns and board['tr'] == turns
    back_diagonal =  board['tl'] == turns and board['mm'] == turns and board['br'] == turns

    if check_top or check_middle or check_bottom or check_left or check_middle or check_right or front_diagonal or back_diagonal:
        return True
    else:
        return False
# Function to get input
def get_input():
    while True:
        print("Enter your side" )
        inputs = input()
        # Check for the keywords
        if inputs == 'tl' or inputs == 'tm' or inputs == 'tr' or inputs == 'ml' or inputs == 'mm' or inputs == 'mr' or inputs == 'bl' or inputs == 'bm' or inputs == 'br':
            return inputs
            break
        else:
            continue
# Set turns and  maximum possible plays
turn = 'X'

for i in range(9):


    if check_match(the_board,turn):
        print(f"player {turn} has won")
        break
    else:
        user_input = get_input()
        the_board[user_input] = turn
        define_board(the_board)

        if turn == 'X':
            turn = 'O'
        else:
            turn == "X"
