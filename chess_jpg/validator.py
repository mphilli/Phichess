'''
TO DO:
Pawn (forward move) ✓
Pawn (attack) ✓
Pawn (en passant)
Knight movement ✓
Bishop movement ✓
Rook movement
Queen movement ✓
King movement ✓
Castling (O-O, O-O-O) ✓
Ambiguous notation
'''


def find_piece(move, board, sofar):
    # print("move :" + move)
    part1 = ""
    move = move.replace("+", "")
    move = move.replace("#", "")

    assoc_row = {'1': '7', '2': '6', '3': '5', '4':'4',
                 '5': '3', '6': '2', '7': '1', '8':'0',
                 '0': '8'}
    assoc_col = {'A': '0', 'B': '1', 'C': '2', 'D': '3',
                 'E': '4', 'F': '5', 'G': '6', 'H': '7',
                 '0': 'A', '1': 'B', '2': 'C', '3': 'D',
                 '4': 'E', '5': 'F', '6': 'G', '7': 'H'}
    white_move = False
    black_move = False
    if sofar % 2 == 0:
        white_move = True
    else:
        black_move = True

    #Castling, short
    if move == "O-O":
        if white_move:
            return ['E1 G1', 'H1 F1']
        else:
            return ['E8 G8', 'H8 F8']
   #Castling, long
    if move == "O-O-O":
        if white_move:
            return ['E1 C1', 'A1 D1']
        else:
            return ['E8 C8', 'A8 D8']

    part2 = move[len(move)-2:].upper()
    #destination
    row = part2[len(part2)-1:]
    col = part2[0:1]
    brow = int(assoc_row.get(row))
    bcol = int(assoc_col.get(col))
    destination = brow + bcol # for bishop
    #pawn, forward movement
    if len(move)== 2:
        if white_move:

            if "♙" in board[brow+2].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow+2)))
            elif "♙" in board[brow+1].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow+1)))
        elif black_move==True:
            if "♟" in board[brow-2].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow-2)))
            elif "♟" in board[brow-1].split("\u2002")[bcol]:
                part1 = col + str(assoc_row.get(str(brow-1)))

    #pawn, attack. en passant still unsupported
    columns_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for column in columns_lower:
        if move.startswith(column + "x"):
            if white_move:
                if (brow + 1) <= 7:
                    if bcol + 1 <= 7:
                        if "♙" in board[brow + 1].split("\u2002")[bcol+1] \
                                and column.upper() == assoc_col.get(str(bcol+1)):
                            part1 = column.upper() + str(int(row) - 1)
                            break
                    if bcol - 1 >= 0:
                        if "♙" in board[brow + 1].split("\u2002")[bcol-1] \
                                and column.upper() == assoc_col.get(str(bcol-1)):
                            part1 = column.upper() + str(int(row) - 1)
                            break
            elif black_move == True:
                if (brow-1) >= 0:
                    if bcol+1 <= 7:
                        if "♟" in board[brow - 1].split("\u2002")[bcol+1] \
                                and column.upper() == assoc_col.get(str(bcol+1)):
                            part1 = column.upper() + str(int(row)+1)
                            break
                    if bcol-1 >= 0:
                        if "♟" in board[brow - 1].split("\u2002")[bcol-1] \
                                and column.upper() == assoc_col.get(str(bcol-1)):
                            part1 = column.upper() + str(int(row)+1)
                            break
    #knight
    if move.startswith("N"):
        if white_move: knight = "♘"
        else: knight = "♞"

        #vertical, up
        if brow-2 >= 0:
            if knight in board[brow-2]:
                if bcol-1 >= 0:
                    if knight in board[brow-2].split("\u2002")[bcol-1]:
                        part1 = str(assoc_col.get(str(bcol-1))) + str((int(row)+2))
                if bcol+1 <= 7:
                    if knight in board[brow-2].split("\u2002")[bcol+1]:
                        part1 = str(assoc_col.get(str(bcol+1))) + str((int(row)+2))
        ##vertical, down2
        if brow+2 <= 7:
            if knight in board[brow + 2]:
                if bcol - 1 >= 0:
                    if knight in board[brow + 2].split("\u2002")[bcol - 1]:
                        part1 = str(assoc_col.get(str(bcol - 1))) + str((int(row) - 2))
                if bcol + 1 <= 7:
                    if knight in board[brow + 2].split("\u2002")[bcol + 1]:
                        part1 = str(assoc_col.get(str(bcol + 1))) + str((int(row) - 2))
        ##vertical, up2
        if brow-1 >= 0:
            if knight in board[brow-1]:
                if bcol - 2 >= 0:
                    if knight in board[brow-1].split("\u2002")[bcol-2]:
                        part1 = str(assoc_col.get(str(bcol-2))) + str((int(row)-1))
                if bcol + 2 <= 7:
                    if knight in board[brow-1].split("\u2002")[bcol+2]:
                        part1 = str(assoc_col.get(str(bcol+2))) + str((int(row)-1))
        ##vertical, down
        if brow+1 <= 7:
            if knight in board[brow+1]:
                if bcol - 2 >= 0:
                    if knight in board [brow+1].split("\u2002")[bcol-2]:
                        part1 = str(assoc_col.get(str(bcol-2))) + str((int(row)-1))
                if bcol + 2 <= 7:
                    if knight in board [brow+1].split("\u2002")[bcol+2]:
                        part1 = str(assoc_col.get(str(bcol+2))) + str((int(row)-1))

    #Bishop
    if move.startswith("B"):
        if white_move: bishop = "♗"
        else: bishop = "♝"
        #white square bishop, white squares = even
        for x in range(len(board)):
            for y in range(len(board[x].split("\u2002"))):
                # find square of destination and compare (even vs odd)
                square = x + y
                bish_row = assoc_row.get(str(x))
                bish_col = assoc_col.get(str(y))

                if square % 2 == 0 and destination % 2 == 0:
                    #light square bishop
                    if bishop in board[x].split("\u2002")[y]:
                        part1 = bish_col + bish_row
                        break # stop looking for bishop
                elif square % 2 != 0 and destination % 2 != 0:
                    #dark square bishop
                    if bishop in board[x].split("\u2002")[y]:
                        part1 = bish_col + bish_row
                        break # stop looking for bishop

    #Queen
    if move.startswith("Q"):
        if white_move: queen = "♕"
        else: queen = "♛"
        for x in range(len(board)):
            for y in range(len(board[x].split("\u2002"))):
                if queen in board[x].split("\u2002")[y]:
                    part1 = assoc_col.get(str(y)) +assoc_row.get(str(x))

    #King
    if move.startswith("K"):
        if white_move: king = "♔"
        else: king = "♚"
        for x in range(len(board)):
            for y in range(len(board[x].split("\u2002"))):
                if king in board[x].split("\u2002")[y]:
                    part1 = assoc_col.get(str(y)) + assoc_row.get(str(x))

    if part1 == "":
        part1 = "ERROR"
        print("Error: could not understand the move " + move)
    start_end = part1 + " " + part2;
    print(start_end)
    return start_end;

# for testing
import phichess
if __name__ == "__main__":
    b = phichess.Board()
    b.modify_board(['e4', 'e5', 'Nf3', 'Nc6', 'Bc4', 'Bc5', 'O-O'])
    b.view_board()