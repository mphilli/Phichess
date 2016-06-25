# Create a representation of a chess board with multidimensional lists
# import validator
# import board_gen.create_board

class Board:
    # global variables
    global columns;
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    global rows;
    rows = ['8', '7', '6', '5', '4', '3', '2', '1'];
    global sofar;
    sofar = 0

    # global history; history = [];

    def __init__(self):
        self.board = Board.create_board(rows, columns)
        # self.history = history # records history of moves
        self.rows = rows
        self.columns = columns
        self.sofar = sofar
        # self.history = history

    def getBoard(self):
        '''
        new_board = Board()
        new_board.board = Board.create_board(rows, columns)
        new_board.board = Board.modify_board(self, history)
        '''
        return self.board;

    def getBoard2(self):
        # eliminates 'EN SPACE' (\u2002)
        board2 = []
        for line in self.board:
            line2 = line.replace("\u2002", "    ")
            line2 = line2.replace("[]", "[    ]")
            board2.append(line2)
        return board2;

    def place_pieces(current_square):
        piece = "  ";
        # pawns: 
        if current_square.endswith("2"):
            piece = "♙ "  # white pawn
        if current_square.endswith("7"):
            piece = "♟ "  # black pawn
        # the back rank for each side: 
        white_end = {'A1': '♖ ', 'B1': '♘ ', 'C1': '♗ ', 'D1': '♕ ',
                     'E1': '♔ ', 'F1': '♗ ', 'G1': '♘ ', 'H1': '♖ '}
        black_end = {'A8': '♜ ', 'B8': '♞ ', 'C8': '♝ ', 'D8': '♛ ',
                     'E8': '♚ ', 'F8': '♝ ', 'G8': '♞ ', 'H8': '♜ '}
        if current_square in white_end:
            piece = white_end.get(current_square)
        if current_square in black_end:
            piece = black_end.get(current_square)

        # if piece == "  ": piece = current_square; 
        return piece;

    def create_board(rows, columns):
        rowlist = []
        for x in range(len(columns)):
            for y in range(len(rows)):
                current_square = columns[y] + rows[x]
                square = Board.place_pieces(current_square)
                if (y + 1) % 8 == 0:
                    rowlist[x] += ' [' + square.replace(" ", "") + ']'
                elif (y) % 8 == 0:
                    rowlist.append('[' + square.replace(" ", "") + ']')
                else:
                    rowlist[x] += ' [' + square.replace(" ", "") + ']'
        board = rowlist;
        return board;

    def modify_board(self, m_input):
        if type(m_input) == list:
            moves = m_input
        else:
            moves = m_input.split(", ")
        # notation = ""
        global sofar
        assoc_row = {'1': '7', '2': '6', '3': '5', '4': '4',
                     '5': '3', '6': '2', '7': '1', '8': '0'}
        assoc_col = {'A': '0', 'B': '1', 'C': '2', 'D': '3',
                     'E': '4', 'F': '5', 'G': '6', 'H': '7'}
        for move in moves:
            if not " " in move: pass
            # move = validator.find_piece(move, self.board, sofar)
            # handle starting position
            # history.append(move)
            start_square = move.split()[0]
            start_column = int(assoc_col.get(start_square[0]))
            start_row = int(assoc_row.get(start_square[1]))
            # print("piece: "+ board[start_row].split("  ")[start_column])
            this_row = self.board[start_row].split(" ")
            piece = this_row[start_column]
            this_row[start_column] = '[]'
            self.board[start_row] = ' '.join(this_row)

            # handle ending position
            end_square = move.split()[1]
            end_column = int(assoc_col.get(end_square[0]))
            end_row = int(assoc_row.get(end_square[1]))
            this_row = self.board[end_row].split(" ")
            # notation += generate_notation(piece, start_square, end_square, this_row[end_column])
            this_row[end_column] = piece
            self.board[end_row] = ' '.join(this_row)

            sofar += 1
        # print(notation)
        return self.board;

    def generate_notation(piecename, start_square, end_square, at_position):
        english = {'♙': "", '♟': "", '♘': 'N', '♞': 'N', '♝': 'B',
                   '♗': 'B', '♖': 'R', '♜': 'R', '♔': 'K', '♚': 'K',
                   '♛': 'Q', '♕': 'Q'}
        move = ""
        piecename = piecename.replace("[", "");
        piecename = piecename.replace("]", "");
        piece = english.get(piecename)
        move += piece
        if at_position != "[]": move += "x"
        destination = end_square.lower()
        move += destination
        return move + " ";

    def view_board(self):
        print("")
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
        for n in range(len(self.board)):
            print(str(len(self.board) - n) + self.board[n].replace("[]", "[  ]"))
        print("   ", end="")
        for letter in columns: print(letter + "    ", end="")
        print("")

    def reset_board(self):
        self.board = Board.create_board(rows, columns)
        history = [];


'''
evans_gambit = ['E2 E4', 'E7 E5', 'G1 F3', 'B8 C6', 'F1 C4', 'F8 C5', 'B2 B4']
board = modify_board(create_board(rows, columns), evans_gambit)

TO DO:
* VALIDATE MOVES
* ALGEBRAIC NOTATION INPUT 
'''
