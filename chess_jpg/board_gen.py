from PIL import Image
from phichess import Board

def generate_board(board):
    im = Image.open('chess_pieces/chessboard.jpg', 'r')
    width = 800; height = 700;
    im = im.resize((width, height), Image.ANTIALIAS)

    # black pieces: 
    BR = Image.open('chess_pieces/BR.png', 'r')
    BR = BR.resize((80,80), Image.ANTIALIAS)
    BN = Image.open('chess_pieces/BN.png', 'r')
    BN = BN.resize((80,80), Image.ANTIALIAS)
    BB = Image.open('chess_pieces/BB.png', 'r')
    BB = BB.resize((80,80), Image.ANTIALIAS)
    BK = Image.open('chess_pieces/BK.png', 'r')
    BK = BK.resize((80,80), Image.ANTIALIAS)
    BQ = Image.open('chess_pieces/BQ.png', 'r')
    BQ = BQ.resize((80,80), Image.ANTIALIAS)
    BP = Image.open('chess_pieces/BP.png', 'r')
    BP = BP.resize((80,80), Image.ANTIALIAS)
    # white pieces:
    WR = Image.open('chess_pieces/WR.png', 'r')
    WR = WR.resize((80,80), Image.ANTIALIAS)
    WN = Image.open('chess_pieces/WN.png', 'r')
    WN = WN.resize((80,80), Image.ANTIALIAS)
    WB = Image.open('chess_pieces/WB.png', 'r')
    WB = WB.resize((80,80), Image.ANTIALIAS)
    WK = Image.open('chess_pieces/WK.png', 'r')
    WK = WK.resize((80,80), Image.ANTIALIAS)
    WQ = Image.open('chess_pieces/WQ.png', 'r')
    WQ = WQ.resize((80,80), Image.ANTIALIAS)
    WP = Image.open('chess_pieces/WP.png', 'r')
    WP = WP.resize((80,80), Image.ANTIALIAS)
    
    A = round(width * 0.013) 
    B = round(width * .1383) 
    C = round(width * .2633) 
    D = round(width * .3883) 
    E = round(width * .5117) 
    F = round(width * .635) 
    G = round(width * .7583) 
    H = round(width * .885)
	
    R1 = round(height * 0.0058)
    R2 = round(height * 0.1314)
    R3 = round(height * 0.256)
    R4 = round(height * 0.375) 
    R5 = round(height * 0.50)
    R6 = round(height * 0.625) 
    R7 = round(height * 0.75)
    R8 = round(height * 0.88)
    
    row_ = {0: R1, 1: R2, 2: R3, 3: R4,
            4: R5, 5: R6, 6: R7, 7: R8}
    col_ = {0: A, 1: B, 2: C, 3: D,
            4: E, 5: F, 6: G, 7: H}
    
    b1 = board.getBoard()
    for x in range(len(b1)):
        for y in range(len(b1[x].split("\u2002"))):
            this_square = b1[x][1:].split("\u2002")[y]
            if "♟" in this_square:
                im.paste(BP, (col_.get(y), row_.get(x)), BP) 
            elif "♜" in this_square:
                im.paste(BR, (col_.get(y), row_.get(x)), BR) 
            elif "♞" in this_square:
                im.paste(BN, (col_.get(y), row_.get(x)), BN) 
            elif "♝" in this_square:
                im.paste(BB, (col_.get(y), row_.get(x)), BB) 
            elif "♛" in this_square:
                im.paste(BQ, (col_.get(y), row_.get(x)), BQ) 
            elif "♚" in this_square:
                im.paste(BK, (col_.get(y), row_.get(x)), BK) 
            elif "♙" in this_square:
                im.paste(WP, (col_.get(y), row_.get(x)), WP) 
            elif "♖" in this_square:
                im.paste(WR, (col_.get(y), row_.get(x)), WR) 
            elif "♘" in this_square:
                im.paste(WN, (col_.get(y), row_.get(x)), WN) 
            elif "♗" in this_square:
                im.paste(WB, (col_.get(y), row_.get(x)), WB) 
            elif "♕" in this_square:
                im.paste(WQ, (col_.get(y), row_.get(x)), WQ) 
            elif "♔" in this_square:
                im.paste(WK, (col_.get(y), row_.get(x)), WK) 
            else: pass
    return im;
