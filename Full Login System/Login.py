
from tkinter import * 
from tkinter import messagebox
import sqlite3
import hashlib

root=Tk()
# password 
# Initializing the sha256() method
sha256 = hashlib.sha256()


#database code
conn=sqlite3.connect("userAuthentication.db")
cur=conn.cursor()

cur.execute('''
            CREATE TABLE if not exists userAuthentication(
                username text,
                password text      
            )
            ''')

cur.execute('SELECT * FROM userAuthentication')

userLoginData=cur.fetchall()

# cur.execute('''
#             DELETE FROM userAuthentication         
#             ''')
# conn.commit()

# functions

def login():
    def verification():
        for i in userLoginData:
            if username.get()==i[0] and hashedInputPassword==i[1]:
                messagebox.showinfo("Login","Login successfully")
                return
        else:
            messagebox.showwarning("Login","Invalid credentials")
                
    if not username.get():
        messagebox.showwarning("Input Error","username is required")
        return
    if not userpassword.get():
        messagebox.showwarning("Input Error","password is required")
        return
    verification()

def root_window():
    root_register.destroy()
    root.deiconify()

def userRegisteration (username,password):
    cur.execute('INSERT INTO userAuthentication VALUES(?,?)',(username.get(),password))
    conn.commit()
    messagebox.showinfo("register","Registered successfully")  
    root_window()

def register_page(b):
    root.withdraw() 
    global root_register 
    
    def register(username_r,userPassword,userConfirmPassword,hashPassword):
        if not username_r.get():
            messagebox.showwarning("Input Error","username is required")
            return 
        if not userPassword.get():
            messagebox.showwarning("Input Error","password is required")
            return
        if not userConfirmPassword.get():
            messagebox.showwarning("Input Error","Confirm password is required")
            return
        if userPassword.get() != userConfirmPassword.get():
            messagebox.showwarning("Error", "Passwords do not match")
            return
        userRegisteration(username_r,hashPassword)
       
    root_register=Toplevel(root)
    root_register.grid_columnconfigure(0, weight=1)
    root_register.geometry("600x450")
    root_register.resizable(0,0)
    root_register.title("Register page")
    lblt=Label(root_register,
                text="Register page",
                bg="#00aa00",
                fg="white",
                height=2,
                font=("The new romans",16,"bold"))
    # Center horizontally
    lblt.grid(row=0, column=0, sticky="we")   
      
    # user input username here
    user_name_lbl_r=Label(root_register,text="User Name",font=("arial",10))
    user_name_lbl_r.grid(row=1,column=0,sticky="ns",padx=20,pady=(40,0))
    username_r=Entry(root_register,width=30)
    username_r.grid(row=2,column=0,sticky="ns",ipadx=(2),ipady=(2))

    #user input passowrd here
    user_password_lbl=Label(root_register,text="password",font=("arial",10))
    user_password_lbl.grid(row=3,column=0,sticky="ns",padx=20,pady=(20,0))
    userPassword=Entry(root_register,width=30,show="*")
    userPassword.grid(row=4,column=0,sticky="ns",ipadx=(2),ipady=(2))
    

    #user input confirm zpassowrd here
    user_password_lbl=Label(root_register,text="confirm password",font=("arial",10))
    user_password_lbl.grid(row=5,column=0,sticky="ns",padx=20,pady=(20,0))
    userConfirmPassword=Entry(root_register,width=30,show="*")
    userConfirmPassword.grid(row=6,column=0,sticky="ns",ipadx=(2),ipady=(2))
    
# -------------hashlib hashing user password ------------------------

    # Passing the byte stream as an argument
    password=userPassword.get()
    password_byte=password.encode()
    sha256.update(password_byte)
    hashPassword=sha256.hexdigest()
    
        
    btn=Button(root_register,text="Register",bd=1,relief="solid",font=("The new romans",12,"bold"),width=10, anchor="center",command=lambda:register(username_r,userPassword,userConfirmPassword,hashPassword))
    btn.grid(row=7,column=0,pady=(30, 0))
    root_register.protocol("WM_DELETE_WINDOW", root_window) 
    
root.title("Login")
root.geometry("600x450")
root.resizable(0,0)
root.grid_columnconfigure(0, weight=1)

lbl=Label(
    text="Login page",
    bg="#00aa00",
    fg="white",
    height=2,
    font=("The new romans",16,"bold"))
lbl.grid(row=0,column=0,sticky="ew")


# user input username here
user_name_lbl=Label(text="User Name",font=("arial",10))
user_name_lbl.grid(row=1,column=0,sticky="ns",padx=20,pady=(40,0))
username=Entry(root,width=30)
username.grid(row=2,column=0,sticky="ns",ipadx=(2),ipady=(2))


#user input passowrd here
user_password_lbl=Label(text="Password",font=("arial",10))
user_password_lbl.grid(row=3,column=0,sticky="ns",padx=20,pady=(20,0))
userpassword=Entry(root,width=30,show="*")
userpassword.grid(row=4,column=0,sticky="ns",ipadx=(2),ipady=(2))


# hashing user input password
inputPassword=userpassword.get()
inputPassword_byte=inputPassword.encode()
sha256.update(inputPassword_byte)
hashedInputPassword=sha256.hexdigest()


# login btn
btn=Button(text="Login",bd=1,relief="solid",font=("The new romans",12,"bold"),width=10, anchor="center",command=login)
btn.grid(row=5,column=0,pady=(30, 0))

# dont have account? register button
register_lbl = Label(root, text="Don't have account? Register", fg="blue", cursor="hand2")
register_lbl.grid(row=6,column=0,pady=(10, 0))
register_lbl.bind("<Button-1>",register_page) 

root.mainloop()

conn.close()