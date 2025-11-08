# Build a fully functional text editor application with Tkinter! Students will learn to create file dialogs, read and write files, use text widgets for editing, and organize layouts with frames and grids. This project demonstrates real-world application development with file handling capabilities.
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
windows=Tk()
windows.geometry("500x500")
windows.title("Text Editor")
windows.config(bg="blue")
  
def open_file():
    file_path=askopenfilename(
        defaultextension="txt",
        filetypes=[("text files","*.txt"),("all files","*.*")]
    )
    if not file_path:
        return
    text_editor.delete(1.0,END)
    with open(file_path,"r") as input_file:
        T=input_file.read()
        text_editor.insert(END,T)
        input_file.close()
    windows.title(f"text editer={file_path}")

def save_file():
    file_path=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("text files","*.txt"),("all files","*.*")]
    )
    if not file_path:
        return
    with open(file_path,"w") as output_file:
        T=text_editor.get(1.0,END)
        output_file.write(T)
    windows.title(f"text editer={file_path}")
button_frame=Frame(master=windows,relief=RAISED)
button_open=Button(master=button_frame,text="open",command=open_file)
button_save_as=Button(master=button_frame,text="save as",command=save_file)
windows.rowconfigure(0,minsize=800,weight=1)
windows.columnconfigure(1,minsize=800,weight=1)
button_open.grid(row=0,column=0,sticky="ew",padx=5,pady=10)
button_save_as.grid(row=1,column=0,sticky="ew",padx=5)
button_frame.grid(row=0,column=0,sticky="ns")
text_editor=Text(windows)
text_editor.grid(row=0,column=1,sticky="nsew")
windows.mainloop()