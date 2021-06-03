import sqlite3
from objects import Works


conn=sqlite3.connect('Database.db')
c=conn.cursor()
def Add_work(table,Work):
    with conn:

        c.execute("""INSERT INTO Todays_work(Work,Remarks)VALUES(:work,:remarks)""",{"work":Work.work,"remarks":Work.remarks})
def show_table():

    with conn:
        c.execute("""SELECT * FROM Todays_work""")
    data=c.fetchall()
    return data
        
def Add():
    w=input("Enter the work: ")
    r=input("Enter the remark: ")
    data=Works(w,r)
    Add_work("Todays_work",data)
def delete_table():
    with conn:
        c.execute("DROP TABLE Todays_work")

def update(n):
    with conn:
#        print(n)
        c.execute("UPDATE Todays_work SET Remarks = \"done\" WHERE _id=?",(n,)) 




