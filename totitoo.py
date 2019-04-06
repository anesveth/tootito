import random
print("""︵‿︵‿︵‿︵‿︵  T O T I T O    U・ᴥ・U  ‿︵‿︵‿︵‿︵‿︵‿︵

QWE       _|_|_
 ASD   ➤  _|_|_
  ZXC      | |


    let's start!
""")
players=[]
player1=input("Jugador 1: ")
players.append(player1)
player2=input("Jugador 2: ")
players.append(player2)
first=random.choice(players)
players.remove(first)
second=players[0]
Iconos=["X","O"]
coordinates=[
"Q","W","E",
"A","S","D",
"Z","X","C"
]
parts=[" "," "," ",
" "," "," ",
" "," "," "
]
icono_en_uso=random.choice(Iconos)
Iconos.remove(icono_en_uso)
icono_oponente=Iconos[0]
def jugada():
    play1=input("seleccione la coordenada de su jugada: ")
    for i in range(len(coordinates)):
        if play1 in parts:
            "Ya esta jugada esa opcion"
            print(jugada)
    if play1 in coordinates: 
        parts[coordinates.index(play1)]=icono_en_uso
def jugadacontrincante():
    play1=input("seleccione la coordenada de su jugada: ")
    for i in range(len(coordinates)):
        if play1 in parts:
            "Ya esta jugada esa opcion"
            print(jugada)
    if play1 in coordinates: 
        parts[coordinates.index(play1)]=icono_oponente
def turn1():
    print ("Turno de el jugador {}, Icono: ".format(first)+"{}".format(icono_en_uso))
    print(jugada())
def turn2():
    print ("Turno de el jugador {}, Icono: ".format(second)+"{}".format(icono_oponente))
    print(jugadacontrincante())
def table():
    '''ella no te ama'''
    tablero=[\
    ["         |         |         "],\
    ["         |         |         "],\
    ["   {}     |    {}    |    {}    ".format(parts[0],parts[1],parts[2])],\
    ["         |         |         "],\
    ["_________|_________|_________"],\
    ["         |         |         "],\
    ["         |         |         "],\
    ["   {}     |    {}    |    {}    ".format(parts[3],parts[4],parts[5])],\
    ["         |         |         "],\
    ["_________|_________|_________"],\
    ["         |         |         "],\
    ["         |         |         "],\
    ["   {}     |    {}    |    {}   ".format(parts[6],parts[7],parts[8])],\
    ["         |         |         "],\
    ["         |         |         "]]
    
    for i in range(len(tablero)):
        print (*tablero[i])
def turnos():
    print(turn1())
    print(table())
    print(turn2())
    print(table())
def 
print(turnos())
