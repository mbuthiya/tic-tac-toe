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
