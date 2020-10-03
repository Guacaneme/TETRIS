
#Posiciones del tablero
posX = 4
posY = 0
#Propiedades tetrominos
"Orden:T- L - J - S - Z - O - I"
tetrominos = [[19968, 17984, 3648, 19520],[11776, 17504, 3712, 50240],[36352, 25664, 3616, 17600],[27648, 17952, 27648, 17952],[50688, 9792, 50688, 9792],[52224, 52224, 52224, 52224],[3840, 17476, 3840, 17476]]
colores = [["#FF007D"],["#67EDDC"],["#1217E0"],["#33E012"],["#E31212"],["#E8CD31"],["#3EF5EA"]]
tRotation = 0

#Tetromino inicial
t = int(random(0,7))


def setup():
    size(300,600)
    background(0,100,200)
    frameRate(5)
    
    
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
    if posY < 18:
        posY +=1
    else:
        posY = 0
        t = int(random(0,7))
        print(t)
        tRotation = 0
        

    

def drawfig():
    push()
    fill(colores[t][0])
    for a in range(0,16):
        if ((tetrominos[t][tRotation] & (1 << 15 - a)) != 0):
            square(((a % 4)+posX) * 30, (((a / 4) | 0)+posY) * 30, 30)

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
