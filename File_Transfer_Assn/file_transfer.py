
#Importing necessary modules
import shutil 
import os
import datetime
import file_transfer_GUI


#Comparing datetimes using comparison operators
today_datetime = datetime.datetime.now()
#Process for getting datetimes in the past. Timedelta is a change in time, then you subtract the change in time from today.
yesterday_datetime = today_datetime - datetime.timedelta(days = 1) 


#Parameters are necessary since this comes from out of the file
def move_files(source, destination):
    
    #Getting a list of the files in the source folder
    fileNames = os.listdir(source)
    source += "\\"  
    destination += "\\"
    for i in fileNames:
        source_path = source+i
        #This is the timestamp, seconds from epoch
        mod_timestamp = os.path.getmtime(source_path)
        #This converts to a datetime
        file_datetime = datetime.datetime.fromtimestamp(mod_timestamp)
        
        #Simple comparison operator that works on datetime objects
        if file_datetime >= yesterday_datetime:
            #Moves the file
            shutil.move(source_path, destination) 

if __name__ == "__main__":
    pass
    
