
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

game = False
gameOver = False

click = False

def setup():
    size(300,600)
    frameRate(2)
    
    
def draw():
    global posX
    global posY
    global t
    global tRotation
    if game:
        background("#101831")
        stroke(255,255,255)
        #Dibuja las líneas del tablero
        for i in range(1,20):
            line(0, (i*30), 300, (i*30))
            if (i < 11):
                line((i*30), 0, (i*30), 600)
        drawfig()
        if posY < 18:
            posY +=1
        else:
            posX = 4
            posY = 0
            t = int(random(0,7))
            tRotation = 0
    elif gameOver:
        print("Game Over")
        
    else:
        inicio()


    

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
    global posX
    if (key == CODED):
        if (keyCode == UP):
            if tRotation >= 3:
                tRotation = 0
            else:
                tRotation += 1
        if (keyCode == DOWN):
            posY += 2
            
        if (keyCode == RIGHT):
            if posX <= 8:
                posX += 1
                
        if (keyCode == LEFT):
            if posX > 0:
                posX -= 1
    
def inicio():
    global game
    global click
    #######Título
    background("#101831")
    textSize(64)
    fill(255,255,255)
    text("TETRIS",40,200)
    textSize(64)
    fill("#83082D")
    text("TETRIS",44,200)
    #######Botón para jugar
    fill("#178124")
    stroke("#178124")
    rect(110,300,80,40)
    fill(255,255,255)
    stroke(255,255,255)
    triangle(135,310,135,330,165,320)
    fill("#5BED6D")
    stroke("#5BED6D")
    triangle(140,310,140,330,170,320)
    if mouseX > 110 and mouseX < 190 and mouseY > 300 and mouseY < 340 and mousePressed:
        game = True
        print("Inició el juego")
 
