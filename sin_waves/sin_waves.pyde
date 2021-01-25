def setup():
    global a
    size(800, 600)
    a = 0
    
def draw():
    global a
    # background(200)
    a += .01
    line(0, height/2 + 100 * sin(a), width, height/2 + 100 * sin(a))
