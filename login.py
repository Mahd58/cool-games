# Create a user registration form with Tkinter! Students will learn to build a login interface with text input fields, password masking, button functionality, and message display. Perfect for understanding form creation and user interaction in GUI applications.
from tkinter import *
window=Tk()
window.geometry("500x500")
f1=Frame(master=window,bg="cyan",height=300,width=200)
f1.place(x=100,y=50)
l1=Label(master=f1,text="full name")
l2=Label(master=f1,text="email id")
l3=Label(master=f1,text="password")
name_entry=Entry(master=f1)
password_entry=Entry(master=f1)
email_entry=Entry(master=f1)
def display_msg():
    name=name_entry.get()
    global msg
    msg="Congragulations your account has been created!"
    confirm_order="welcome"+name
    text_box.insert(END,msg)
    text_box.insert(END,confirm_order)
text_box=Text(height=2)
button=Button(text="create account",command=display_msg,height=1,bg="blue",fg="black")
l1.place(x=80,y=50)
name_entry.place(x=50,y=80)
l2.place(x=80,y=110)
email_entry.place(x=50,y=140)
l3.place(x=80,y=170)
password_entry.place(x=50,y=200)
button.place(x=150,y=300)
text_box.place(x=20,y=350)
window.mainloop()