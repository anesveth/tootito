import random
#Variables usadas en funciones distintas aparecen afuera/antes de ellas

def screen1v1():
    '''
    Pantalla inicial modo Player vs player
    Aparece inicialmente mostrando las coordenadas del totito
    '''
    print("""︵‿︵‿︵‿︵‿︵  T O T I T O    U・ᴥ・U  ‿︵‿︵‿︵‿︵‿︵‿︵                                
                ///// 1  vs  1  /////

    QWE       _|_|_
     ASD   ➤  _|_|_
      ZXC      | |

        the first player to get three in a row of their mark wins
        let's start!
    """)
def screen1vc():
    '''
    Pantalla inicial modo Player vs computer
    Aparece inicialmente mostrando las coordenadas del totito
    '''
    print("""︵‿︵‿︵‿︵‿︵  T O T I T O    U・ᴥ・U  ‿︵‿︵‿︵‿︵‿︵‿︵                                
            ///// player  vs  computer  /////

    QWE       _|_|_
     ASD   ➤  _|_|_
      ZXC      | |

        try to get three in a row
        let's start!
    """)
def screenmisere():
    '''
    Pantalla inicial modo Player vs Player MISERE
    Aparece inicialmente mostrando las coordenadas del totito
    '''
    print("""︵‿︵‿︵‿︵‿︵  T O T I T O    U・ᴥ・U  ‿︵‿︵‿︵‿︵‿︵‿︵                                
                ///// 1  vs  1  MISERE  /////

    QWE       _|_|_
     ASD   ➤  _|_|_
      ZXC      | |
      
        get your opponent to make three in a row
        let's start!
    """)
def menu():
    '''Menu principal de opciones'''
    print("""︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵
                
                T O T I T O    U・ᴥ・U  


                1) Player vs Player

                2) Player vs Computer

                3) Misere

                    ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡
    """)
print (menu())
selection=input("""Choose your game mode ➤ """)
print("︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵")
players=[]
if (selection=="1"):
    print(screen1v1())
    player1=input("Player 1: ")
    players.append(player1)
    player2=input("Player 2: ")
    players.append(player2)
    first=random.choice(players)
    players.remove(first)
    second=players[0]

if selection=="2":
    print(screen1vc())
    player=input("Your name: ")
    players.append(player)
    computernames=[
    "Santa","Kenny vel","Champion","Ella no te ama","Sus mentiras","Justin Bieber","GamerGirl",
    "Chum Chum","Britney Spears","Katy Perry","One Direction","Mickey Mouse","Kim Kardashian",
    "Mcdonald's","La niña del Aro","Aros de cebolla","Minion","Harry Potter",
    "Voldemort","Larry is real","Badabun","Dora the explorer","Gucci","Gucci Gang","Fangirl",
    "Harry Styles","Louis Tomlinson","Shawn Mendes"
    ]
    titlesforthename=["Son of","King of","Slave of","Fan of","Duchess","Killer of",
    "President","Lover of","Queen","Pray for","Death to","Hates","Boyfriend of","Girlfriend of"]
    #hace un nombre a base de las dos listas
    computername=str(random.choice(titlesforthename))+" "+str(random.choice(computernames))
    print("YOUR OPPONENT IS ( •̀ω•́ )σ {}".format(computername))
    players.append(computername)
    first=random.choice(players)
    players.remove(first)
    second=players[0]


if (selection=="3"):
    print(screenmisere())
    player1=input("Player 1: ")
    players.append(player1)
    player2=input("Player 2: ")
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
icono_en_uso=random.choice(Iconos)#Icono del primer jugador
Iconos.remove(icono_en_uso)
icono_oponente=Iconos[0]#Icono del segundo jugador
def jugada():
    '''
    Pide coordenadas para la jugada del primer jugador
    '''
    play1=input("Choose the coordinate of your move: ")
    if play1 in usedcoordinates:
        print("This option has already been played")
        #EVITA QUE EL JUGADOR CORRIJA/REEMPLAZE JUGADAS SUYAS O DE SU OPONENTE
        print(jugada())
    elif play1 in coordinates: 
        parts[coordinates.index(play1)]=icono_en_uso
        usedcoordinates.append(play1)

def jugadacontrincante():
    '''
    Pide coordenadas para la jugada del segundo jugador
    '''
    play1=input("Choose the coordinate of your move: ")
    if play1 in usedcoordinates:
        print("This option has already been played")
        print(jugada())
        #EVITA QUE EL JUGADOR CORRIJA/REEMPLAZE JUGADAS SUYAS O DE SU OPONENTE
    elif play1 in coordinates: 
        parts[coordinates.index(play1)]=icono_oponente
        usedcoordinates.append(play1)
    
def turn1():
    '''
    Muestra al primer jugador (elejido al azar), su icono(X o O) y le avisa que es su turno
    '''
    print ("Turn of player {}, Icon: ".format(first)+"{}".format(icono_en_uso))
    print(jugada())
def turn2():
    '''
    Muestra al segundo jugador que quedo, su icono(X o O) y le avisa que es su turno
    '''
    print ("Turn of player {}, Icon: ".format(second)+"{}".format(icono_oponente))
    print(jugadacontrincante())

def jugadacomputadora():
    '''Algoritmo modo de juego de la computadora'''
    if first==computername:#si la computadora juega primero
        play1=random.choice(coordinates)
        while (play1 in usedcoordinates):
            play1=random.choice(coordinates)
        usedcoordinates.append(play1)
        parts[coordinates.index(play1)]=icono_en_uso
    elif second==computername:#si la computadora juega de segundas
        play1=random.choice(coordinates)
        while (play1 in usedcoordinates):
            play1=random.choice(coordinates)
        usedcoordinates.append(play1)
        parts[coordinates.index(play1)]=icono_oponente

def turn1_1vsc():
    '''
    primer turno, puede ser player o computadora
    '''
    print ("Turn of player {}, Icon: ".format(first)+"{}".format(icono_en_uso))
    if first==player:
        play1=input("Choose the coordinate of your move: ")
        if play1 in usedcoordinates:
            print("This option has already been played")
            #EVITA QUE EL JUGADOR CORRIJA/REEMPLAZE JUGADAS SUYAS O DE SU OPONENTE
            print(jugada())
        elif play1 in coordinates: 
            parts[coordinates.index(play1)]=icono_en_uso
            usedcoordinates.append(play1)
    elif first==computername:#si empieza la computadora la partida, su seleccion sera al azar
        print(jugadacomputadora())

def turn2_1vsc():    
    '''
    segundo turno, puede ser player o computadora
    '''
    print ("Turn of player {}, Icon: ".format(second)+"{}".format(icono_oponente))
    if second==player:
        play1=input("Choose the coordinate of your move: ")
        if play1 in usedcoordinates:
            print("This option has already been played")
            #EVITA QUE EL JUGADOR CORRIJA/REEMPLAZE JUGADAS SUYAS O DE SU OPONENTE
            print(jugada())
        elif play1 in coordinates: 
            parts[coordinates.index(play1)]=icono_oponente
            usedcoordinates.append(play1)
    elif second==computername:#si empieza la computadora la partida, su seleccion sera al azar
        print(jugadacomputadora())

def table():
    '''Tabla del totito en la cual se van mostrando las jugadas'''
    tablero=[\
    ["        |       |        "],\
    ["   {}    |   {}   |    {}   ".format(parts[0],parts[1],parts[2])],\
    ["________|_______|________"],\
    ["        |       |        "],\
    ["   {}    |   {}   |    {}   ".format(parts[3],parts[4],parts[5])],\
    ["________|_______|________"],\
    ["        |       |        "],\
    ["   {}    |   {}   |    {}  ".format(parts[6],parts[7],parts[8])],\
    ["        |       |        "]]
    
    for i in range(len(tablero)):
        print (*tablero[i])
winningXcase=[("X","X","X")]
winningOcase=[("O","O","O")]

def turnos1v1():
    '''
    Junta las funciones anteriores
    generando el sistema de juego 1 vs 1
    '''
    print(turn1())
    print(table())
    print(turn2())
    print(table())

def turnos1vc():
    '''
    Junta las funciones anteriores
    generando el sistema de juego 1 vs computer
    '''
    print(turn1_1vsc())
    print(table())
    print(turn2_1vsc())
    print(table())

attempts=["1","2","3","4","5"] #####lista de intentos disponibles.

usedattempts=[]
def gamemode1v1():
    '''
    Modo de juego 1v1 
    '''
    ganador="n"
    secondarycount=0
    while(ganador=="n"):##El juego se repite hasta que alguien gana.
        print(turnos1v1())
        wincombos=[(parts[0],parts[1],parts[2]),(parts[3],parts[4],parts[5]),
        (parts[6],parts[7],parts[8]),(parts[0],parts[3],parts[6]),
        (parts[6],parts[4],parts[2]),(parts[0],parts[4],parts[8]),
        (parts[2],parts[5],parts[8]),(parts[1],parts[4],parts[7])
        ]
        for i in range(8):#COMPROBACION DE QUE HAYA GANADO
            if (wincombos[i]==winningXcase[0])and(ganador=="n"): 
                if icono_en_uso=="X":
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(first))
                    ganador=first
                else:
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(second))
                    ganador=second   
            if (wincombos[i]==winningOcase[0])and(ganador=="n"): 
                if icono_en_uso=="O":
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(first))
                    ganador=first
                else:
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(second))
                    ganador=second 
        #### EN CASO DE EMPATE DETIENE EL JUEGO CUANDO YA NO SE PUEDE GANAR
        usedattempts.append(attempts[secondarycount])
        secondarycount=secondarycount+1
        if (len(usedattempts)==4) and (len(usedcoordinates)>=8) and (ganador=="n"):
            print ("♡♡♡♡♡♡♡♡♡♡ IT'S A TIE (ㆀ˘･з･˘) ♡♡♡♡♡♡♡♡♡♡")
            ganador="noone" 
    
def gamemode1vc():
    '''
    Modo de juego 1vComputer 
    '''  
    ganador="n"
    secondarycount=0
    while(ganador=="n"):##El juego se repite hasta que alguien gana.
        print(turnos1vc())
        wincombos=[(parts[0],parts[1],parts[2]),(parts[3],parts[4],parts[5]),
        (parts[6],parts[7],parts[8]),(parts[0],parts[3],parts[6]),
        (parts[6],parts[4],parts[2]),(parts[0],parts[4],parts[8]),
        (parts[2],parts[5],parts[8]),(parts[1],parts[4],parts[7])
        ]
        for i in range(8):#COMPROBACION DE QUE HAYA GANADO
            if (wincombos[i]==winningXcase[0])and(ganador=="n"): 
                if icono_en_uso=="X":
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(first))
                    ganador=first
                else:
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(second))
                    ganador=second   
            if (wincombos[i]==winningOcase[0])and(ganador=="n"): 
                if icono_en_uso=="O":
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(first))
                    ganador=first
                else:
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(second))
                    ganador=second 
        #### EN CASO DE EMPATE DETIENE EL JUEGO CUANDO YA NO SE PUEDE GANAR
        usedattempts.append(attempts[secondarycount])
        secondarycount=secondarycount+1
        if (len(usedattempts)==4) and (len(usedcoordinates)>=8) and (ganador=="n"):
            print ("♡♡♡♡♡♡♡♡♡♡ IT'S A TIE (ㆀ˘･з･˘) ♡♡♡♡♡♡♡♡♡♡")
            ganador="noone" 

def gamemodemisere():
    '''
    Modo de juego 1v1 misere
    ''' 
    perdedor="n"
    secondarycount=0
    while(perdedor=="n"):##El juego se repite hasta que alguien gana.
        print(turnos1v1())
        losecombos=[(parts[0],parts[1],parts[2]),(parts[3],parts[4],parts[5]),
        (parts[6],parts[7],parts[8]),(parts[0],parts[3],parts[6]),
        (parts[6],parts[4],parts[2]),(parts[0],parts[4],parts[8]),
        (parts[2],parts[5],parts[8]),(parts[1],parts[4],parts[7])
        ]
        for i in range(8):#COMPROBACION DE QUE HAYA GANADO
            if (losecombos[i]==winningXcase[0])and(perdedor=="n"): 
                if icono_en_uso=="X":
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(second))
                    perdedor=first
                else:
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(first))
                    perdedor=second   
            if (losecombos[i]==winningOcase[0])and(perdedor=="n"): 
                if icono_en_uso=="O":
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(second))
                    perdedor=first
                else:
                    print("Player {} wins! ₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡ ♡♡♡♡♡♡♡♡♡♡".format(first))
                    perdedor=second
        #### EN CASO DE EMPATE DETIENE EL JUEGO CUANDO YA NO SE PUEDE GANAR
        usedattempts.append(attempts[secondarycount])
        secondarycount=secondarycount+1
        if (len(usedattempts)==4) and (len(usedcoordinates)>=8) and (perdedor=="n"):
            print ("♡♡♡♡♡♡♡♡♡♡ IT'S A TIE (ㆀ˘･з･˘) ♡♡♡♡♡♡♡♡♡♡")
            perdedor="noone" 

############################################################################################################
###########################SE ACTIVA EL PROGRAMA DEPENDE DE LO ELEJIDO EN EL MENU ##########################

if (selection=="1"):
    print(gamemode1v1())
if (selection=="2"):
    print(gamemode1vc())
if (selection=="3"):
    print(gamemodemisere())


