#Tablero y posiciones
tablero = [["N" for x in range(0,10)]for y in range(0,20)]
posX = 4
posY = 0
#Propiedades tetrominos
"Orden:T- L - J - S - Z - O - I"
tetrominos = [[19968, 17984, 3648, 19520],[11776, 17504, 3712, 50240],[36352, 25664, 3616, 17600],[27648, 17952, 27648, 17952],[50688, 19584, 50688, 19584],[52224, 52224, 52224, 52224],[3840, 17476, 3840, 17476]]
colores = [["#FF007D"],["#E56515"],["#1217E0"],["#33E012"],["#E31212"],["#E8CD31"],["#3EF5EA"]]
tRotation = 0

#Tetromino inicial
t = int(random(0,7))

juego = False
juego_terminado = False

tnext = 0

puntaje = 0

pos_fig_tab = []


def setup():
    size(500,620)
    
    
def draw():
    global juego, juego_terminado
    global posX
    global posY
    global t
    global tRotation
    global puntaje
    global tnext
    
    if juego:
        background("#101831")
        stroke(255,255,255)
        #Dibuja las líneas del tablero
        for i in range(0,21):
            line(10, (i*30)+10, 310, (i*30)+10)
            if (i < 11):
                line((i*30)+10, 10, (i*30)+10, 610)
        drawset()
        #drawfig()
            
        ficha_en_tablero()
        drawtablero()
        borrar_filas()
        if posY < 17:
            if posY == 16 and t == 6 and tRotation%2 == 1:
                if tablero[0][4] == "N" and tablero[0][5] == "N" and tablero[1][4] == "N" and tablero[1][5] == "N":
                    nuevo_tetromino()
                else:
                    juego = False
                    juego_terminado = True
            else:
                if bajar():
                    posY +=1
                else:
                    if tablero[0][4] == "N" and tablero[0][5] == "N" and tablero[1][4] == "N" and tablero[1][5] == "N":
                        nuevo_tetromino()
                    else:
                        juego = False
                        juego_terminado = True              
        elif posY < 18:
            if t == 5:
                if bajar():
                    posY +=1
                else:
                    if tablero[0][4] == "N" and tablero[0][5] == "N" and tablero[1][4] == "N" and tablero[1][5] == "N":
                        nuevo_tetromino()
                    else:
                        juego = False
                        juego_terminado = True
            elif tRotation == 0 or (tRotation == 2 and (t == 3 or t== 4 or t == 6)):
                if bajar():
                    posY += 1
                else:
                    if tablero[2][4] == "N" and tablero[2][5] == "N" and tablero[1][4] == "N" and tablero[1][5] == "N":
                        nuevo_tetromino()
                    else:
                        juego = False
                        juego_terminado = True
            else:
                if tablero[0][4] == "N" and tablero[0][5] == "N" and tablero[1][4] == "N" and tablero[1][5] == "N":
                    nuevo_tetromino()
                else:
                    juego = False
                    juego_terminado = True
        else:
            if tablero[0][4] == "N" and tablero[0][5] == "N" and tablero[1][4] == "N" and tablero[1][5] == "N":
                nuevo_tetromino()
            else:
                juego = False
                juego_terminado = True
                
                
    elif juego_terminado:
        background("#101831")
        #####Título
        propiedades("#FFFFFF","",80)
        text("JUEGO",130,200)
        text("TERMINADO",15,350)

        propiedades("#83082D","",80)
        text("JUEGO",135,200)
        text("TERMINADO",20,350)

        propiedades("#FFFFFF","",35)
        text("PUNTAJE : "+str(puntaje),100,480)        
        
        
    else:
        inicio()
        
def nuevo_tetromino():        
    posX = 4
    posY = 0
    t = tnext
    tRotation = 0
    puntaje +=10
    
    
def borrar_fig():
    for w in range(0,7,2):
        tablero[pos_fig_tab[w+1]-1][pos_fig_tab[w]] = "N"
 

def drawtablero():
    global pos_fig_tab
    
    cambiar_pos_fig()
    
    for f in range(20):
        for c in range(10):
            lugar = tablero[f][c]
            if lugar != "N":
                    fill(colores[tablero[f][c]][0])
                    square((c*30)+10,(f*30)+10,30)
                
def cambiar_pos_fig():
    #Quita la ficha del tablero
    if posY != 0:
        for w in range(0,7,2):
            tablero[pos_fig_tab[w+1]-1][pos_fig_tab[w]] = "N"
            
        #Pone la ficha en el tablero
        for w in range(0,7,2):
            tablero[pos_fig_tab[w+1]][pos_fig_tab[w]] = t

    
    
def ficha_en_tablero():
    global pos_fig_tab
    pos_fig_tab = []
    for a in range(0,16):
        if ((tetrominos[t][tRotation] & (1 << 15 - a)) != 0):
            pos_fig_tab += [((a % 4)+posX),(((a / 4) | 0)+posY)]
            
def bajar(z=1):
    x = []
    y = []
    for a in range(0,7,2):
        x += [pos_fig_tab[a]]
        y += [pos_fig_tab[a+1]]
    for b in range(4):
        if y[b] == max(y):
            if tablero[y[b]+z][x[b]] != "N":
                return False
    return True

def borrar_filas():
    global puntaje
    for q in range(20):
        c = 0
        for p in range(10):
            if tablero[q][p] != "N":
                c += 1
        if c == 10:
            del(tablero[q])
            tablero.insert(0,["N","N","N","N","N","N","N","N","N","N"])
            puntaje += 100
    
    
def keyPressed():
    global tRotation
    global posY
    global posX
    
    if (key == CODED):
        if (keyCode == UP):
            if tRotation >= 3:
                ficha_en_tablero()
                borrar_fig()
                tRotation = 0
            else:
                ficha_en_tablero()
                borrar_fig()
                tRotation += 1
                
        if (keyCode == DOWN):
            if posY <16:
                if bajar(2):
                    ficha_en_tablero()
                    borrar_fig()
                    posY += 2
            
        if (keyCode == RIGHT):
            if posX <= 6:
                ficha_en_tablero()
                borrar_fig()
                posX += 1
            elif posX <= 7:
                if t == 5:
                    ficha_en_tablero()
                    borrar_fig()
                    posX += 1

                elif tRotation == 3 and t != 3:
                    ficha_en_tablero()
                    borrar_fig()
                    posX += 1
                
                elif tRotation == 1 and (t==4 or t==6):
                    ficha_en_tablero()
                    borrar_fig()
                    posX += 1

                        
        if (keyCode == LEFT):
            if posX > 0:
                ficha_en_tablero()
                borrar_fig()
                posX -= 1
            elif tRotation == 1 and t != 4 and t != 5:
                if posX > -1:
                    ficha_en_tablero()
                    borrar_fig()
                    posX -=1
                                

def inicio():
    global juego
    #######Título
    background("#101831")
    propiedades("#FFFFFF","",85)
    text("TETRIS",110,200)
    propiedades("#83082D","",85)
    text("TETRIS",115,200)

    #######Botón para jugar
    propiedades("#178124","#178124")
    rect(205,310,90,40)
    propiedades("#FFFFFF","#FFFFFF")
    triangle(235,320,235,340,265,330)
    propiedades("#5BED6D","#5BED6D")
    triangle(240,320,240,340,270,330)
    
    if mouseX > 205 and mouseX < 295 and mouseY > 310 and mouseY < 350 and mousePressed:
        juego = True
        frameRate(2)
    
def drawset():
    global tnext
    ########Puntaje
    propiedades("#FFFFFF","",20)
    text("PUNTAJE",360,100)
    propiedades("#101831","#FFFFFF")
    rect(375,120,50,30)
    propiedades("#FFFFFF","",15)
    text(str(puntaje),385,140)
    
    #######Pieza siguiente
    propiedades("#FFFFFF","",20)
    text("SIGUIENTE",350,250)
    propiedades("#101831","#FFFFFF")
    rect(340,265,120,120)
    
    if posY == 0:
        tnext = int(random(0,7))
    ix = 355
    iy = 295
    if tnext == 6:
        ix -= 15
        iy -= 15
    if tnext == 5:
        ix += 15
    fill(colores[tnext][0])
    for a in range(0,16):
        if ((tetrominos[tnext][0] & (1 << 15 - a)) != 0):
            square(((a%4)*30)+ix,(((a/4)|0)*30)+iy,30)
    
    
def propiedades(color_1,color_2 ="",tam =""):
    fill(color_1)
    if color_2 != "":
        stroke(color_2)
    if tam != "":
        textSize(tam)
        
