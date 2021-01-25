def setup():
    global s, x_count, y_count, tiles, covers
    s = 50

    x_count = width//s
    y_count = height//s
    size(800, 600)
    
    tiles = []
    covers = []
    
    for x in range(x_count):
        tiles.append([])
        covers.append([])
        for y in range(y_count):
            tiles[x].append("bomb" if random(0, 1) < .2 else 0)
            covers[x].append(True)
            
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            tiles[x][y] = surrounding_total(x, y)
    print(tiles)
def draw():
    background(200)
    
    for x in range(x_count+1):
        line(x * s, 0, x * s, height)
    for y in range(y_count+1):
        line(0, y * s, width, y * s)
        
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            fill(0)
            textAlign(CENTER, CENTER)
            if tiles[x][y] == "bomb":
                push()
                ellipseMode(CORNER)
                ellipse(x * s + 10, y * s + 10, s-20, s-20)
                pop()
            else:
                text(tiles[x][y] if tiles[x][y] != 0 else "", x*s + s/2, y*s + s/2)
                
            
            
            
def surrounding_total(x_pos, y_pos):
    on_left = on_right = on_top = on_bot = False
    top_l = top_c = top_r = cen_l = cen_r = bot_l = bot_c = bot_r = False
    if tiles[x_pos][y_pos] == "bomb":
        return "bomb"
    if not x_pos-1 == abs(x_pos-1): # If on left edge
        on_left = True
        cen_r = tiles[x_pos+1][y_pos  ] == "bomb"
    if not x_pos+1 == constrain(x_pos+1, 0, x_count-1): # If on right edge
        on_right = True
        cen_l = tiles[x_pos-1][y_pos  ] == "bomb"
    if not y_pos-1 == abs(y_pos-1): # If on top edge
        on_top = True
        bot_c = tiles[x_pos  ][y_pos+1] == "bomb"
    if not y_pos+1 == constrain(y_pos+1, 0, y_count-1): # If on bottom edge
        on_bot = True
        top_c = tiles[x_pos  ][y_pos-1] == "bomb"
    elif on_left and on_top:
        bot_r = tiles[x_pos+1][y_pos+1] == "bomb"
    elif on_right and on_top:
        bot_l = tiles[x_pos-1][y_pos+1] == "bomb"
    elif on_left and on_bot:
        top_r = tiles[x_pos+1][y_pos-1] == "bomb"
    elif on_right and on_bot:
        top_l = tiles[x_pos-1][y_pos-1] == "bomb"
    elif not on_left or on_right:
        cen_l = tiles[x_pos-1][y_pos  ] == "bomb"
        cen_r = tiles[x_pos+1][y_pos  ] == "bomb"
    else:
        top_l = tiles[x_pos-1][y_pos-1] == "bomb"#
        top_c = tiles[x_pos  ][y_pos-1] == "bomb"#
        top_r = tiles[x_pos+1][y_pos-1] == "bomb"#
        
        cen_l = tiles[x_pos-1][y_pos  ] == "bomb"#
        cen_r = tiles[x_pos+1][y_pos  ] == "bomb"#
        
        bot_l = tiles[x_pos-1][y_pos+1] == "bomb"#
        bot_c = tiles[x_pos  ][y_pos+1] == "bomb"#
        bot_r = tiles[x_pos+1][y_pos+1] == "bomb"#
    return top_l + top_c + top_r + cen_l + cen_r + bot_l + bot_c + bot_r
    
    
