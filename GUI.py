# Create an interactive GUI application using Tkinter that greets users by name and displays today's date! Students will learn to build windows, add widgets, handle button clicks, and display dynamic messages in a text box.
from tkinter import *
windows=Tk()
windows.title("Food panda")
windows.geometry("300x300")
# label widgets
label_1=Label(text="welcome to Food panda",fg="black",bg="orange",height=1,width=300)
label_1.pack()
order_label=Label(text="What do you want to order?",fg="black",bg="white")
order_label.pack()
entry_order=Entry()
def display_msg():
    order=entry_order.get()
    global msg
    msg="Food panda sambhall le ga \n"
    confirm_order="Your "+order+" Order has been confirmed"
    text_box.insert(END,msg)
    text_box.insert(END,confirm_order)
text_box=Text(height=2)
button=Button(text="order now",command=display_msg,height=1,bg="blue",fg="black")
entry_order.pack()
button.pack()
text_box.pack()
windows.mainloop()

