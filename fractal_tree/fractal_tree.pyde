
def setup():
    size(600, 400)

def draw():
    global theta
    background(0);
    frameRate(30);
    stroke(255);
    a = (mouseX / float(width)) * 90;
    theta = radians(a);
    translate(width/2,height);
    line(0,0,0,-120);
    translate(0,-120);
    branch(120);
    
def branch(l):
    
    l *= .66
    
    if l > 1:
        pushMatrix()
        rotate(theta)
        line(0, 0, 0, -l)
        translate(0, -l)
        branch(l)
        popMatrix()
        
        pushMatrix()
        rotate(-theta)
        line(0, 0, 0, -l)
        translate(0, -l)
        branch(l)
        popMatrix()
        
    
