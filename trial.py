#Import the required Libraries
from tkinter import *
from tkinter import ttk
global string
def text():
    global entry,string
    win= Tk()
    win.title("Enter your hole number")
    win.geometry("700x300")
    img= PhotoImage(file='bf.png', master= win)
    img_label= Label(win,image=img)

    img_label.place(x=0, y=0)
    def display_text():
        global string  
        string= entry.get()
        label.configure(text=string)
    label=Label(win, text="", font=("Courier 22 bold"))
    label.pack()

    entry= Entry(win, width= 40)
    entry.focus_set()
    entry.pack()
    ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)
    win.mainloop()

    


