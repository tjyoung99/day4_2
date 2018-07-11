def setup():
    size (500,500)
    stroke(0,0,0)
    fill(255,0,0)
    rect(0,450,50,50) #red
    fill(0,255,0)
    rect(50,450,50,50) #green
    fill(0,0,255)
    rect(100,450,50,50) #blue
    fill(255,0,255)
    rect(150,450,50,50)#future
    fill(255,255,0)
    rect(200,450,50,50)#yellow
    fill(random(255),random(255),random(255))
    rect(250,450,50,50)
def draw():
    if mousePressed:
        line(pmouseX,pmouseY, mouseX,mouseY)
    fill(random(255),random(255),random(255))
    rect(250,450,50,50)
def mouseClicked():
    if mouseX<50 and mouseY>450 : #red
        stroke(255,0,0)
    elif mouseX<100 and mouseY>450 :#green
        stroke(0,255,0)
    elif mouseX<150 and mouseY>450 :#blue
        stroke(0,0,250)
    elif mouseX<200 and mouseY>450 : #future
        stroke(255,0,255)
    elif mouseX<250 and mouseY>450: 
        stroke(255,255,0)
    elif mouseX<300 and mouseY>450: 
        stroke(random(255),random(255),random(255))
    elif mouseX<350 and mouseY>450: 
        rect(mouseX,mouseY,100,100)
