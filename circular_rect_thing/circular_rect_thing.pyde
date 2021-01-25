def setup():
    global a
    a = 0
    size(600, 600)

def draw():
    global a
    a -= .1
    x = sin(a) * 300 * (constrain(-a //TWO_PI, 0, 20))/20
    y = cos(a) * 300 * (constrain(-a //TWO_PI, 0, 20))/20
    background(200)
    fill(255)
    # rect(width/2, height/2, -(width/2-mouseX), -(height/2-mouseY))
    # ellipse(width/2, height/2, 600, 600)
    # rect(width/2, height/2, x, y)
    
    # point(width/2 + x, height/2 + y)
    line(x + width/2, y + height/2, width/2, height/2)
    
    fill(0)
    text(str(a // TWO_PI), width/2, height/2)
    fill(255)
    
    
