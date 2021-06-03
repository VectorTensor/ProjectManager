import sqlite3

conn = sqlite3.connect('Database.db')
c=conn.cursor()
c.execute("""CREATE TABLE Todays_work(_id INTEGER PRIMARY KEY AUTOINCREMENT, Work text ,Remarks text)""")
conn.commit()
c.close()

