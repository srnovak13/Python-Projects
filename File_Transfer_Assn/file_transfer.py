import shutil
import os

# set where the source of the files are
source = 'C:\\Users\\srnov\\Git Depositories\\Python Projects\\Python-Projects\\File_Transfer_Assn\\Folder_A'

#set the destination path to folder B
destination = 'C:\\Users\\srnov\\Git Depositories\\Python Projects\\Python-Projects\\File_Transfer_Assn\\Folder_B'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i,destination)
    
