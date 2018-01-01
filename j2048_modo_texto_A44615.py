"""

Projecto : "2048 Modo Texto"

Desenvolvido por: Jorge Miguel Coelho Silva
                  A44615

Desensolvido para: Projecto 2048 - Matemática Discréta e Programação

Ficheiros referentes ao game 2048:

    - Motor  - j2048_motor_A44615.py
             - Toda a informação relacionada com a logica do game
        
    - Testes - j2048_modo_texto_A44615.py
             - Zona de testes
        
    - Gestor - j2048_gestor_A44615.py
             - Regista e analiza o envio do ficheiro para confirmação posterior

Informações do Modo Texto:

    - Inicicalização do game 2048 em modo texto para testes

Update Log:

    - 2017-12-26 - Actualização do Modo de Texto para Inglês.
                   Actualização do modo de teclas.
                   Inserção do gestor.

"""

####### Imports #######

from j2048_motor_A44615 import *
from j2048_gestor_A44615 import *

####### Prints ########

def align(string):

    size = len(string)

    while size != 7:
        string = " " + string
        size = len(string)

    return string

def start_2048(game): # Função para imprimir o game 2048 em modo de Texto
    points = total_points(game)
    size = get_grid_size(game)
    print("Pontos =", points)
    for l in range(1, size + 1):
        row = ""
        for c in range(1, size + 1):
            row = row + align(str(value(game, l , c))) + " "
        print(row)

read_identification()
start_seed(None)

####### Game Start #######

game = new_game()

start_2048(game)

####### Reg. Grid ########

reg_initial_grid(value(game,1,1), value(game,1,2), value(game,1,3), value(game,1,4),
                 value(game,2,1), value(game,2,2), value(game,2,3), value(game,2,4),
                 value(game,3,1), value(game,3,2), value(game,3,3), value(game,3,4),
                 value(game,4,1), value(game,4,2), value(game,4,3), value(game,4,4))


####### Set KeyBindings ########

key = None

while key != 'q' and not(gameover(game)):
    key = input()

    if key == 'n':
        game = new_game()
        reg_plays(key)
    elif key == 'a':
        game = left(game)
        reg_plays(key)
    elif key == 'w':
        game = up(game)
        reg_plays(key)
    elif key == "d":
        game = right(game)
        reg_plays(key)
    elif key == "s":
        game = down(game)
        reg_plays(key)

    start_2048(game)

####### Connection confirmed #######

reg_points(total_points(game))
message = write_reg()
print(message)
