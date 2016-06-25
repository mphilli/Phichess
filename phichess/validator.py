#for validating moves and reading algebraic notation
import phichess

# ALGEBRA
#board = phichess.create_board(phichess.rows, phichess.columns)

def find_piece(move, board, sofar):
    part1 = ''; part2 = '';
    assoc_row = {'1': '7', '2': '6', '3': '5', '4':'4',
                 '5': '3', '6': '2', '7': '1', '8':'0'}
    assoc_col = {'A': '0', 'B': '1', 'C': '2', 'D': '3',
                 'E': '4', 'F': '5', 'G': '6', 'H': '7',
                 '0': 'A', '1': 'B', '2': 'C', '3': 'D',
                 '4': 'E', '5': 'F', '6': 'G', '7': 'H'}
    white_move = False; black_move = False;
    if sofar % 2 == 0:
        white_move = True
    else:
        black_move = True
    part2 = move[len(move)-2:].upper()
    #destination
    row = part2[len(part2)-1:]
    col = part2[0:1]
    brow = int(assoc_row.get(row))
    bcol = int(assoc_col.get(col))
    #pawn
    if len(move)==2:
        if white_move==True: 
            if "♙" in board[brow+2].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow+2)))
            elif "♙" in board[brow+1].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow+1)))
        elif black_move==True:
            if "♟" in board[brow-2].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow-2)))
            elif "♟" in board[brow-1].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow-1)))
    #knight
    if move.startswith("N"):
        if white_move==True:
            ##vertical, up
            if "♘" in board[brow-2]:
                if "♘" in board[brow-2].split("\u2002")[bcol-1]:
                    part1 = str(assoc_col.get(str(bcol-1))) + str((int(row)+2))
                elif "♘" in board[brow-2].split("\u2002")[bcol+1]:
                    part1 = str(assoc_col.get(str(bcol+1))) + str((int(row)+2))
            ##vertical, down2
            if "♘" in board[brow + 2]:
                if "♘" in board[brow + 2].split("\u2002")[bcol - 1]:
                    part1 = str(assoc_col.get(str(bcol - 1))) + str((int(row) - 2))
                elif "♘" in board[brow + 2].split("\u2002")[bcol + 1]:
                    part1 = str(assoc_col.get(str(bcol + 1))) + str((int(row) - 2))
            ##vertical, up2
            if "♘" in board[brow-1]:
                if "♘" in board[brow-1].split("\u2002")[bcol-2]:
                    part1 = str(assoc_col.get(str(bcol-2))) + str((int(row)-1))
                elif "♘" in board[brow-1].split("\u2002")[bcol+2]:
                    part1 = str(assoc_col.get(str(bcol+2))) + str((int(row)-1))
            ##vertical, down
            if "♘" in board[brow+1]:
                if "♘" in board [brow+1].split("\u2002")[bcol-2]:
                    part1 = str(assoc_col.get(str(bcol-2))) + str((int(row)-1))
                elif "♘" in board [brow+1].split("\u2002")[bcol+2]:
                    part1 = str(assoc_col.get(str(bcol+2))) + str((int(row)-1))

        elif black_move==True:
            ##vertical, up 
            if "♞" in board[brow-2]:
                if "♞" in board[brow-2].split("\u2002")[bcol-1]:
                    part1 = str(assoc_col.get(str(bcol-1))) + str((int(row)+2))
                elif "♞" in board[brow-2].split("\u2002")[bcol+1]:
                    part1 = str(assoc_col.get(str(bcol+1))) + str((int(row)+2))
            ##vertical, up2
            if "♞" in board[brow-1]:
                if "♞" in board[brow-1].split("\u2002")[bcol-2]:
                    part1 = str(assoc_col.get(str(bcol-2))) + str((int(row)-1))
                elif "♞" in board[brow-1].split("\u2002")[bcol+2]:
                    part1 = str(assoc_col.get(str(bcol+2))) + str((int(row)-1))
            ##vertical, down
            if "♞" in board[brow+1]:
                if "♞" in board [brow+1].split("\u2002")[bcol-2]:
                    part1 = str(assoc_col.get(str(bcol-2))) + str((int(row)-1))
                elif "♞" in board [brow+1].split("\u2002")[bcol+2]:
                    part1 = str(assoc_col.get(str(bcol+2))) + str((int(row)-1))
            ##vertical, down2
            if "♞" in board[brow+2]:
                if "♞" in board [brow+2].split("\u2002")[bcol-1]:
                    part1 = str(assoc_col.get(str(bcol-1))) + str((int(row)-2))
                elif "♞" in board [brow+2].split("\u2002")[bcol+1]:
                    part1 = str(assoc_col.get(str(bcol+1))) + str((int(row)-2))

        
    
        



            
    start_end = part1 + " " + part2;
    print(start_end)
    return start_end; 
