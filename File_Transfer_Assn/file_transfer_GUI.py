# Importing modules
import shutil 
import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog 
	

# Defining CreateWidgets() function to 
# create tkinter widgets 
def CreateWidgets(): 
	link_Label = Label(root, text ="Select The File To Copy/Move : ",bg = "lightgray")
					 
	link_Label.grid(row = 1, column = 0, pady = 5, padx = 5)
					 
	
	root.sourceText = Entry(root, width = 50,textvariable = sourceLocation) 
							 
	root.sourceText.grid(row = 1, column = 1, pady = 5, padx = 5,columnspan = 2)
						 
						 
	
	source_browseButton = Button(root, text ="Browse",command = SourceBrowse, width = 15) 
								
	source_browseButton.grid(row = 1, column = 3,pady = 5, padx = 5) 
							 
	
	destinationLabel = Label(root, text ="Select The Destination : ",bg ="lightgray")
							 
	destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5)
						 
	
	root.destinationText = Entry(root, width = 50,textvariable = destinationLocation) 
								 
	root.destinationText.grid(row = 2, column = 1,pady = 5, padx = 5,columnspan = 2)   
							
							
	
	dest_browseButton = Button(root, text ="Browse",command = DestinationBrowse, width = 15)
							 
	dest_browseButton.grid(row = 2, column = 3,pady = 5, padx = 5)
						 
	
	copyButton = Button(root, text ="Copy File",command = CopyFile, width = 15)
						 
	copyButton.grid(row = 3, column = 1,pady = 5, padx = 5) 
					 
	
	moveButton = Button(root, text ="Move File",command = MoveFile, width = 15)
						 
	moveButton.grid(row = 3, column = 2,pady = 5, padx = 5)  
					

def SourceBrowse(): 
	
	#Opening the file-dialog directory prompting 
	# the user to select files to copy using 
	#filedialog.askopenfilenames() method
	root.files_list = list(filedialog.askopenfilenames(initialdir ="C:/Users/srnov")) 
	
	# Displaying the selected files in the root.sourceText 
	# Entry using root.sourceText.insert() 
	root.sourceText.insert('1', root.files_list) 
	
def DestinationBrowse(): 
	# Opening the file-dialog directory prompting 
	# the user to select destination folder to 
	# which files are to be copied using the 
	# filedialog.askopendirectory() method. 
	 destinationdirectory = filedialog.askdirectory(initialdir ="C:/Users/srnov") 

	# Displaying the selected directory in the 
	# root.destinationText Entry using 
	# root.destinationText.insert() 
	 root.destinationText.insert('1', destinationdirectory)
	
def CopyFile(): 
	# Retrieving the source file selected by the 
	# user in the SourceBrowse() and storing it in a 
	# variable named files_list 
	files_list = root.files_list 

	# Retrieving the destination location from the 
	# textvariable using destinationLocation.get() and 
	# storing in destination_location 
	destination_location = destinationLocation.get() 

	# Looping through files present in the list 
	for f in files_list: 
		
		# Copying the file to the destination using copy()
	                shutil.copy(f, destination_location) 

	messagebox.showinfo("SUCCESSFULL") 
	
def MoveFile(): 
	
	# Retrieving the source file selected by the 
	# user in the SourceBrowse() and storing it in a 
	# variable named files_list''' 
	files_list = root.files_list 

	# Retrieving the destination location from the 
	# textvariable using destinationLocation.get() and 
	# storing in destination_location 
	destination_location = destinationLocation.get() 

	# Looping through files present in the list 
	for f in files_list: 
		
		# Moving the file to the destination using move()
		 shutil.move(f, destination_location) 

	messagebox.showinfo("SUCCESSFULL") 

# Creating object of tk class 
root = tk.Tk() 
	
# Setting the title and background color 
# disabling the resizing property 
root.geometry("830x120") 
root.title("File-Transfer GUI") 
root.config(background = "blue") 
	
# Creating tkinter variable 
sourceLocation = StringVar() 
destinationLocation = StringVar() 
	
# Calling the CreateWidgets() function 
CreateWidgets() 
	
 
root.mainloop() 
