#
#
#Python Version: 3.9.1
#
#Author: Steven R. Novak
#
#Purpose: Demonstrating using Tkinter GUI module,
#              Using Tkinter Parent and Child relationships
#
#Tested OS: This code was written and tested to work on Windows 10


from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Importing other modules to have access to them
import student_tracking_gui
import student_tracking_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Defining master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #Using CenterWindow method to center app on screen
        student_tracking_func.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="lightgray")
        #Using protocol method to catch if user click the 'X" button
        self.master.protocol("WM_DELETE_WINDOW", lambda student_tracking_func.ask_quit(self))
        arg = self.master

        #Loading GUI widget from separate module
        student_tracking_gui.load_gui(self)

        













if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
