"""
Projecto: "2048"

Desenvolvido por: Jorge Miguel Coelho Silva
                  A44615

Desenvolvido para: Projecto - Matemática Discréta e Programação

Ficheiros referentes ao jogo 2048:

    - Motor  - j2048_motor_A44615.py
             - Toda a informação relacionada com a logica do jogo
        
    - Testes - j2048_modo_texto_A44615.py
             - Zona de testes
        
    - Gestor - j2048_gestor_A44615.py
             - Regista e analiza o envio do ficheiro para confirmação posterior

Informações do motor:

    - Funções e constantes estão escritas em Inglês
    
    - Comentários as construcções lógicas em Português

Guia de referências:

    ## Zona de comentários informativos a cada bloco/linha de código
    
Update Log:

    - 2017-12-26 - Adicionado Possibilidade de escolha de dificuldade.
                   Adicionado as funções Direita, Cima, Baixo, Transposta e inversa.

    - 2017-12-20 - Adicionado comentários conclusivos as funções e objectivos das mesmas.
                   Usando comentários para identificar zonas de código.
                   
    - 2017-12-19 - Actualização das funções e constantes do motor lógico do jogo 2048 para Inglês.
    
    - 2017-12-19 - Actualização do ficheiro j2048_motor_A44615.py.
                   Esta modificação não registou alterações anteriores.

"""

#Imports  ###########################################################################################

from random import random
from random import choice

#Lógica   ###########################################################################################

def grid_type(value): # Função que define o tipo de grelha a ser apresentada

    print("Seleccione a dificuldade: easy, medium, classic")
    dif = value # Requesita ao utilizador uma palavra chave para definir a dificuldade
    
    if dif == 'easy':
        grid_type = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
        print("Dificuldade escolhida :", dif)
    elif dif == 'medium':
        grid_type = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
        print("Dificuldade escolhida :", dif)
    else:
        grid_type = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
        print("Dificuldade escolhida : default(Classic)")
 
    return grid_type

def get_empty_positions(grid): # Função que vai obter zonas vazias da grelha

    empty_positions = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                empty_positions.append([i, j])

    return empty_positions

def get_empty_position(grid): # Função que vai obter a zona vazia da grelha

    empty_positions = get_empty_positions(grid)
    empty_position = choice(empty_positions)

    return empty_position

def get_2or4(): # Função que gera o o valor obtido de 2 ou 4

    if random() > 0.1:
        return 2
    else:
        return 4

def insert_2or4(grid): # Função que insere o valor 2 ou 4 na grelha

    value_2or4              = get_2or4()
    empty_position          = get_empty_position(grid)

    i_row                   = empty_position[0]
    i_column                = empty_position[1]

    grid[i_row][i_column]   = value_2or4

def new_game(): # Função que inicia um novo jogo

    grid     = grid_type(value)

    size = len(grid)
    
    gameover = False
    victory  = False
    points   = 0

    insert_2or4(grid)
    insert_2or4(grid)

    return(grid, gameover, victory, points, size)

def move_left(a_list): # Função de mover a lista para a esquerda

    result = []

    for value in a_list:
        if value != 0:
            result.append(value)

    while len(result) != len(a_list):
        result.append(0)

    return result

def sum_left(a_list): # Função que soma a esquerda

    result = []
    points = 0
    n      = 0

    while n < len(a_list):
        if (n < len(a_list)-1) and (a_list[n] == a_list[n+1]):
            count = a_list[n] + a_list[n+1]
            result.append(count)
            points = points + count
            n      = n + 2
        else:
            result.append(a_list[n])
            n      = n + 1

    while len(result) != len(a_list):
        result.append(0)

    return(result, points)

def refresh_grid(actual_grid, changed_grid): # Função que actualiza a grelha

    both_equals = True

    for l in range(len(actual_grid)):
        for c in range(len(actual_grid[l])):
            if actual_grid[l][c] != changed_grid[l][c]:
                both_equals = False

    if not both_equals:
        insert_2or4(changed_grid)

def get_victory(grid): # Função que verifica se já chegou a 2048

    result = False

    for l in range(len(grid)):
        for c in range(len(grid[l])):
            if grid[l][c] == 2048:
                result = True

    return result

def adjacent_equals(grid): # Função que verifica se existe iguais adjacentes

    exists = False

    ## Por Linhas

    for l in range(len(grid)):
        for c in range(len(grid[l]) - 1):
            if grid[l][c] == grid[l][c + 1]:
                exists = True

    ## Por Colunas

    for l in range(len(grid) - 1):
        for c in range(len(grid[l])):
            if grid[l][c] == grid[l + 1][c]:
                exists = True

    return exists

def get_gameover(grid): # Função que verifica se ainda existe possibilidade de jogar

    gameover = False

    if (len(get_empty_positions(grid)) == 0) and (not adjacent_equals(grid)):
        gameover = True

    return gameover

def left(game): # Função que movimenta para a esquerda

    grid         = game[0]
    gameover     = game[1]
    victory      = game[2]
    points       = game[3]
    size         = game[4]

    changed_grid = []

    for row in grid:
        row2 = move_left(row)
        (row3, sum_points) = sum_left(row2)
        changed_grid.append(row3)

        points = points + sum_points

    refresh_grid(grid, changed_grid)
    if victory == False:
        victory = get_victory(changed_grid)

    gameover = get_gameover(changed_grid)

    changed_game = (changed_grid, gameover, victory, points, size)

    return changed_game

def right(game):

    grid          = game[0]
    gameover      = game[1]
    victory       = game[2]
    points        = game[3]
    size          = game[4]

    inverted_grid = invert(grid)
    transform     = (inverted_grid, gameover, victory, points, size)

    game          = left(transform)

    grid          = game[0]

    final_grid    = invert(grid)

    gameover      = game[1]
    victory       = game[2]
    points        = game[3]
    size          = game[4]

    changed_game  = (final_grid, gameover, victory, points, size)

    return changed_game

def up(game):
    
    grid            = game[0]
    gameover        = game[1]
    victory         = game[2]
    points          = game[3]
    size            = game[4]

    transposed_grid = transposed(grid)
    transform       = (transposed_grid, gameover, victory, points, size)

    game            = left(transform)

    grid            = game[0]

    final_grid      = transposed(grid)

    gameover        = game[1]
    victory         = game[2]
    points          = game[3]
    size            = game[4]

    changed_game    = (final_grid, gameover, victory, points, size)

    return changed_game

def down(game):
    
    grid            = game[0]
    gameover        = game[1]
    victory         = game[2]
    points          = game[3]
    size            = game[4]

    transposed_grid = transposed(grid)
    transform       = (transposed_grid, gameover, victory, points, size)

    game            = right(transform)

    grid            = game[0]

    final_grid      = transposed(grid)

    gameover        = game[1]
    victory         = game[2]
    points          = game[3]
    size            = game[4]

    changed_game    = (final_grid, gameover, victory, points, size)

    return changed_game

def transposed(a_list):

    transposed = []

    for i in range(len(a_list)):
        list_column = []

        for row in a_list:
            list_column.append(row[i])
            
        transposed.append(list_column)

    return transposed

def invert(a_list):

    for row in a_list:
        row.reverse()

    return a_list

def value(game, row, column):

    grid     = game[0]
    i_row    = row - 1
    i_column = column - 1

    return grid[i_row][i_column]

def gameover(game):
    return game[1]

def win_or_lose(game):
    return game[2]

def total_points(game):
    return game[3]

def get_grid_size(game):
    return game[4]
