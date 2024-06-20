import pygame
from tkinter import *
import pygame_widgets as pw
import OnePlayers
import help
import trial
global t
def window2():
    color_light = (0, 0, 0)
    # dark shade of the button
    color_dark = (88, 88, 88)
    pygame.init()
    window_width = 1000
    window_height = 600
    window =pygame.display.set_mode((window_width, window_height))

    image = pygame.image.load("photo.jpeg")
    image = image.convert()
    image = pygame.transform.scale(image, (1000, 700))

    image = image.convert()
    smallfont = pygame.font.Font('december-holidays.ttf',70)
    text = smallfont.render('CHOOSE THE INITIAL HOLE', True,(0,0,0 ))
    textRect=text.get_rect()
    textRect.center=(460,120)
    #button
    def text_objects(text,font):
        textsurface =font.render(text,True , "white")
        return textsurface , textsurface.get_rect()
    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(window, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(window, ic, (x, y, w, h))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        window.blit(textSurf, textRect)
    running= True
    while running:
      events = pygame.event.get()
      scaled_image = pygame.transform.scale(image, (window_width, window_height))
      window.blit(scaled_image, (0, 0))      
      window.blit(text,textRect)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running= False
      button("Holes", 360, 300, 50, 30, color_dark, color_light, trial.text)
      button("1", 430, 300, 50, 30, color_dark, color_light, OnePlayers.OnePlayers)
      button("Quit", 10, 400, 88, 30, color_dark, color_light, quit)
      button("Help", 10, 450, 88, 30, color_dark, color_light, help.help)
      #   rect0 = pygame.draw.rect(window, color_dark, pygame.Rect(213, 295, 62, 42), 6, 20)
      #   rect1 = pygame.draw.rect(window, color_dark, pygame.Rect(150, 295, 62, 42), 6, 20)
      rect2 = pygame.draw.rect(window, color_dark, pygame.Rect(4, 394, 100, 42), 6, 20)
      rect3 = pygame.draw.rect(window, color_dark, pygame.Rect(4, 444, 100, 42), 6, 20)
    #   rect4 = pygame.draw.rect(window, color_dark, pygame.Rect(284, 294, 62, 42), 6, 20)
      rect5 = pygame.draw.rect(window, color_dark, pygame.Rect(354, 294, 62, 42), 6, 20)
    #   rect6 = pygame.draw.rect(window, color_dark, pygame.Rect(424, 294, 62, 42), 6, 20)
    #   rect7 = pygame.draw.rect(window, color_dark, pygame.Rect(494, 294, 62, 42), 6, 20)
      pygame.display.update()
      pygame.display.flip()
    pygame.quit()





