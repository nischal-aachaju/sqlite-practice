
from tkinter import * 
from tkinter import messagebox
import sqlite3


root=Tk()

# functions
def register(b):
    print(b)
    root_register=Tk()
    root_register.geometry("600x450")
    root_register.resizable(0,0)
    lblt=Label(text="hello,register page")
    lblt.pack()
    root_register.mainloop()
    

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


btn=Button(text="Login",bd=1,relief="solid",font=("The new romans",12,"bold"),width=10, anchor="center",)
btn.grid(row=5,column=0,pady=(30, 0))

register_lbl = Label(root, text="Don't have account? Register", fg="blue", cursor="hand2")
register_lbl.grid(row=6,column=0,pady=(10, 0))
register_lbl.bind("<Button-1>",register) 
# btn=Button(text="Don't have account? Register",font=("The new romans",12,),width=20, anchor="center",)
# btn.grid(row=6,column=0,pady=(2))

root.mainloop()