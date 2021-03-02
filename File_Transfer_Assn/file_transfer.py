import shutil
import os

# set where the source of the files are
source = 'C:\\Users\\srnov\\Git Depositories\\Python Projects\\Python-Projects\\File_Transfer_Assn\\Folder_New\\'

#set the destination path to folder B
destination = 'C:\\Users\\srnov\\Git Depositories\\Python Projects\\Python-Projects\\File_Transfer_Assn\\Folder_TBD\\'
files = os.listdir(source)

#moving all the files in "Folder_New" to "Folder_TBD"
shutil.copytree(source,destination)



if 
    
