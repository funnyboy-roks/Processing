class Eye:
    def __init__(self, x, y, r = 25):
        self.x = x*2
        self.y = y*2
        self.r = r
        self.w = self.r*2
        self.h = self.r*2
        self.cx = x
        self.cy = y
        
    def update(self):
        
        c = max(dist(mouseX, mouseY, self.x, self.y), 0.001)
        angle = acos((self.y-mouseY)/c)
        if mouseX < self.x:
            angle *= -1
        self.cx = sin(angle) * constrain(c, 0, self.r/2) + self.x
        self.cy = -cos(angle) * constrain(c, 0, self.r/2) + self.y
        
        c2 = max(dist(mouseX, mouseY, self.cx, self.cy), 0.001)
        angle2 = acos((self.cy-mouseY)/c2)
        self.cx2 = sin(angle) * constrain(c, 0, self.r/4) + self.cx
        self.cy2 = -cos(angle) * constrain(c, 0, self.r/4) + self.cy
        
        push()
        ellipseMode(CENTER)
        colorMode(RGB)
        fill(255)        
        ellipse(self.x, self.y, self.w, self.h)
        colorMode(HSB)
        # fill(map(angle, -PI, PI, 0, 255), 255, 255)
        fill(0)
        ellipse(self.cx, self.cy, self.w/2, self.h/2)
        fill(100)
        # fill(map(angle, -PI, PI, 0, 255), 255, 255)
        # ellipse(self.cx2, self.cy2, self.w/4, self.h/4)
        pop()
        
        
