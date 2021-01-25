def setup():
    global x, y, on_line, vy, g
    x = width/2
    y = height/2
    vy = 0
    g = .9
    on_line = False
    
    size(800, 600)
    
def draw():
    global x, y, on_line, vy
    background(202)
    strokeWeight(2)
    line(100, height/2, width-100, height/2)
    
    x = constrain(x, 0, width)
    y = constrain(y, 0, height)
    
    if not on_line:
        y += vy
        vy += g
        
    if y > height-25:
        vy *= -.7
        y = height-25
    
    if x >= 100 and x <= width-100:
        if y >= height/2 - 25 and y <= height/2 + 25:
            y = height/2
            on_line = True
    else:
        on_line = False
    
    circle(x, y, 50)

    yi = str(int(round(map(y, 0, height, height/2, -height/2)))) + "i"
    xi = str(int(round(map(x, 0, width , -100/6, 100 + 100/6))))
    

    
    push()
    textSize(36)
    fill(0)
    text(xi if yi == "0i" else "{} + {}".format(xi, yi), width/2, height-50)
    pop()
    
    if(mousePressed and dist(x, y, mouseX, mouseY) < 25):
        vy = 0
        x = mouseX
        if not on_line:
            y = mouseY
    print(vy)
    
def mousePressed():
    global offset_x, offset_y
    offset_x = x - mouseX
    offset_y = y - mouseY
    
