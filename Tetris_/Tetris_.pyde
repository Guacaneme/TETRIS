
#POsiciones del tablero
posX = 4
posY = 0
#Propiedades tetrominos
tetrominos = [["T",[184, 154, 58, 178]],["L",[120, 147, 60, 402]],["J",[312, 210, 57, 150]],["S",[240, 153, 240, 153]],["Z",[408, 180, 408, 180]]]
colores = [["#FF007D"],["#67EDDC"],["#1217E0"],["#33E012"],["#E31212"]]
tRotation = 0

#Tetromino inicial
t = int(random(0,4))


def setup():
    size(300,600)
    background(0,100,200)
    frameRate(1.5)
    
    
def draw():
    global posY
    global t
    global tRotation
    background(0,100,200)
    #Dibuja las líneas del tablero
    for i in range(1,20):
        line(0, (i*30), 300, (i*30))
        if (i < 11):
            line((i*30), 0, (i*30), 600)
    drawfig()
    if posY < 20:
        posY +=1
    else:
        posY = 0
        t = int(random(0,4))
        tRotation = 0
        

    

def drawfig():
    push()
    fill(colores[t][0])
    for a in range(0,9):
        if ((tetrominos[t][1][tRotation] & (1 << 8 - a)) != 0):
            square(((a % 3)+posX) * 30, (((a / 3) | 0)+posY) * 30, 30)

    pop()
    
def keyPressed():
    global tRotation
    global posY
    if (key == CODED):
        if (keyCode == UP):
            if tRotation >= 3:
                tRotation = 0
            else:
                tRotation += 1
        if (keyCode == DOWN):
            posY += 2
