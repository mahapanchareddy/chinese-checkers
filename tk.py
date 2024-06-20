#Import the required library
from tkinter import *
import pygame
#Create an instance of tkinter frame
def winner():
    win= Tk()

    #Set the geometry
    win.geometry("1500x1000")
    # image = pygame.image.load("won.png")
    # image = image.convert()
    # label1 = Label( win, image = bg)
    # label1.place(x = 0, y = 0)
    #Create a canvas object
    canvas= Canvas(win, width= 1000, height= 750, bg="pink")

    #Add a text in Canvas
    canvas.create_text(550, 350, text="YOU WON THE GAME!", fill="black", font=('Helvetica 50 bold'))
    canvas.pack()

    win.mainloop()