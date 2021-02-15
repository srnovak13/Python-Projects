import sqlite3

# create database 'test'
conn = sqlite3.connect('test.db')

#creating a table called 'tbl_files'
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_name TEXT\
            )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'MyMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#add .txt files to the database
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_name) VALUES(?)", (x,))
            print(x)
conn.close()
            
