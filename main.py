from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from StudentList import *


def createTable():
    con = sqlite3.connect("project.db")
    cur = con.cursor()
    cur.executescript('''
create table if not exists  books (bid text primary key,title text,author text,status text);
create table if not exists books_issued (bid text primary key,
                      issued_to text);
''')
    # con.commit()
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = sqlite3.connect("project.db")
cur = con.cursor()

def logout():
    root.destroy()  # Close the main page (root) window
    import login  # Import the login page to go back to it

root = Tk()
root.state("zoomed")
root.iconbitmap("library.ico")
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("library.ico")
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.08)

headingLabel = Label(headingFrame1, text="Welcome to Softwarica Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn1.place(relx=0.28,rely=0.2, relwidth=0.45,relheight=0.08)

btn2 = Button(root,text="Add New Book",bg='black', fg='white', command=addBook)
btn2.place(relx=0.28,rely=0.28, relwidth=0.45,relheight=0.08)
    
btn3 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn3.place(relx=0.28,rely=0.36, relwidth=0.45,relheight=0.08)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.44, relwidth=0.45,relheight=0.08)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.52, relwidth=0.45,relheight=0.08)

btn6 = Button(root, text="View Student List", bg='black', fg='white', command = displayStudentList)
btn6.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.08)

btn_logout = Button(root, text="Logout", bg='black', fg='white', command=logout)
btn_logout.place(relx=0.41, rely=0.75, relwidth=0.16, relheight=0.08)

createTable()
root.mainloop()