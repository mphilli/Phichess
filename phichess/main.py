from phichess import Board
import board_gen
import os
import os.path
from random import randint

# small interface, class instance

def play(board):
    if board.sofar % 2 == 0:
        move = input("White to move: ")
    else:
        move = input("Black to move: ")
    if move=="image":
        board_gen.generate_board(board)
        board_gen.im.show()
        play(board)
    elif move == "quit":
        main();
    else: 
        board.modify_board(move.upper())
        board.view_board()
        board.sofar += 1
        play(board)


def main():
    board = Board()
    print("Phichess 0.1")
    print("commands: view, move, reset, create image")
    command = input(">>> ")
    while(command != "quit"):
        randname = str(randint(0, 1099))
        if command == "play": play(board) 
        if command == "view":
            board.view_board()
        elif command == "move":
            moves = input("move(s): ")
            board.board = board.modify_board(moves.upper())
        elif command == "reset":
            board.reset_board()
        elif command == "create image":
            if os.path.isfile("last_position.jpg"):
                print("found")
                os.remove("last_position.jpg")
            result = board_gen.generate_board(board)
            result.show()
            result.save(randname + ".jpg")
        else: board.modify_board(command.upper())
        command = input("command: ")

if __name__ == "__main__":
    #execute the main method
    main()

