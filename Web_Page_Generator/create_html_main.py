

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import webbrowser



class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        
        self.master.title("Summer Sales")
        self.master.configure(bg="lightgray")
        self.txt_fname = tk.Entry(self.master)
        self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.btn_add = tk.Button(self.master,width=12,height=2,text='Submit',command=self.OpenHTML)
        self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)

    def OpenHTML(self):
        f= open("summer_sale.html","w")

        message= """<html>
                            <body>
                            <h1>"""
        message2=self.txt_fname.get()
        message3=  """</h1>
                            </body>
                            </html>"""
        messageFinal=message+message2+message3
        

        f.write(messageFinal)
        f.close()

        filename='C:\\Users\\srnov\\Git Depositories\\Python Projects\\Python-Projects\\summer_sale.html'
        

        webbrowser.open_new_tab(filename)















if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
