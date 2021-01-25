def setup():
    global dots
    size(800, 600)
    dots = []
    for _ in range(50):
        # dots.append([random(width), random(height), random(-5, 5), random(-5, 5)])
        dots.append({
                     "x": random(width),
                     "y": random(height),
                     "vx": random(-5, 5),
                     "vy": random(-5, 5)
                     })
    
def draw():
    
    background(200)
    
    closest = None
    closest_d = 0
    
    for pos in dots:
        strokeWeight(8)
        # if dist(pos["x"], pos["y"], mouseX, mouseY) <= 150:
        point(pos["x"], pos["y"])
        strokeWeight(1)
        pos["x"] += pos["vx"]
        pos["y"] += pos["vy"]
        
        if pos["x"] >= width or pos["x"] <= 0:
            pos["vx"] *= -1
        if pos["y"] >= height or pos["y"] <= 0:
            pos["vy"] *= -1
        
        # if dist(pos["x"], pos["y"], mouseX, mouseY) > closest_d:
        #     closest_d = dist(pos["x"], pos["y"], mouseX, mouseY)
        #     closest = pos
        if dist(pos["x"], pos["y"], mouseX, mouseY) <= 100:
            line(pos["x"], pos["y"], mouseX, mouseY)
    # line(closest["x"], closest["y"], mouseX, mouseY)
