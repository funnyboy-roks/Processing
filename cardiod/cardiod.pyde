def setup():
    global a1, a2
    size(900, 900)
    a1 = a2 = 0
    
def draw():
    global a1, a2
    
    r = width/2
    
    ax = sin(a2) * r + width/2
    ay = cos(a2) * r + height/2
    # circle(width/2, height/2, 2*r)
    
    x = sin(a1) * r + width/2
    y = cos(a1) * r + height/2
    
    
    strokeWeight(1)
    line(ax, ay, x, y)
    strokeWeight(8)
    point(ax, ay)
    point(x, y)

    speed = PI/128
    step = 2

    a1 += speed
    a2 += speed * step
    
    
    
    
