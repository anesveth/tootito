import random
#Variables usadas en funciones distintas aparecen afuera/antes de ellas
def screen():
    '''
    Aparece inicial mostrando las coordenadas del totito
    '''
    print("""︵‿︵‿︵‿︵‿︵  T O T I T O    U・ᴥ・U  ‿︵‿︵‿︵‿︵‿︵‿︵

    QWE      _|_|_
    ASD   ➤  _|_|_
    ZXC       | |


        let's start!
    """)
print(screen())
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
usedcoordinates=[]
parts=[" "," "," ",
" "," "," ",
" "," "," "
]
icono_en_uso=random.choice(Iconos)
Iconos.remove(icono_en_uso)
icono_oponente=Iconos[0]
def jugada():
    '''
    Pide coordenadas para la jugada del primer jugador
    '''
    play1=input("seleccione la coordenada de su jugada: ")
    if play1 in usedcoordinates:
        print("Ya esta jugada esa opcion")
        #EVITA QUE EL JUGADOR CORRIJA/REEMPLAZE JUGADAS SUYAS O DE SU OPONENTE
    elif play1 in coordinates: 
        parts[coordinates.index(play1)]=icono_en_uso
        usedcoordinates.append(play1)
def jugadacontrincante():
    '''
    Pide coordenadas para la jugada del segundo jugador
    '''
    play1=input("seleccione la coordenada de su jugada: ")
    if play1 in usedcoordinates:
        print("Ya esta jugada esa opcion")
        #EVITA QUE EL JUGADOR CORRIJA/REEMPLAZE JUGADAS SUYAS O DE SU OPONENTE
    elif play1 in coordinates: 
        parts[coordinates.index(play1)]=icono_oponente
        usedcoordinates.append(play1)
def turn1():
    '''
    Muestra al primer jugador (elejido al azar), su icono(X o O) y le avisa que es su turno
    '''
    print ("Turno de el jugador {}, Icono: ".format(first)+"{}".format(icono_en_uso))
    print(jugada())
def turn2():
    '''
    Muestra al segundo jugador que quedo, su icono(X o O) y le avisa que es su turno
    '''
    print ("Turno de el jugador {}, Icono: ".format(second)+"{}".format(icono_oponente))
    print(jugadacontrincante())
def table():
    '''Tabla del totito en la cual se van mostrando las jugadas'''
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
winningXcase=[("X","X","X")]
winningOcase=[("O","O","O")]

def turnos():
    '''
    Junta las funciones anteriores
    generando el sistema de juego
    '''
    print(turn1())
    print(table())
    print(turn2())
    print(table())

ganador="n"
def gamemode1v1():
    ganador="n"
    while(ganador=="n"):##El juego se repite hasta que alguien gana.
        print(turnos())
        wincombos=[(parts[0],parts[1],parts[2]),(parts[3],parts[4],parts[5]),
        (parts[6],parts[7],parts[8]),(parts[0],parts[3],parts[6]),
        (parts[6],parts[4],parts[2]),(parts[0],parts[4],parts[8]),
        (parts[2],parts[5],parts[8]),(parts[1],parts[4],parts[7])
        ]
        for i in range(8):#COMPROBACION DE QUE HAYA GANADO
            if (wincombos[i]==winningXcase[0])and(ganador=="n"): 
                if icono_en_uso=="X":
                    print("Jugador {} gana!".format(first))
                    ganador=first
                else:
                    print("Jugador {} gana!".format(second))
                    ganador=second   
            if (wincombos[i]==winningOcase[0])and(ganador=="n"): 
                if icono_en_uso=="O":
                    print("Jugador {} gana!".format(first))
                    ganador=first
                else:
                    print("Jugador {} gana!".format(second))
                    ganador=second   
print(gamemode1v1())
