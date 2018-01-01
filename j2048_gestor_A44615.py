"""

Projecto : "2048 Gestor"

Desenvolvido por: Jorge Miguel Coelho Silva
                  A44615

Desensolvido para: Projecto 2048 - Matemática Discréta e Programação

Ficheiros referentes ao game 2048:

    - Motor  - j2048_engine_A44615.py
             - Toda a informação relacionada com a logica do game
        
    - Testes - j2048_text_mode_A44615.py
             - Zona de testes
        
    - Gestor - j2048_manager_A44615.py
             - Regista e analiza o envio do ficheiro para confirmação posterior

Informações do Gestor:

    - 

Update Log:

    - 2017-12-26 - Actualização do Gestor para Inglês.

"""
####### Imports #######

from random import randint
from random import seed
from urllib import request

####### Global Var #######

number  = None
friends = None
grid    = None
plays   = None
points  = None
seedvar = None

def get_number(row):

    #global number

    number = row[7:-1] # Lê o número do indice 7 ao último indice antes do fim-de-linha
    
    return number

def get_friends(row):

    #global friends

    friends = row[7:-1]

    #Count commas
    n_comma = 0
    for letter in friends:
        if letter == ",":
            n_comma = n_comma + 1

    n_friends = n_comma + 1

    if (n_friends < 2) or (n_friends > 5):
        print("Número de amigos = " + str(n_friends))
        print("O número de amigos é INVÁLIDO. Tem que estar entre 2 e 5.")
        print("A  sua entrada no ranking vai ser REJEITADA.")

    return friends

def read_identification():

    global number
    global friends

    file_name = "identification.txt"
    mode      = "r"

    file = open(file_name, mode)

    row1 = file.readline()
    row2 = file.readline()

    file.close()

    number  = get_number(row1)
    friends = get_friends(row2)

def start_seed(seed_to_use):

    global seedvar

    if seed_to_use == None:
        seed_to_use = randint(1, 1000)

    seed(seed_to_use)
    seedvar = seed_to_use

def reg_initial_grid(g11, g12, g13, g14,
                     g21, g22, g23, g24,
                     g31, g32, g33, g34,
                     g41, g42, g43, g44):

    global grid
    global plays
    global points

    grid = [[g11, g12, g13, g14],
            [g21, g22, g23, g24],
            [g31, g32, g33, g34],
            [g41, g42, g43, g44]]

    global number
    global friends
    global seedvar
    
    plays = ""
    points = None

def reg_plays(letter):

    global plays

    plays = plays + letter

def reg_points(p):

    global points

    points = p

def reg_ranking():
    message = None
    try:
        url_string = "http://ec2-54-246-213-131.eu-west-1.compute.amazonaws.com/cgi-bin/submit_2048.py?numero=" + number + "&amigos=" + friends + "&jogadas=" + plays + "&pontos=" + str(points) + "&semente=" + str(seedvar)
        url = request.urlopen(url_string)
        message = url.read().decode("utf-8")
    except Exception as err:
        message = "Não foi possível registar a pontuação no ranking.\n"
        message = message + str(err)
    return message

def write_reg():

    file_name = number + "." + str(points)
    mode = "w"

    file = open(file_name, mode)

    file.write("numero=" + number + "\n")
    file.write("amigos=" + friends + "\n")
    file.write("grelha_inicial=" + str(grid) + "\n")
    file.write("jogadas=" + plays + "\n")
    file.write("pontos=" + str(points) + "\n")
    file.write("semente=" + str(seedvar) + "\n")

    file.close()

    message_cloud = reg_ranking()

    return message_cloud
    
