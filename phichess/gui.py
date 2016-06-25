from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from phichess import Board
import board_gen

class PhichessApplication(Frame):

    board = Board()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        
        frame = Frame(self, height = 200, width = 400)
        frame.grid(row=0, column = 0, sticky = "n")
        #label for image
        image = Image.open("chess_pieces/starting_board.jpg")
        photo = ImageTk.PhotoImage(image)
        self.label1 = Label(self, image=photo)
        self.label1.grid(row = 0, column = 1)
        self.label1.image = photo
        
        self.label = Label(frame, text="Enter moves manually: ")
        self.label.grid(row = 0, column = 0)
        '''
        self.main_text = Text(self)
        self.main_text["height"] = 10;
        self.main_text["width"] = 40;
        self.main_text["font"] = ("Helvetica", 22)
        self.main_text.grid(row=0, column=1)
        '''
        self.command = Entry(frame, width = 44)
        self.command.grid(row=1, column=0, sticky="n")
        self.button1 = Button(frame, width=30)
        self.button1["text"] = "Enter"
        self.button1["command"] = self.cipher
        self.button1.grid(row=2, column=0, sticky = "we")
        self.button_reset = Button(frame, width = 30, text = "Reset")
        self.button_reset["command"] = self.reset
        self.button_reset.grid(row = 3, column = 0, sticky = "we")

        
        self.listbox = Listbox(frame, width = 44, height =40)
        openings = get_openings()
        for item in openings:
            self.listbox.insert(END, item)
        self.listbox.grid(row=4, column = 0)
        self.scrollbar = Scrollbar(frame)
        self.scrollbar.grid(row=4, column = 0, sticky="ens")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.button2 = Button(frame, width=30)
        self.button2["text"] = "Enter"
        self.button2["command"] = self.displayseq
        self.button2.grid(row=5, column = 0, sticky = "we")

    def reset(self):
        image = Image.open("chess_pieces/starting_board.jpg")
        photo = ImageTk.PhotoImage(image)
        self.label1 = Label(self, image=photo)
        self.label1.grid(row=0, column=1)
        self.label1.image = photo


    def cipher(self):
        board = PhichessApplication.board
        data = self.command.get()
        if data == "view":
            
            self.main_text.delete('1.0', END)
            rows = board.getBoard2()
            for x in rows:
                self.main_text.insert(END, x + "\n")
            self.command.delete(0,END)
            self.command.insert(0,"")
        if " " in data:   
            #self.main_text.delete('1.0', END)
            board.modify_board(data.upper())
            board.view_board()
            result = board_gen.generate_board(board)
            result.save("last.jpg")
            '''
            rows = board.getBoard2()
            for x in rows:
                self.main_text.insert(END, x + "\n")
            '''
            
            image = Image.open("last.jpg")
            photo = ImageTk.PhotoImage(image)
            self.label1 = Label(self, image=photo)
            self.label1.grid(row = 0, column = 1)
            self.label1.image = photo
            
            self.command.delete(0,END)
            self.command.insert(0,"")
        if data == "image":
            '''
            board_gen.generate_board(board)
            board_gen.im.save("last.jpg")
            image = Image.open("last.jpg")
            photo = ImageTk.PhotoImage(image)

            self.label1 = Label(self, image=photo)
            self.label1.grid(row = 1, column = 0)
            self.label1.image = photo
            self.command.delete(0,END)
            self.command.insert(0,"")
            '''

    def displayseq(self):
        index = self.listbox.curselection()[0]
        file = open("chess_openings_list.txt")
        sequences = []
        lines = file.readlines()
        for line in lines: 
            sequences.append(line.split(" - ")[1])
        sequence = sequences[index]


def get_openings():
    file = open("chess_openings_list.txt", "r+")
    lines = file.readlines()
    openings = []
    for line in lines:
        openings.append(line.split(" - ")[0])
    return openings;
    
if __name__ == "__main__":
    root = Tk()
    root.wm_title("PhiChess 0.1")
    app = PhichessApplication(master=root)
    app.mainloop()
