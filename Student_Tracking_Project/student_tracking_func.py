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

#Importing other modules
import student_tracking
import student_tracking_gui

def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

#Catch if user clicks on the windows upper-right X to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

#=================================================
def create_db(self):
    conn = sqlite3.connect('student_list.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT,\
        col_lname TEXT,\
        col_phone TEXT,\
        col_email TEXT,\
        col_course TEXT\
        );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('student_list.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_phone,col_email,col_course) VALUES (?,?,?,?,?)""", ('John','Smith','555-123-4567','jsmith@email.com','French 101'))
            conn.commit()
    conn.close()

def count_records(cur):
    count=""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur, count

#Select item in ListBox
def onSelect(self,event):
    varList = event.widget
    select = VarList.curselection()[0]
    value = VarList.get(select)
    conn = sqlite3.connect('student_list.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_lname = (?)""",[value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def onSubmit(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize data to keep it consistent in database
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip().title()
    if not "@" or not"." in var_email:
        print("Incorrect email format!")
    if (len(var_fname) > 0 and len(var_lname > 0 and len(var_phone) >0 and len(var_email) > 0 and len(var_course) > 0):
        conn = sqlite3.connect('student_list.db')
        with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(col_lname) FROM tbl_students WHERE col_lname = '{}'""".format(var_lname))
        count = cursor.fetchone()[0]
        chkName = count
        if chkName == 0:
            print("chkName: {}".format(chkName))
            cursor.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_phone,col_email,col_course) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_phone,var_email,var_course))
            self.lstList1.insert(END, var_lname)
            onClear(self)
        else:
            messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name".format(var_lname))
            onClear(self)
    conn.commit()
    conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('student_list.db)
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*)FROM tbl_student""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete confirmation","All information associated with,({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('student_list.db')
                with conn:
                        cursor = conn.cursor()
                        cursor.execute("""DELETE FROM tbl_students WHERE col_lname = '{}'""".format(var_select)
                        onDeleted(self)
                        conn.commit()
          else:
              confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('student_list.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT col_lname FROM tbl_students""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()

if __name__ == "__main__":
    pass
