Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> connection = sqlite3.connect("C:\\Users\\srnov\\test_database.db")
>>> c = connection.cursor()
>>> c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
sqlite3.OperationalError: table People already exists
>>> c.execute("INSERT INTO People VALUES('Ron','Obvious',42)")
<sqlite3.Cursor object at 0x000002710DE74340>
>>> connection.commit()
>>> c.execute("DROP TABLE IF EXISTS People")
<sqlite3.Cursor object at 0x000002710DE74340>
>>> connection.close()
>>> with sqlite3.connect("test_database.db") as connection:
	c = connection.cursor()
	c.executescript("""DROP TABLE IF EXISTS People;
		         CREATE TABLE People(FirstName TEXT,LastName TEXT,Age INT);
		         INSERT INTO People VALUES('Ron','Obvious','42');
		         """)

	
<sqlite3.Cursor object at 0x000002710DEBE9D0>
>>> peopleValues = (('Luigi','Vercotti',43),('Arthur','Belling',28))
>>> c.executemany("INSERT INTO People VALUES(?,?,?)",peopleValues)
<sqlite3.Cursor object at 0x000002710DEBE9D0>
>>> 