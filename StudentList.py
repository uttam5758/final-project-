from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = sqlite3.connect("project.db")
cur = con.cursor()
# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"


def displayStudentList():
    root = Tk()
    root.state("zoomed")
    root.iconbitmap("library.ico")
    root.title("Student List")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Set the background color of the root window to green
    root.configure(bg="green")

    # Create a Frame
    frame = Frame(root)
    frame.pack(pady=(20, 0))
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Create a Canvas for student display
    student_display = Canvas(frame, bg="white", highlightthickness=0)
    student_display.pack(fill=BOTH, expand=YES)

    # Create Headings
    student_display.create_text(50, 20, text="Book ID", anchor=W, fill="black", font=("Arial", 12, "bold"))
    student_display.create_text(250, 20, text="Student Name", anchor=W, fill="black", font=("Arial", 12, "bold"))

    # Fetch data from the database
    getStudents = "SELECT * FROM " + issueTable
    cur.execute(getStudents)
    rows = cur.fetchall()

    # Insert data into the Student Display
    y = 40
    for row in rows:
        student_display.create_text(50, y, text=row[0], anchor=W, fill="black", font=("Arial", 10))
        student_display.create_text(250, y, text=row[1], anchor=W, fill="black", font=("Arial", 10))
        y += 20

    # Create a Quit Button
    quitBtn = Button(root,text="Quit",font=("Arial", 20),bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.pack(side=BOTTOM, pady=(20, 0))
    root.mainloop()