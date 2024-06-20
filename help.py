from tkinter import *
def help():
    inter = Tk()
    inter.geometry("1080x720")    
    text1 = Label(inter,text="TRIANGULAR PEG PUZZLE",fg='#F1C40F',font=("verdana",30))
    text2 = Label(inter,text="Game Rules :",fg='#515A5A',font=("verdana",25))
    text3 = Label(inter,text= "The rules of the game are :\n1.Every jump must be a jump of a peg over a neighboring peg.\n2. There must be a space for the jumping peg to land in.\n3. Jumps can be made either on the diagonal or the horizontal lines.\n4. A peg that is jumped is removed--just like in checkers. ",font=("arial",15))
    canvas = Canvas(inter,width=1080,height=400) 
    canvas.place(x=0,y=300)
    text1.pack()
    text2.pack()
    text3.pack()
    inter.mainloop()
