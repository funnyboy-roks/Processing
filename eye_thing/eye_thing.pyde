from objs import *

def setup():
    noStroke()
    global eyes, r
    
    r = 25
    count = 0
    
    eyes = []
    
    size(800, 600)
    # eye = Eye(100, 100)
    # eye2 = Eye(100, 200)
    for x in range(5):
        eyes.append([])
        for y in range(5):
            eyes[x].append(Eye(x * r + r/2, y * r + r/2, r))
            count += 1
            
    print(count)
            
    
def draw():
    background(200)
    for x in eyes:
        for y in x:
            y.update()
    
