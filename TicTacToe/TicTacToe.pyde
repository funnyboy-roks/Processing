def setup():
    global tiles, current
    tiles = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    size(900, 900)
    current = "X"

def draw():
    global x, y
    background(200)
    x = int(mouseX//(width/3))
    y = int(mouseY//(height/3))
    
    full = True
    
    for x_pos in range(len(tiles)):
        if x_pos != 0:
            line(x_pos * width/3, 0, x_pos * width/3, height)
        
        for y_pos in range(len(tiles[x_pos])):
            if y_pos != 0:
                line(0, y_pos * height/3, width, y_pos * height/3)
            push()
            textSize(144)
            textAlign(CENTER, CENTER)
            fill(0)
            text(tiles[x_pos][y_pos], x_pos * width/3, y_pos * height/3, width/3, height/3)
            pop()
            
            if tiles[x_pos][y_pos] != "":
                checking = tiles[x_pos][y_pos]
                top_l = constrain(x_pos-1, 0, 2) == x_pos-1 and constrain(y_pos-1, 0, 2) == y_pos-1 and tiles[x_pos-1][y_pos-1] == checking
                top_c = constrain(y_pos-1, 0, 2) == y_pos-1 and tiles[x_pos  ][y_pos-1] == checking
                top_r = constrain(x_pos+1, 0, 2) == x_pos+1 and constrain(y_pos-1, 0, 2) == y_pos-1 and tiles[x_pos+1][y_pos-1] == checking
                
                cen_l = constrain(x_pos-1, 0, 2) == x_pos-1 and tiles[x_pos-1][y_pos  ] == checking
                cen_r = constrain(x_pos+1, 0, 2) == x_pos+1 and tiles[x_pos+1][y_pos  ] == checking
                
                bot_l = constrain(x_pos-1, 0, 2) == x_pos-1 and constrain(y_pos+1, 0, 2) == y_pos+1 and tiles[x_pos-1][y_pos+1] == checking
                bot_c = constrain(y_pos+1, 0, 2) == y_pos+1 and tiles[x_pos  ][y_pos+1] == checking
                bot_r = constrain(x_pos+1, 0, 2) == x_pos+1 and constrain(y_pos+1, 0, 2) == y_pos+1 and tiles[x_pos+1][y_pos+1] == checking
                
                if (top_l and bot_r) or (top_r and bot_l) or (cen_l and cen_r) or (top_c and bot_c):
                    stop(checking)
            else:
                full = False
            
        
    if full:
        stop("Tie")
    
    # print(x, y)
    push()
    textSize(144)
    textAlign(CENTER, CENTER)
    fill(100)
    if not tiles[x][y]:
        text(current, x * width/3, y * height/3, width/3, height/3)
    pop()
        
def mouseClicked():
    global current
    
    
    
    if not tiles[x][y]:
        tiles[x][y] = current
        if current == "X":
            current = "O"
        elif current == "O":
            current = "X"
            
def stop(player):
    
    textSize(72)
    if player == "Tie":
        textAlign(CENTER, CENTER)
        text("Tie!", width/2, height-100)
    else:
        textAlign(CENTER, CENTER)
        text("Player '{}' has won the game!".format(player), width/2, height-100)
    noLoop()
    
    
    
