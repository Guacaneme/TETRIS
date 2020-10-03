posX = 5
posY = 0
T = [184, 154, 58, 178]
tRotation = 0

def setup():
    size(300,600)
    background(0,100,200)
    frameRate(1)
    
    
def draw():
    global posY
    background(0,100,200)
    for i in range(1,20):
        line(0, (i*30), 300, (i*30))
        if (i < 11):
            line((i*30), 0, (i*30), 600)
    drawfig()
    if posY < 20:
        posY +=1
    else:
        posY = 0
        print("SUBIÓ :P")
    

def drawfig():
    push()
    fill(200,10,50)
    for a in range(0,9):
        if ((T[tRotation] & (1 << 8 - a)) != 0):
            square(((a % 3)+posX) * 30, (((a / 3) | 0)+posY) * 30, 30)
#square(posX*30,posY*30,30)
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
