"""
Projecto: "2048 - Modo Gráfico"

Desenvolvido por: Jorge Miguel Coelho Silva
                  A44615

Desenvolvido para: Projecto - Matemática Discréta e Programação

Ficheiros referentes ao jogo 2048:

    - Motor  - j2048_motor_A44615.py
             - Toda a informação relacionada com a logica do jogo
        
    - Testes - j2048_modo_texto_A44615.py
             - Zona de testes
        
    - Gestor - j2048_gestor_A44615.py
             - Analisa, regista e envia o ficheiro para confirmação posterior

Informações do motor:

    - Funções e constantes estão escritas em Inglês
    
    - Comentários as construcções lógicas em Português

Guia de referências:

    ## Zona de comentários informativos a cada bloco/linha de código
    
Update Log:

    - 2017-12-29 - Criação do modo Gráfico usando PyGame

"""

#Import pygame module
import pygame
from pygame.locals import *
from j2048_motor_A44615 import *

#Ini pygame module
pygame.init()

#Sound Settings
intro_music      = pygame.mixer.Sound("intro.wav")

#Window Setting
width            = 800
height           = 600
w_resolution     = (width, height)

pygame.display.set_caption('2048 - Modo Gráfico - A44615')

window           = pygame.display.set_mode(w_resolution)

#Graphic settings
frame_rate       = 20 #>60 pref (PC MASTER RACE)
clock            = pygame.time.Clock() # Clock to control frame rate
antialias        = True # Default "True", set "False" to lower details
frame            = 0
frame_position_x = int(width/2)  # Frame Display Position in x
frame_position_y = int(height/2) # Frame Display Position in y

#Game Settings
background_color = (187, 173, 160) # Default background color - Grey
done             = False # Main cycle control
status           = None

#Default Color Settings
white            = (255, 255, 255)
grid_empty       = (204, 192, 179)
grid_2           = (238, 228, 218)
grid_4           = (237, 224, 200)
grid_8           = (242, 177, 121)
grid_16          = (245, 149,  99)
grid_32          = (246, 124,  95)
grid_64          = (246,  94,  59)
grid_128_1024    = (237, 207, 114)
grid_256         = (237, 204,  97)
grid_2048        = (237, 194,  46)
grid_4096        = ( 62,  57,  51)
red              = (255,   0,   0)
black            = (  0,   0,   0)

#Image Loading

i_introBg        = pygame.image.load("introbg.bmp")
i_fader          = pygame.image.load("loading.bmp")
i_smallLogo      = pygame.image.load("smalllogo.bmp")
i_menuBg         = pygame.image.load("menu.bmp")
i_newgame        = pygame.image.load("img_newgame.bmp")
io_newgame       = pygame.image.load("imgOver_newgame.bmp")
i_score          = pygame.image.load("img_score.bmp")
io_score         = pygame.image.load("imgOver_score.bmp")
i_about          = pygame.image.load("img_about.bmp")
io_about         = pygame.image.load("imgOver_about.bmp")
i_quit           = pygame.image.load("img_quit.bmp")
io_quit          = pygame.image.load("imgOver_quit.bmp")
i_gamebg         = pygame.image.load("gamebg.bmp")
i_gamebgdif      = pygame.image.load("gamebg_dif.bmp")
io_gamebgdif     = pygame.image.load("over_gamebg_dif.bmp")
i_gamenew        = pygame.image.load("img_ngameN.bmp")
io_gamenew       = pygame.image.load("imgOver_ngameN.bmp")
i_gamequit       = pygame.image.load("img_ngameQ.bmp")
io_gamequit      = pygame.image.load("imgOver_ngameQ.bmp")
i_dif_easy       = pygame.image.load("img_dif_easy.bmp")
io_dif_easy      = pygame.image.load("img_dif_easyul.bmp")
i_dif_easy_t     = pygame.image.load("img_dif_easy_text.bmp")
i_dif_classic    = pygame.image.load("img_dif_classic.bmp")
io_dif_classic   = pygame.image.load("img_dif_classicul.bmp")
i_dif_classic_t  = pygame.image.load("img_dif_classic_text.bmp")
i_dif_medium     = pygame.image.load("img_dif_medium.bmp")
io_dif_medium    = pygame.image.load("img_dif_mediumul.bmp")
i_dif_medium_t   = pygame.image.load("img_dif_medium_text.bmp")


#Font Loader
f_pixel          = pygame.font.Font("Pixel_font.otf", 24)
f_pixel_warning  = pygame.font.Font("Pixel_font.otf", 14)
f_default_color  = (170, 126, 114) # Default font color - White

#Global variable

dificult = None

#Game Start
game = new_game()

   
#Introduction to the game
def loading():

    global status

    pygame.mixer.Sound.play(intro_music)
      
    window.blit(i_introBg, (0,0))
    pygame.display.flip()
    pygame.time.delay(5000)
    for i in range(60):
        i_fader.set_alpha(i)
        window.blit(i_fader, (0,0))
        pygame.display.flip()
        
        pygame.time.delay(60)

        status = 1

def g_dificult():

    global dificult

    dif_process = True

    while dif_process:

        process_events()
        mouse = pygame.mouse.get_pos()

        #go back
        if 660+30 > mouse[0] > 660 and 171+30 > mouse[1] > 171:
            window.blit(io_gamebgdif, (0,0))
            text = f_pixel_warning.render("voltar", 1, red)
            window.blit(text, (390,340))
            if pygame.mouse.get_pressed()[0]:
                menu()
        else:
            window.blit(i_gamebgdif, (0,0))
        #Easy    
        if 210+80 > mouse[0] > 210 and 280+25 > mouse[1] > 280:
            window.blit(io_dif_easy, (185,268))
            window.blit(i_dif_easy_t, (245,320))
            if pygame.mouse.get_pressed()[0]:
                dificult = "easy"
                dif_process = False
        else:
            window.blit(i_dif_easy, (185,268))
        #Classic
        if 355+120 > mouse[0] > 355 and 280+25 > mouse[1] > 280:
            window.blit(io_dif_classic, (345,265))
            window.blit(i_dif_classic_t, (245,320))
            if pygame.mouse.get_pressed()[0]:
                dificult = "classic"
                dif_process = False
                game = new_game()
        else:
            window.blit(i_dif_classic, (345,265))
        #Medium
        if 550+65 > mouse[0] > 550 and 280+25 > mouse[1] > 280:
            window.blit(io_dif_medium, (520,272))
            window.blit(i_dif_medium_t, (245,320))
            if pygame.mouse.get_pressed()[0]:
                dificult = "medium"
                dif_process = False
        else:
            window.blit(i_dif_medium, (520,272))
            
        pygame.display.flip()
    game = new_game()
    g_newgame()

    print("Dificult set to: " + str(dificult))
    return dificult

def g_newgame():

    global dificult
    global game
    global status
    
    gamerunning = True
    
    while gamerunning:

        process_events()

        points                  = total_points(game)
        str_points              = str(points)
        points_size             = 54 - 2 * len(str_points)
        font_points             = pygame.font.Font("Pixel_font.otf", points_size)
        points_render           = font_points.render(str_points, 1 , black)
        surface_points          = points_render.get_rect()
        surface_points.center   = (690,210)
        window.blit(points_render, surface_points)
        
        pygame.display.flip()
        
        mouse = pygame.mouse.get_pos()

        window.blit(i_gamebg, (0,0))
        #Start the game
     
        
        #New Game button
        if 600+180 > mouse[0] > 600 and 327+45 > mouse[1] > 327:
            window.blit(io_gamenew, (600,327))
            if pygame.mouse.get_pressed()[0]:
                game = new_game()
                g_newgame()
        else:
            window.blit(i_gamenew, (600,327))
        #Quit Button
        if 592+180 > mouse[0] > 592 and 390+45 > mouse[1] > 390:
            window.blit(io_gamequit, (592,390))
            if pygame.mouse.get_pressed()[0]:
                menu()
        else:
            window.blit(i_gamequit, (592,390))

        #Game Grid

##        pygame.draw.rect(window, grid_empty, ( 35, 40,126,126))  # linha 1, Coluna 1
##        pygame.draw.rect(window, grid_empty, (166, 40,126,126))  # linha 1, Coluna 2
##        pygame.draw.rect(window, grid_empty, (297, 40,126,126))  # linha 1, Coluna 3
##        pygame.draw.rect(window, grid_empty, (428, 40,126,126))  # linha 1, Coluna 4
##        pygame.draw.rect(window, grid_empty, ( 35,170,126,126))  # linha 2, Coluna 1
##        pygame.draw.rect(window, grid_empty, (166,170,126,126))  # linha 2, Coluna 2
##        pygame.draw.rect(window, grid_empty, (297,170,126,126))  # linha 2, Coluna 3
##        pygame.draw.rect(window, grid_empty, (428,170,126,126))  # linha 2, Coluna 4
##        pygame.draw.rect(window, grid_empty, ( 35,300,126,126))  # linha 3, Coluna 1
##        pygame.draw.rect(window, grid_empty, (166,300,126,126))  # linha 3, Coluna 2
##        pygame.draw.rect(window, grid_empty, (297,300,126,126))  # linha 3, Coluna 3
##        pygame.draw.rect(window, grid_empty, (428,300,126,126))  # linha 3, Coluna 4
##        pygame.draw.rect(window, grid_empty, ( 35,430,126,126))  # linha 4, Coluna 1
##        pygame.draw.rect(window, grid_empty, (166,430,126,126))  # linha 4, Coluna 2
##        pygame.draw.rect(window, grid_empty, (297,430,126,126))  # linha 4, Coluna 3
##        pygame.draw.rect(window, grid_empty, (428,430,126,126))  # linha 4, Coluna 4
        x = 43
        y = 50
        for row in range(4):
            for column in range (4):
                number = value(game, row+1, column+1)
                pygame.draw.rect(window, grid_empty, (x,y, 115,115))
                if (number == 2):
                    pygame.draw.rect(window, grid_2, (x,y,115,115))
                    font = pygame.font.Font("Pixel_font.otf", 24)
                    number_render = font.render(str(number), 1, black)
                    surface_number = number_render.get_rect()
                    surface_number.center = (x+58, y+58)
                    window.blit(number_render, surface_number)
                elif(number == 4):
                    pygame.draw.rect(window, grid_4, (x,y,115,115))
                    font = pygame.font.Font("Pixel_font.otf", 24)
                    number_render = font.render(str(number), 1, black)
                    surface_number = number_render.get_rect()
                    surface_number.center = (x+58, y+58)
                    window.blit(number_render, surface_number)
                elif(number == 8):
                    pygame.draw.rect(window, grid_8, (x,y,115,115))
                    font = pygame.font.Font("Pixel_font.otf", 24)
                    number_render = font.render(str(number), 1, white)
                    surface_number = number_render.get_rect()
                    surface_number.center = (x+58, y+58)
                    window.blit(number_render, surface_number)
                elif(number == 16):
                    pygame.draw.rect(window, grid_16, (x,y,115,115))
                    font = pygame.font.Font("Pixel_font.otf", 24)
                    number_render = font.render(str(number), 1, white)
                    surface_number = number_render.get_rect()
                    surface_number.center = (x+58, y+58)
                    window.blit(number_render, surface_number)
                elif(number == 32):
                    pygame.draw.rect(window, grid_32, (x,y,115,115))
                    font = pygame.font.Font("Pixel_font.otf", 24)
                    number_render = font.render(str(number), 1, white)
                    surface_number = number_render.get_rect()
                    surface_number.center = (x+58, y+58)
                    window.blit(number_render, surface_number)
                x += 130
            y += 130
            x = 43

def menu():

    for i in range(60):
        i_menuBg.set_alpha(i)
        window.blit(i_menuBg, (0,0))
        pygame.display.flip()

    menu = True

    while menu:

        process_events()

        mouse = pygame.mouse.get_pos()

        #Button New Game
        if 551+200 > mouse[0] > 551 and 111+50 > mouse[1] > 111:
            window.blit(io_newgame, (551,111))
            if pygame.mouse.get_pressed()[0]:
                g_dificult()
        else:
            window.blit(i_newgame, (551,111))
        #Button Score
        if 544+200 > mouse[0] > 544 and 212+50 > mouse[1] > 212:
            window.blit(io_score, (544,212))
        else:
            window.blit(i_score, (544, 212))
        #Button about
        if 572+200 > mouse[0] > 572 and 329+50 > mouse[1] > 329:
            window.blit(io_about, (572,329))
        else:
            window.blit(i_about, (572, 329))
        #Button Quit
        if 560+200 > mouse[0] > 560 and 426+50 > mouse[1] > 426:
            window.blit(io_quit, (560,426))
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
        else:
            window.blit(i_quit, (560, 426))    
    
        pygame.display.update()

#Game event processor function
def process_events():

    global done
    global status
    global game
    
    for event in pygame.event.get():  # This cycle process all events in pygame
        print(event)
        if event.type == pygame.QUIT: # This if checks if the user want to close the game
            done = True

        elif (event.type == pygame.KEYDOWN) and (status != None):
            if event.key == pygame.K_n:
                game = new_game()
            elif event.key == pygame.K_LEFT:
                game = left(game)
            elif event.key == pygame.K_RIGHT:
                game = right(game)
            elif event.key == pygame.K_DOWN:
                game = down(game)
            elif event.key == pygame.K_UP:
                game = up(game)

#Main cycle
while not(done):
    
    process_events()

    if (status == 1):
        loading()
    else:
        menu()       

    windw.blit(window, (0,0))
    pygame.display.flip()
    clock.tick(frame_rate) #Frame rate control
    
#Close pygame window
pygame.quit()

