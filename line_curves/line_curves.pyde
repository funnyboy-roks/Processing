def setup():
    global x, y
    size(800, 600)
    x = 0
    y = 0
    
def draw():
    global x, y
    line(0, y, x, height)
    
    x+= 5
    y += 5
