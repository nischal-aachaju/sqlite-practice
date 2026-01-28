from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib

root = Tk()

# ---------------- DB SETUP ----------------
conn = sqlite3.connect("userAuthentication.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userAuthentication(
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()

# cur.execute('''
#             DELETE FROM userAuthentication         
#             ''')
# conn.commit()


def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

# ---------------- WINDOW HELPERS ----------------
root_register = None

def show_root_window():
    global root_register
    root_register.destroy()
    root.deiconify()

def open_register_page(event=None):
    global root_register
    root.withdraw()
    
    root_register = Toplevel(root)
    root_register.geometry("600x450")
    root_register.resizable(0, 0)
    root_register.title("Register page")
    root_register.grid_columnconfigure(0, weight=1)

# top login text
    lblt = Label(
        root_register,
        text="Register page",
        bg="#00aa00",
        fg="white",
        height=2,
        font=("Times New Roman", 16, "bold"),)
    lblt.grid(row=0, column=0, sticky="we")
# register page
# username  
    Label(root_register, text="User Name", font=("arial", 10)).grid(row=1, column=0, pady=(40, 0))
    username_r = Entry(root_register, width=30)
    username_r.grid(row=2, column=0, ipady=2)

# password
    Label(root_register, text="Password", font=("arial", 10)).grid(row=3, column=0, pady=(20, 0))
    userPassword = Entry(root_register, width=30, show="*")
    userPassword.grid(row=4, column=0, ipady=2)

# confirm password
    Label(root_register, text="Confirm Password", font=("arial", 10)).grid(row=5, column=0, pady=(20, 0))
    userConfirmPassword = Entry(root_register, width=30, show="*")
    userConfirmPassword.grid(row=6, column=0, ipady=2)


    def register():
        u = username_r.get().strip()
        p1 = userPassword.get()
        p2 = userConfirmPassword.get()

        if not u:
            messagebox.showwarning("Input Error", "username is required")
            return
        if not p1:
            messagebox.showwarning("Input Error", "password is required")
            return
        if not p2:
            messagebox.showwarning("Input Error", "Confirm password is required")
            return
        if p1 != p2:
            messagebox.showwarning("Error", "Passwords do not match")
            return

        hp = hash_pw(p1)

        # Check if user already exists
        cur.execute("SELECT 1 FROM userAuthentication WHERE username=?", (u,))
        if cur.fetchone():
            messagebox.showwarning("Register", "Username already exists")
            return

        cur.execute("INSERT INTO userAuthentication(username, password) VALUES(?, ?)", (u, hp))
        conn.commit()

        messagebox.showinfo("Register", "Registered successfully")
        show_root_window()

    Button(
        root_register,
        text="Register",
        bd=1,
        relief="solid",
        font=("Times New Roman", 12, "bold"),
        width=10,
        command=register,).grid(row=7, column=0, pady=(30, 0))

    root_register.protocol("WM_DELETE_WINDOW", show_root_window)

# ---------------- LOGIN LOGIC ----------------
def login():
    u = username.get().strip()
    p = userpassword.get()

    if not u:
        messagebox.showwarning("Input Error", "username is required")
        return
    if not p:
        messagebox.showwarning("Input Error", "password is required")
        return

    hp = hash_pw(p)

    cur.execute("SELECT password FROM userAuthentication WHERE username=?", (u,))
    row = cur.fetchone()

    if row and row[0] == hp:
        messagebox.showinfo("Login", "Login successfully")
    else:
        messagebox.showwarning("Login", "Invalid credentials")

# ---------------- UI (LOGIN PAGE) ----------------
root.title("Login")
root.geometry("600x450")
root.resizable(0, 0)
root.grid_columnconfigure(0, weight=1)

Label(
    root,
    text="Login page",
    bg="#00aa00",
    fg="white",
    height=2,
    font=("Times New Roman", 16, "bold"),
).grid(row=0, column=0, sticky="ew")

#user input username here
Label(root, text="User Name", font=("arial", 10)).grid(row=1, column=0, pady=(40, 0))
username = Entry(root, width=30)
username.grid(row=2, column=0, ipady=2)

#user input passowrd here
Label(root, text="Password", font=("arial", 10)).grid(row=3, column=0, pady=(20, 0))
userpassword = Entry(root, width=30, show="*")
userpassword.grid(row=4, column=0, ipady=2)

Button(
    root,
    text="Login",
    bd=1,
    relief="solid",
    font=("Times New Roman", 12, "bold"),
    width=10,
    command=login,).grid(row=5, column=0, pady=(30, 0))

# Don't have account ? register button
register_lbl = Label(root, text="Don't have account? Register", fg="blue", cursor="hand2")
register_lbl.grid(row=6, column=0, pady=(10, 0))
register_lbl.bind("<Button-1>", open_register_page)

root.mainloop()
conn.close()
