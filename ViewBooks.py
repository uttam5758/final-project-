from tkinter import *
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = sqlite3.connect("project.db")
cur = con.cursor()

# Enter Table Names here
bookTable = "books"

def View():
    root = Tk()
    root.state("zoomed")
    root.iconbitmap("library.ico")
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Set the background color of the root window to green
    root.configure(bg="green")

    # Create a Frame
    frame = Frame(root)
    frame.pack(pady=20)
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Create a Canvas for book display
    book_display = Canvas(frame, bg="white", highlightthickness=0)
    book_display.pack(fill=BOTH, expand=YES)

    # Create Headings
    book_display.create_text(50, 20, text="Book ID", anchor=W, fill="black", font=("Arial", 12, "bold"))
    book_display.create_text(250, 20, text="Title", anchor=W, fill="black", font=("Arial", 12, "bold"))
    book_display.create_text(450, 20, text="Author", anchor=W, fill="black", font=("Arial", 12, "bold"))
    book_display.create_text(650, 20, text="Availability", anchor=W, fill="black", font=("Arial", 12, "bold"))

    # Fetch data from the database
    getBooks = "SELECT * FROM " + bookTable
    cur.execute(getBooks)
    rows = cur.fetchall()

    # Insert data into the Book Display
    y = 40
    for row in rows:
        book_display.create_text(50, y, text=row[0], anchor=W, fill="black", font=("Arial", 10))
        book_display.create_text(250, y, text=row[1], anchor=W, fill="black", font=("Arial", 10))
        book_display.create_text(450, y, text=row[2], anchor=W, fill="black", font=("Arial", 10))
        book_display.create_text(650, y, text=row[3], anchor=W, fill="black", font=("Arial", 10))
        y += 20

        quitBtn = Button(root,text="Quit",font=("Arial", 20),bg='#f7f1e3', fg='black', command=root.destroy)
        quitBtn.place(relx=0.40,rely=0.91, relwidth=0.18,relheight=0.08)

    root.mainloop()