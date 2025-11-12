from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
windows=Tk()
windows.geometry("500x500")
windows.config(bg="grey")
upload=Image.open("app_img.jpg")
upload=upload.resize((200,200))
image=ImageTk.PhotoImage(upload)
label_image=Label(windows,image=image,bg="grey")
label_image.place(x=150,y=50)
text=Label(windows,text="Hey user!Welcome to denomination counter application!",bg="grey")
text.place(x=110,y=280)
def msg():
    msg_box=messagebox.showinfo("alert","Do you want to calculate denominater")
    if msg_box=="ok":
        top()

def top():
    top_window=Toplevel()
    top_window.geometry("350x350")
    top_window.config(bg="grey")
    l1=Label(top_window,text="enter the total amount",bg="grey")
    entry1=Entry(top_window)
    l2=Label(top_window,text="Here are the number of notes",bg="grey")
    ll1=Label(top_window,text="2K",bg="grey")
    e1=Entry(top_window)
    ll2=Label(top_window,text="1K",bg="grey")
    e2=Entry(top_window)
    ll3=Label(top_window,text="500",bg="grey")
    e3=Entry(top_window)
    def calculate():
        try:
            global amount
            amount=int(entry1.get())
            notes_2K=amount//2000
            amount=amount%2000
            notes_1K=amount//1000
            amount=amount%1000
            notes_500=amount//500
            amount=amount%500
            e1.delete(0,END)
            e1.insert(END,str(notes_2K))
            e2.delete(0,END)
            e2.insert(END,str(notes_1K))
            e3.delete(0,END)
            e3.insert(END,str(notes_500))
        except ValueError:
            messagebox.showerror("error","plz enter valid number")
    calculate_btn=Button(top_window,text="Lets calculate",bg="red",command=calculate)
    l1.place(x=50,y=50)
    entry1.place(x=50,y=80)
    l2.place(x=50,y=100)
    ll1.place(x=100,y=150)
    e1.place(x=150,y=150)
    ll2.place(x=100,y=200)
    e2.place(x=150,y=200)
    ll3.place(x=100,y=250)
    e3.place(x=150,y=250)
    calculate_btn.place(x=170,y=270)
button=Button(text="Lets get started",bg="red",command=msg)
button.place(x=200,y=350)
windows.mainloop()