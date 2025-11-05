# Learn to handle keyboard and mouse events in Tkinter! Students will create an interactive application that responds to key presses and button clicks, understanding event-driven programming and event binding concepts.
from tkinter import *
windows=Tk()
windows.geometry("500x500")
windows.config(bg="pink")
button=Button(text="click me")
button.pack()
def handle_click(event):
   print("button got clicked")
   event.widget.config(bg="orange")
button.bind("<Button-1>",handle_click)    
windows.mainloop()