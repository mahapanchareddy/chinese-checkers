import pygame
import sys
import interface2
import trial
import tk,tk1

color_light = (202, 203, 213 )
color_dark = (2, 6, 145)


def OnePlayers():
    pygame.init()
    sound = pygame.mixer.Sound('Small bell.mp3')
    
    import numpy
    matrix = numpy.ones((17, 25))
   
    matrix *= -1
    first_player = [[0,12], [1, 11],[1,13], [2, 10],[2,12],[2, 14], [3, 9], [3, 11], [3, 13], [3, 15],[4,8],[4,10],[4,12],[4,14],[4,16]]
    h = trial.string
    if h == "1":
        first_player.pop(0)
    elif h == "2":
        first_player.pop(1)
    elif h == "3":
        first_player.pop(2)
    elif h == "4":
        first_player.pop(3)
    elif h == "5":
        first_player.pop(4)
    elif h == "6":
        first_player.pop(5)
    elif h == "7":
        first_player.pop(6)
    elif h == "8":
        first_player.pop(7)
    elif h == "9":
        first_player.pop(8)
    elif h == "10":
        first_player.pop(9)
    elif h == "11":
        first_player.pop(10)
    elif h == "12":
        first_player.pop(11)
    elif h == "13":
        first_player.pop(12)
    elif h == "14":
        first_player.pop(13)
    elif h == "15":
        first_player.pop(14)
    
    move_index = [[-1, -1], [-1, 1], [0, 2], [1, 1], [1, -1], [0, -2]]
   
    #-1 is white , 1 is red, 0 is grey
    matrix_index = [1, 2, 3, 4, 13, 12, 11, 10, 9]
    for i in range(9):
        j = 12
        first_time = True
        while matrix_index[i] > 0:
            if (i % 2 == 0) and first_time:
                first_time = False
                matrix[i][j] = matrix[16 - i][j] = 0

                matrix_index[i] -= 1
            else:
                j -= 1
                matrix[i][j] = matrix[i][24 - j] = matrix[16 - i][j] = matrix[16 - i][24 - j] = 0
                matrix_index[i] -= 2
            j -= 1
    for i in range(5,16):
        for j in range(0,23):
            matrix[i][j]=-1
    for j in range(0,7):
        matrix[4][j] = -1
    for j in range(17,25):
        matrix[4][j] = -1
    matrix[5][23] = -1

    for i in range(5,16):
        for j in range(0,23):
            matrix[i][j]=-1
    for j in range(0,7):
        matrix[4][j] = -1
    for j in range(17,25):
        matrix[4][j] = -1
    matrix[5][23] = -1
    matrix[11][23] = -1
    matrix[12][24] = -1
    matrix[16][12] = -1

    def add_player(index):
        if index == 1:
            for i in range(len(first_player)):
                matrix[first_player[i][0]][first_player[i][1]] = index
        
    # adding each players pawns
    class remplissage:
        def __init__(self):
            self_x = 0
            self_y = 0

        def pion(self):
            colors = [(240, 230, 230), "red"]
            for i in range(0, 17):
                for j in range(0, 25):
                    if matrix[i][j] >= 0:
                        rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pions_rect.append(pygame.draw.rect(screen, colors[int(matrix[i][j])], rect, border_radius=20))
    
    #possible moves
    def valid_moves(coor):
        valid_index = []
        for i in range(len(move_index)):
            x = coor[0] + move_index[i][0]
            y = coor[1] + move_index[i][1]
            if -1 < x < 17 and -1 < y < 25:
                if matrix[x][y] != -1 or matrix[x][y] != 0 :
                    check_path(move_index[i], x, y, valid_index)

        return valid_index

    def check_path(path_coor, x, y, moves_array):
        x2 = x + path_coor[0]
        y2 = y + path_coor[1]
        if [x2, y2] not in moves_array:
            if -1 < x2 < 17 and -1 < y2 < 25:
                if matrix[x2][y2] == 0:
                    moves_array.append([x2, y2])
                    for j in range(len(move_index)):
                        x3 = x2 + move_index[j][0]
                        y3 = y2 + move_index[j][1]
                        if [x3, y3] not in moves_array:
                            if -1 < x3 < 17 and -1 < y3 < 25:
                                if matrix[x3][y3] > 0:
                                    check_path(move_index[j], x3, y3, moves_array)

    # to make the move
    def move(pos, target):
        sound.play()
        matrix[target[0]][target[1]] = matrix[pos[0]][pos[1]]
        matrix[pos[0]][pos[1]] = 0
        if(pos[0] == target[0]):
            if(target[1] > pos[1]):
                m = pos[1] + 2
                matrix[pos[0]][m] = 0 
            else:
                m = pos[1] - 2
                matrix[pos[0]][m] = 0
        elif(pos[0] > target[0]):
            if(target[1] > pos[1]):
                a = pos[0] - 1
                b = pos[1] + 1
                matrix[a][b] = 0 
            else:
                a = pos[0] - 1
                b = pos[1] - 1
                matrix[a][b] = 0
        elif (pos[0]<target[0]):
            if(target[1] > pos[1]):
                c = pos[0] + 1
                d = pos[1] + 1
                matrix[c][d] = 0 
            else:
                c = pos[0] + 1
                d = pos[1] - 1
                matrix[c][d] = 0

    # the coordinates relative to the grid
    def get_token_coor(x, y):
        grid_width = 0
        grid_heigth = 0
        coor = [int((y - grid_heigth) / 20), int((x - grid_width) / 20)]
        return coor

    # animation of possible shifts
    def animation(moves=[], clicked_token=None):
        print(moves)
        colors = [(240, 230, 230), "red"]
        moves.append(clicked_token)
        for i in range(0, 17):
            for j in range(0, 25):
                if matrix[i][j] >= 0:
                    rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pions_rect.append(pygame.draw.rect(screen, colors[int(matrix[i][j])], rect, border_radius=20))
                if [i, j] in moves:
                    test_cercle = pygame.image.load('cercle.png')
                    test_cercle = pygame.transform.scale(test_cercle, (CELL_SIZE, CELL_SIZE))
                    screen.blit(test_cercle, (j * CELL_SIZE, i * CELL_SIZE))
       
    def WriteText(text, text_pos_x, text_pos_y, text_size, col):
        text_font = pygame.font.SysFont(None, text_size)
        text_render = text_font.render(text, True, col)
        screen.blit(text_render, (text_pos_x, text_pos_y))

   
    def winner():
        first = True
        c = count = 1
        first_player = [[0,12], [1, 11],[1,13], [2, 10],[2,12],[2, 14], [3, 9], [3, 11], [3, 13], [3, 15],[4,8],[4,10],[4,12],[4,14],[4,16]]
       
        for i in range(len(first_player)):
            if matrix[first_player[i][0]][first_player[i][1]] == 0:
                # print(True)
                c = count = count +  1

        if count == 15:
            win = pygame.mixer.Sound('win.mp3')
            win.play()
            WriteText('You have won!', nb_col * CELL_SIZE - 370, nb_ligne * CELL_SIZE - 130, 50, 'green')
            tk.winner()
            return True
        else:
            if count != 15:
                return False


    add_player(1)
    nb_col = 25
    nb_ligne = 25
    CELL_SIZE = 20
    screen = pygame.display.set_mode(size=(nb_col * CELL_SIZE, nb_ligne * CELL_SIZE))
    timer = pygame.time.Clock()
    game_on = True
    pions_rect = []

    players = remplissage()

    screen.fill(pygame.Color("white"))
    players.pion()
    player_index = 1
    is_selecting = False
    player_valid_moves = []
    last_selected_token = []

    def text_objects(text, font):
        textsurface =font.render(text,True , "white")
        return textsurface , textsurface.get_rect()
    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)
    
    font_size = pygame.font.Font(None, 45)

    while game_on:
        #player turn
        if player_index == 2: col = 'red'
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in pions_rect if s.collidepoint(pos)]
                
                if clicked_sprites:
                    clicked_token = get_token_coor(clicked_sprites[0].x, clicked_sprites[0].y)
                    print(clicked_token)
                    if matrix[clicked_token[0], clicked_token[1]] == player_index:
                        if clicked_token == last_selected_token:
                            is_selecting = False
                            last_selected_token = []
                            player_valid_moves = []
                            screen.fill(pygame.Color("white"))
                            animation()
                        else:
                            player_valid_moves = valid_moves(clicked_token)
                            last_selected_token = clicked_token
                            is_selecting = True
                            screen.fill(pygame.Color("white"))
                            animation(player_valid_moves,last_selected_token)
                    elif clicked_token in player_valid_moves:
                        move(last_selected_token, clicked_token)
                        winner()
                        is_selecting = False
                        last_selected_token = []
                        player_valid_moves = []
                        screen.fill(pygame.Color("white"))
                        player_index = (player_index+1) % 1
                        if player_index == 0:
                            player_index += 1

                        animation()
            
            button("back",400, 430, 70, 30, color_dark, color_light, interface2.window2)
            rect2 = pygame.draw.rect(screen, color_dark, pygame.Rect(394, 424, 82, 42), 6, 20)
        pygame.display.update()
        timer.tick(60)

