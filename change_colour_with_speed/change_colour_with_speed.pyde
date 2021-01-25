def setup():
    size(800, 600)
    
def draw():
    colorMode(HSB)
    fill(map(dist(pmouseX, pmouseY, mouseX, mouseY), 0, 100, 0, 255), 255, 255)

    
    ellipse(width/2, height/2, min(width, height), min(width,height))
