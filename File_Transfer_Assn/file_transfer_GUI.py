import tkinter
from tkinter import *
from tkinter import filedialog
import file_transfer

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('File Transfer GUI')
        self.master.minsize(550,200)

        self.txt_browse1 = Entry(self.master, text = "", font = ("Helvetica", 12), width = 40)
        self.txt_browse1.grid(row = 0, column = 1, columnspan = 8, padx = (20,20), pady=(50,7))
        
        self.txt_browse2 = Entry(self.master, text = "", font = ("Helvetica", 12), width = 40)
        self.txt_browse2.grid(row = 2, column = 1, columnspan = 8, padx=(5,0), pady=(5,5))



        self.btn_browse1 = Button(self.master, text = "Move From...", width = 12, height = 1, command=lambda:self.get_directory(self.txt_browse1))
        self.btn_browse1.grid(row=0, column=0, padx = (20,20), pady=(50,7))

        self.btn_browse2 = Button(self.master, text = "Move To...", width = 12, height = 1, command=lambda:self.get_directory(self.txt_browse2))
        self.btn_browse2.grid(row=2, column=0, padx = (5,0), pady=(5,5))

        self.btn_checkFiles = Button(self.master, text = "Move Files", width = 12, height = 2, command=lambda:file_transfer.move_files(self.txt_browse1.get(), self.txt_browse2.get()))
        self.btn_checkFiles.grid(row=4, column=0, padx = (5,0), pady=(10,5))

        self.close = Button(self.master, text = "Close Program", width = 12, height = 2, command = lambda:self.quit())
        self.close.grid(row=4, column=8, padx = (5,0), pady=(10,5))

    def get_directory(self, text):
        directory = filedialog.askdirectory()
        text.delete(0,END)
        text.insert(0,directory)
        return

    def quit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
