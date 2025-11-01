# Create a visual number pad interface using Tkinter! Students will learn to use nested loops, grid layout management, frames, and labels to build a phone-style number pad with organized rows and columns.
from tkinter import *
window=Tk()
window.geometry("500x500")
#f1=Frame(master=window,bg="orange")
#f1.pack()
#f2=Frame(master=window,height=300,width=200,bg="tomato")
#f2.pack()
numbers=[[7,8,9],[4,5,6],[1,2,3],["*",0,"#"]]
for row_number in range(4):
    window.columnconfigure(row_number,weight=1,minsize=75)
    window.rowconfigure(row_number,weight=1,minsize=75)
    for column_number in range(3):
        frame=Frame(master=window,borderwidth=1,relief=RIDGE,highlightcolor="black")
        frame.grid(row=row_number,column=column_number)
        label=Label(master=frame,text=numbers[row_number][column_number])
        label.pack(padx=1,pady=1)
window.mainloop()