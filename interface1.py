import pygame,time
from tkinter import *
import pygame_widgets as pw
from pygame.locals import *
# import sys
import interface2
import help
global string 
string = ''
is_muted = False
def window1():
    color_light = (0, 0, 0 )

    # dark shade of the button
    color_dark = (88, 88, 88)
    pygame.init()
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play()
    # time.sleep(2)
    # pygame.mixer.music.stop()
    window_width = 1000
    window_height = 600
    window =pygame.display.set_mode((window_width, window_height))

    image = pygame.image.load("start.png")
    image = image.convert()
    image = pygame.transform.scale(image, (1000, 700))
    mute_img = pygame.image.load("mute.png")
    unmute_img = pygame.image.load("unmute.png")

    smallfont1 = pygame.font.Font('december-holidays.ttf', 100)
    text1 = smallfont1.render('CHINESE CHECKERS', True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = (460, 120)

    def toggle_mute():
        global is_muted
        is_muted = not is_muted
    
    clock = pygame.time.Clock()
    #button
    def quit():
        window.distroy()

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
    running = True
    mute_rect = mute_img.get_rect()
    

    unmute_rect = unmute_img.get_rect()
    while running:
        scaled_image = pygame.transform.scale(image, (window_width, window_height))
        window.blit(scaled_image, (0, 0))
        # window.blit(pygame.transform.scale(image, (900, 600)), (0, 0))
        window.blit(text1, textRect1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mute_rect.collidepoint(event.pos):
                    toggle_mute()
        
                if is_muted:
                    window.blit(mute_img, mute_rect)
                    pygame.mixer.music.stop()
                else:
                    window.blit(unmute_img, unmute_rect)
                    pygame.mixer.music.play()

        button("Play Game", 380, 270, 150, 50, color_dark, color_light,interface2.window2)
        button("Quit", 10, 400, 88, 30, color_dark, color_light, quit)
        button("Help", 10, 450, 88, 30, color_dark, color_light, help.help)
        rect1 = pygame.draw.rect(window, color_dark, pygame.Rect(374, 264, 162, 62), 6, 20)
        rect = pygame.draw.rect(window, color_dark, pygame.Rect(374, 264, 162, 62), 6, 20)
        rect2 = pygame.draw.rect(window, color_dark, pygame.Rect(4, 394, 100, 42), 6, 20)
        rect3 = pygame.draw.rect(window, color_dark, pygame.Rect(4, 444, 100, 42), 6, 20)
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()

    


    pygame.quit()
window1()