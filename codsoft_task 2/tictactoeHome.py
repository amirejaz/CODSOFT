from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

class HomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("450x400+450+80")
        self.root.resizable(False,False)
        self.root.config(bg="palegreen3")

        #title
        self.title = Label(self.root,text="Tic Tac Toe",anchor="w",bg="goldenrod1", padx=120,fg="white",font=("Helvetica", 30, "bold")).place(x=0,y=0,relwidth=1)

        self.img = Image.open("images/tictactoe.png")
        self.resize_image1 = self.img.resize((140,140))
        self.showimg = ImageTk.PhotoImage( self.resize_image1)
        # create label and add resize image
        label = Label(image=self.showimg)
        label.image = label
        label.place(x=150,y=100)

        
        playbtn = Button(self.root, text="Play",cursor="hand2",command=self.game_window, bg="green", fg="white", font=("Helvetica", 25)).place(x=160, y=300, width=120, height=30)
        exitbtn = Button(self.root, text="Exit",cursor="hand2",command=self.exit_, bg="red", fg="white", font=("Helvetica", 25)).place(x=160, y=350, width=120, height=30)

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()
    
    def game_window(self):
        self.root.destroy()
        from tictactoe import TicTacToeGUI
        root = Tk()
        obj = TicTacToeGUI(root)
        root.mainloop()

def main():
    root = Tk()
    app = HomeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()