from operator import imod
import sqlite3
from tkinter import *
from tkinter import messagebox
root=Tk()


# database connections 

conn =sqlite3.connect("data.db")
cur=conn.cursor()

# cur.execute("""
#             CREATE TABLE if not exists user_names(
#                 s_id INTERGER PRIMER KEY ,
#                 f_name TEXT ,
#                 l_name TEXT
                
#             )
            
#             """)

# conn.commit()
# conn.close()

def onSubmit():
    cur.execute("INSERT INTO user_names VALUES(?,?,?)",(s_id.get(),f_name.get(),l_name.get()))
    messagebox.showinfo("message","Succesfully stored")
    s_id.delete(0,END)
    f_name.delete(0,END)
    l_name.delete(0,END)
    conn.commit()



# tkinter
root.title("user input store")
root.geometry("400x400")
root.resizable(0,0)
label=Label(text="hello users")
label.pack()
s_id=Entry()
s_id.pack()
f_name=Entry()
f_name.pack()
l_name=Entry()
l_name.pack()
btn=Button(text="Submit",command=onSubmit)
btn.pack()

root.mainloop()
