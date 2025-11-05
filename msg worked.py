# Create a virus scanner simulation with pop-up alerts using Tkinter! Students will learn to use messagebox to display warning dialogs, understand button commands, and create interactive alert systems for desktop applications.
from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("500x500")
window.config(bg="orange")
def msg():
    messagebox.showwarning("alert","Last chance!")
button=Button(text="scan virus",bg="red",command=msg)
button.place(x=250,y=0)
def eroor():
    messagebox.showerror("error found","error found")
button_2=Button(text="Enter",bg="yellow",command=eroor)
button_2.place(x=250,y=250)
def info():
    messagebox.showinfo("your info alert","your info is really getting hacked")
show_info=Button(text="your info",bg="brown",command=info)
show_info.place(x=250,y=400)
window.mainloop()