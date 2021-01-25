def setup():
    size(400, 400)
    noLoop()
def draw():
    for x in range(width):
        for y in range(height):
            colorMode(HSB)
            h = map(x, 0, width-1, 0, 255)
            s = map(y, 0, height-1, 255, 0)
            stroke(h, s, 255)
            point(x, y)
    
