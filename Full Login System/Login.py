
from tkinter import * 
from tkinter import messagebox
import sqlite3

# problem is; when btn register is clicked and all the input are oaky
# then functon new_window should be exicute , 
# but when any is required run then our register page is destroing 
# so it should be prevent this
# soln is: when all things is done and succesfylly data is addes to database then new_window() should exicute
root=Tk()

# functions

def login():
    if not username.get():
        messagebox.showwarning("Input Error","username is required")
        return
    if not userpassword.get():
        messagebox.showwarning("Input Error","password is required")
    return
def new_window():
    root_register.destroy()
    root.deiconify()
    root_register.protocol("WM_DELETE_WINDOW",new_window)

def register_page(b):

    
    root.withdraw()
    def register():
    
        if not username_r.get():
            messagebox.showwarning("Input Error","username is required")
            return
            
        if not userPassword.get():
            messagebox.showwarning("Input Error","password is required")
            return
        if not userConfirmPassword.get():
            messagebox.showwarning("Input Error","Confirm password is required")
            return

    
    global root_register
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

    btn=Button(root_register,text="Register",bd=1,relief="solid",font=("The new romans",12,"bold"),width=10, anchor="center",command=register)
    btn.grid(row=7,column=0,pady=(30, 0))
    

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


btn=Button(text="Login",bd=1,relief="solid",font=("The new romans",12,"bold"),width=10, anchor="center",command=login)
btn.grid(row=5,column=0,pady=(30, 0))

register_lbl = Label(root, text="Don't have account? Register", fg="blue", cursor="hand2")
register_lbl.grid(row=6,column=0,pady=(10, 0))
register_lbl.bind("<Button-1>",register_page) 
# btn=Button(text="Don't have account? Register",font=("The new romans",12,),width=20, anchor="center",)
# btn.grid(row=6,column=0,pady=(2))

root.mainloop()