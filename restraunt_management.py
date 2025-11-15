# Create a Restaurant order Management using the Python library Tkinter.
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
class restrauntordermannagement:
    def __init__(self,main_window):
        self.main_window=main_window
        self.main_window.title("restraunnt management")
        self.menu={
            "Beef Burger":2000,
            "Pizza":890,
            "Cocacola":500,
            "Noodles":200,
            "Popcorn":100
        }
        self.setup_background(main_window)
        frame=ttk.Frame(main_window)
        frame.place(relx=0.5,rely=0.5)
        ttk.Label(main_window,text="restraunt order management",bg="orange")
        self.menu_label={}
        self.menu_quontiti={}
        for i,(item,price) in enumerate(self.menu.items(),start=1):
            label=ttk.Label(main_window,text=f"{item} (PKR{price})",bg="orange")
            label.grid(row=i,column=0,padx=10,pady=5)
            q_entry=ttk.Entry(main_window,width=5)
            q_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_label[item]=label
            self.menu_quontiti[item]=q_entry
            order_button=ttk.Button(main_window,text="place order",bg="orange",command=self.place_order)
            order_button.grid(row=7,columnspan=3,padx=10,pady=5)
    def place_order(self,main_window):
        messagebox.showinfo("order placed","Thank you for visiting")


    def setup_background(self,main_window):
        canvas=tk.Canvas(main_window,width=600,height=600)
        canvas.pack()
        #upload=Image.open("restraunt_bg.jpg")
        # upload=upload.resize((200,200))
        image=tk.PhotoImage(file="restraunt_bg.jpg")
        bg_image=image.subsample(image.width()//600,image.height()//600)
        canvas.create_image(0,0,anchor=tk.NW,image=bg_image)
        canvas.image=bg_image
if __name__=="__main__":
    main_window=tk.Tk()
    ob1=restrauntordermannagement(main_window)
    main_window.geometry("500x500")
    main_window.mainloop()