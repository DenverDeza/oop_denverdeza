from tkinter import*
import sqlite3

#--------------------------------------------------------function

def submit():
    conn = sqlite3.connect("C:/Users/STUDENT4/DBdeza.db")

    c = conn.cursor()

    c.execute("Insert INTO Author VALUES(:Author_ID,:Author_Name,:Author_Age,:Email)",
                {
                  'Author_ID':Author_ID.get(),
                  'Author_Name':Author_Name.get(),
                  'Author_Age':Author_Age.get(),
                  'Email':Email.get()
                })
    conn.commit()
    conn.close()

    Author_ID.delete(0, END)
    Author_Name.delete(0, END)
    Author_Age.delete(0, END)
    Email.delete(0, END)

def query():
    conn = sqlite3.connect("C:/Users/STUDENT4/DBdeza.db")
    c = conn.cursor()

    c.execute("Select*,oid FROM Author")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\n"

    query_label = Label(root,text = print_records)
    query_label.grid(row = 20,column = 0,columnspan = 2)

    conn.close()

def delete():
    conn = sqlite3.connect("C:/Users/STUDENT4/DBdeza.db")

    c = conn.cursor()

    
    c.execute("DELETE from Author WHERE oid="+delete_box.get())

    conn.commit()

    conn.close

def query_jr():
    conn = sqlite3.connect("DBdeza.db")
    c = conn.cursor()

    c.execute("Select*,oid FROM Author")
    records = c.fetchall()

    print_records=''
    x = 1
    for record in records:
        print_records += str(x) + ". " +str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " "  + "\n"
        x += 1

    query_label=Label(root,text=print_records)
    query_label.grid(row=25,column=0,columnspan=2)

    conn.commit()

    conn.close()
     
    




root = Tk()
root.title("Author")
root.geometry("500x500")

conn = sqlite3.connect('DBdeza.db')

c = conn.cursor()

'''

c.execute("""CREATE TABLE "Author" (
	"Author_ID"	INTEGER,
	"Author_Name"	TEXT,
	"Author_Age"	NUMERIC,
	"Email"	TEXT
)'''

#--------------------------------------------------------entry

Author_ID = Entry(root, width = 30)
Author_ID.grid(row = 0, column = 1, padx = 20)

Author_Name = Entry(root, width = 30)
Author_Name.grid(row = 1, column = 1, padx = 20)

Author_Age = Entry(root, width = 30)
Author_Age.grid(row = 2, column = 1, padx = 20)

Email = Entry(root, width = 30)
Email.grid(row = 3, column = 1, padx = 20)

#--------------------------------------------------------label

Author_ID_label = Label(root, text = "AuthorID")
Author_ID_label.grid(row = 0, column = 0)

Author_Name_label = Label(root, text = "AuthorName")
Author_Name_label.grid(row = 1, column = 0)

Author_Age_label = Label(root, text = "AuthorAge")
Author_Age_label.grid(row = 2, column = 0)

Email_label = Label(root, text = "Email")
Email_label.grid(row = 3, column = 0)

#--------------------------------------------------------button

submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, padx=30)

delete_box_label = Label(root, text="Select ID No.")
delete_box_label.grid(row=10, column=0)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=136)



conn.commit()

conn.close()

root.mainloop()
