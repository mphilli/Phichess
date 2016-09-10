from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from phichess import Board
import board_gen

class PhichessApplication(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.b = Board()

    def createWidgets(self):

        #frames
        frameleft = Frame(self, height = 200, width = 400)
        frameright = Frame(self)

        # label for image
        image = Image.open("chess_pieces/starting_board.jpg")
        photo = ImageTk.PhotoImage(image)
        self.image_label = Label(frameright, image=photo) #image
        self.image_label.image = photo

        title_image = Image.open("chess_pieces/chess-banner.jpg")
        title_photo = ImageTk.PhotoImage(title_image)

        # other labels
        self.title_label = Label(frameright, image=title_photo) # title
        self.title_label.image = title_photo
        self.seq_label = Label(frameright, text="")
        self.label = Label(frameleft, text="Enter moves manually: ") # text
        self.label2 = Label(frameleft, text="Search list: ") # text 2

        # text entry fields #
        self.command = Entry(frameleft, width=44)
        self.searchbar = Entry(frameleft)


        # Buttons #
        self.first_enter = Button(frameleft, width=20)
        self.first_enter["text"] = "Enter"
        self.first_enter["command"] = self.cipher

        self.button_reset = Button(frameleft, width=30, text="Reset")
        self.button_reset["command"] = self.reset

        self.second_enter = Button(frameleft, width=30)
        self.second_enter["text"] = "Enter"
        self.second_enter["command"] = self.displayseq

        self.copy_button = Button(frameright, width = 30, text ="Copy Notation to Clipboard")
        self.copy_button["command"] = self.copy

        self.searchbutton = Button(frameleft)
        self.searchbutton['text'] = "Search"
        self.searchbutton['command'] = lambda: self.search_click(self.searchbar.get())

        #list box with openings
        self.listbox = Listbox(frameleft, height = 35, width = 44)
        openings = get_openings()
        for item in openings:
            self.listbox.insert(END, item)

        self.listbox.bind('<Double-1>', lambda x: self.second_enter.invoke())
        self.listbox['font'] = ("Sans Serif", 12)

        self.scrollbar = Scrollbar(frameleft)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # GRID ORIENTATION

        #frames
        frameleft.grid(row=0, column = 0) # 0 0
        frameright.grid(row=0, column = 1)

        #frameleft
        self.label.grid(row=1, column=0, columnspan = 2, sticky = "w")  # 0 0 TEXT
        self.command.grid(row=2, column=0, sticky="new", columnspan = 2) # 1 0
        self.first_enter.grid(row=2, column=1, sticky="we", columnspan = 2) # 2 0
        self.button_reset.grid(row=4, column=1, sticky="we", columnspan = 1) # 3 0
        self.searchbar.grid(row = 5, column = 0, sticky = "we")
        self.label2.grid(row=4, column = 0, sticky = "ws")
        self.scrollbar.grid(row=7, column=0, sticky="ens", columnspan = 2) # 4 0
        self.listbox.grid(row=7, column=0, columnspan = 2) # 4 0
        self.searchbutton.grid(row= 5, column = 1, sticky = "we")
        self.second_enter.grid(row=6, column=1, sticky="nswe", columnspan = 1) # 5 0

        #frameright
        self.title_label.grid(row=0, column=0, columnspan=2)   # TITLE
        self.title_label.config(font=("Sans Serif", 24))
        self.image_label.grid(row=1, column=0, columnspan = 2) # 0 1 IMAGE
        self.seq_label.grid(row=2, column=0, columnspan = 1)  # 1 1
        self.copy_button.grid(row=2, column = 1, sticky ="ens")

    def reset(self):
        self.b.reset_board()
        self.seq_label['text'] = ""
        self.command.delete(0, END)
        self.searchbar.delete(0, END)
        #reset the listbox
        self.listbox.delete(0, END)
        openings = get_openings()
        for item in openings:
            self.listbox.insert(END, item)
        image = Image.open("chess_pieces/starting_board.jpg")
        photo = ImageTk.PhotoImage(image)
        self.image_label['image'] = photo
        self.image_label.image = photo

    def cipher(self):
        moves = self.command.get()
        self.b.reset_board()
        moves = moves.replace(" ", ", ")
        print(moves)
        self.b.modify_board(moves)
        result = board_gen.generate_board(self.b)
        result.save("last.jpg")
        image = Image.open("last.jpg")
        photo = ImageTk.PhotoImage(image)
        self.image_label['image'] = photo
        self.image_label.image = photo
        self.seq_label.config(font=("sans serif", 22))
        self.seq_label['text'] = moves
        self.seq_label.grid(row=2, column=0)

    def displayseq(self):
        self.b.reset_board()
        index = self.listbox.curselection()[0]
        file = open("chess_openings_list.txt")
        sequences = []
        lines = file.readlines()
        if self.listbox.size() < 2014:
            for line in lines:
                    if line.split(" - ")[0] in self.listbox.get(0,END):
                        sequences.append(line.split(" -  ")[1])
        else:
            for line in lines:
                sequences.append(line.split(" -  ")[1])
        sequence = sequences[index].replace("\n", "")
        print(self.listbox.size())
        moves = sequence.replace(" ", ", ")
        print(moves)
        self.b.modify_board(moves)
        result = board_gen.generate_board(self.b)
        result.save("last.jpg")
        image = Image.open("last.jpg")
        photo = ImageTk.PhotoImage(image)
        self.image_label['image'] = photo
        self.image_label.image = photo
        self.seq_label.config(font=("sans serif", 22))
        self.seq_label['text'] = sequence
        self.seq_label.grid(row=2, column=0)

    def copy(self):
        root2 = Tk()
        root2.withdraw()
        root2.clipboard_clear()
        root2.clipboard_append(self.seq_label['text'])
        root2.destroy()

    def search_click(self, search):
        openings = get_searched(search)
        self.listbox.delete(0, END)
        for item in openings:
            self.listbox.insert(END, item)
			
    """
    def search(self):
        root3 = Tk()
        root3.bind('<Return>', self.search_click())
    """


def get_openings():
    file = open("chess_openings_list.txt", "r+")
    lines = file.readlines()
    openings = []
    for line in lines:
        openings.append(line.split(" - ")[0])
    file.close()
    return openings

def get_searched(search):
    file = open("chess_openings_list.txt", "r+")
    lines = file.readlines()
    openings = []
    for line in lines:
        if search.lower() in line.lower():
            openings.append(line.split(" - ")[0])
    file.close()
    return openings

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Chess JPG 0.2")
    app = PhichessApplication(master=root)
    app.mainloop()