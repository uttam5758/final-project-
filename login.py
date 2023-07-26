import sqlite3
from tkinter import Frame, Tk, Label, Entry, Button, messagebox
from PIL import ImageTk, Image

def register():
    username = entry_username.get()
    password = entry_password.get()
    con = sqlite3.connect("project.db")
    cur = con.cursor()
    cur.execute('SELECT id from user where username = ? LIMIT 1',[username])
    data=cur.fetchone()
    
    if (len(username.strip())==0 or len(password.strip())==0):
        messagebox.showerror("Registration Error", "Username and password cannot be empty")
        return
    if data is not None:
        messagebox.showerror("Registration Error", "Username already exists!")
    else:
        cur.execute('INSERT INTO user (username,password) VALUES (?,?)',[username,password])
        con.commit()
        cur.close()
        messagebox.showinfo("Registration Successful", "Registration successful!")
        entry_username.delete(0, "end")
        entry_password.delete(0, "end")

def login():
    con = sqlite3.connect("project.db")
    cur = con.cursor()
    username = entry_username.get()
    password = entry_password.get()
    cur.execute('SELECT username from user where username = ? and password = ? LIMIT 1',[username,password])
    con.commit()
    data=cur.fetchone()    
    if data is not None:
        messagebox.showinfo("Login Successful", "Login successful!")  
        entry_username.delete(0, "end")
        entry_password.delete(0, "end")
        root.destroy()
        import main
    else:
        messagebox.showerror("Login Error", "Invalid username or password!")
        entry_username.delete(0, "end")
        entry_password.delete(0, "end")

def delete_user():
    con = sqlite3.connect("project.db")
    cur = con.cursor()
    username = entry_username.get()
    cur.execute('DELETE FROM user WHERE username = ?', [username])
    con.commit()
    cur.close()
    messagebox.showinfo("User Deletion", "User deleted successfully!")
    entry_username.delete(0, "end")
    entry_password.delete(0, "end")

def delete_all_accounts():
    try:
        con = sqlite3.connect("project.db")
        cur = con.cursor()
        cur.execute("DELETE FROM user")
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("Delete All Accounts", "All accounts deleted successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = Tk()
root.state("zoomed")
root.iconbitmap("library.ico")
root.minsize(width=400,height=400)
root.geometry("600x500")

image = Image.open("bookshelf.jpg")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)

background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_softwarica = Label(root, text="Softwarica Library", font=("Helvetica", 24), fg="white", bg="#3b3b3b")
label_softwarica.place(x=10, y=10)

login_frame = Frame(root, bg="#3b3b3b", width=300, height=200)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

label_username = Label(login_frame, text="Username:")
entry_username = Entry(login_frame)
label_password = Label(login_frame, text="Password:")
entry_password = Entry(login_frame, show="*")
button_register = Button(login_frame, text="Register Account", command=register)
button_login = Button(login_frame, text="Login", command=login)

label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username.grid(row=0, column=1, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
button_register.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

button_delete = Button(login_frame, text="Delete Account", command=delete_user)
button_delete.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

button_delete_all = Button(login_frame, text="Delete All Accounts", command=delete_all_accounts)
button_delete_all.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


def createTable():
    con = sqlite3.connect("project.db")
    cur = con.cursor()
    cur.executescript('''                
create table if not exists  books (bid text primary key,title text,author text,status text);           
create table if not exists  user (id text primary key,username text,password text);
create table if not exists books_issued (bid text primary key,
                      issued_to text);
''')
    con.commit()
    cur.close()
createTable()
root.mainloop()