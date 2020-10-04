#Tablero y posiciones
tablero = [[0 for x in range(0,10)]for y in range(0,20)]
posX = 4
posY = 0
#Propiedades tetrominos
"Orden:T- L - J - S - Z - O - I"
tetrominos = [[19968, 17984, 3648, 19520],[11776, 17504, 3712, 50240],[36352, 25664, 3616, 17600],[27648, 17952, 27648, 17952],[50688, 9792, 50688, 9792],[52224, 52224, 52224, 52224],[3840, 17476, 3840, 17476]]
colores = [["#FF007D"],["#E56515"],["#1217E0"],["#33E012"],["#E31212"],["#E8CD31"],["#3EF5EA"]]
tRotation = 0

#Tetromino inicial
t = int(random(0,7))

juego = False
juego_terminado = False

tnext = 0

puntaje = 0

def setup():
    size(500,620)
    
    
def draw():
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
        drawfig()
        if posY < 18:
            posY +=1
        else:
            posX = 4
            posY = 0
            t = tnext
            tRotation = 0
            puntaje +=10
    
    elif juego_terminado:
        print("Game Over")
        
    else:
        inicio()
    
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
    
    


def drawfig():
    push()
    fill(colores[t][0])
    for a in range(0,16):
        if ((tetrominos[t][tRotation] & (1 << 15 - a)) != 0):
            square((((a % 4)+posX) * 30)+10, ((((a / 4) | 0)+posY) * 30)+10, 30)
    pop()
    
    
def drawtablero():
    for f in range(21):
        for c in range(11):
            lugar = tablero[f][c]
            if lugar != 0:
                fill(colores[tablero[f][c]][0])
                square((c*30)+10,(f*30)+10,30)
    
#def ficha_en_tablero():
        
    
    
def keyPressed():
    global tRotation
    global posY
    global posX
    if (key == CODED):
        if (keyCode == UP):
            if tRotation >= 3:
                tRotation = 0
                posY -= 1
            else:
                tRotation += 1
                posY -=1
        if (keyCode == DOWN):
            posY += 2
            
        if (keyCode == RIGHT):
            if posX <= 8:
                posX += 1
                
        if (keyCode == LEFT):
            if posX > 0:
                posX -= 1
    
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
        print("Inició el juego")
        
def propiedades(color_1,color_2 ="",tam =""):
    fill(color_1)
    if color_2 != "":
        stroke(color_2)
    if tam != "":
        textSize(tam)
