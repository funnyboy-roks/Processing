class Ball {
  public float x, y, r, d, dx, dy;
  public float speed = 5;
  public int val, id;
  public String type;

  Ball(int val, String type) {
    dx = 1;
    dy = 1;
    this.val = val;
    this.r = 10;
    this.d = this.r * 2;
    this.type = type;
    newPos();
    while (!validSpot()) {
      newPos();
    }
  }

  void show() {
    //ellipseMode(CENTER);
    push();
    colorMode(HSB);
    fill(map(val, 0, 5, 100, 200), 255, 255);
    strokeWeight(1);
    stroke(0); 
    ellipse(x, y, this.d, this.d);
    pop();
    ellipseMode(CORNER);
  }

  void move() {
    if (this.x < 0 || this.x + this.d > width) {
      touchEdge(0);//Side edges = 0
    }
    if (this.y < height * .1 || this.y + this.d > height) {
      touchEdge(1);//Top edges = 0;
    }
    for (Brick brick : bricks) {
      if (checkCollide(brick))
        break;
    }



    this.x += this.dx * speed;
    this.y += this.dy * speed;
  }

  void newPos() {

    this.x = random(width  - this.d);
    this.y = random(height * 0.1, height - this.d);
  }
  Boolean validSpot() {
    Boolean status = true;
    for (Brick brick : bricks) {
      if (this.x + this.d >= brick.x && this.x <= brick.x + brick.w && this.y + this.d >= brick.y && this.y <= brick.y + brick.h) {
        status = false;
        break;
      }
    }
    return status;
  }

  Boolean checkCollide(Brick brick) {
    Boolean status = false;
    if (brick.visible) {
      //if I keep moving in my current X direction, will I collide with the center rectangle?
      if (this.x + this.d + this.dx * speed > brick.x && this.x + this.dx * speed < brick.x + brick.w && this.y + this.d > brick.y && this.y < brick.y + brick.h) {
        this.dx *= -1;
        brick.collide(this.val);
        status =  true;
      }

      //if I keep moving in my current Y direction, will I collide with the center rectangle?
      if (this.x + this.d > brick.x && this.x < brick.x + brick.w && this.y + this.d + this.dy * speed > brick.y && this.y + this.dy * speed < brick.y + brick.h) {
        this.dy *= -1;
        brick.collide(this.val);
        status =  true;
      }
    } 
    return status;
  }

  Brick nearestBrick() {
    Brick best = null;
    int bestIndex = 0;
    float bestDist = 10000;
    for (int i = 0; i < bricks.size(); i++) {
      Brick b = bricks.get(i);
      if (dist(this.x, this.y, b.x, b.y) < bestDist) {
        bestDist = dist(this.x, this.y, b.x, b.y);
        bestIndex = i;
      }
    }
    if (bricks.size()>0) {
      best = bricks.get(bestIndex);
      line(this.x + this.r, this.y + this.r, best.x + best.w/2, best.y + best.h/2);
    }
    return best;
  }

  void touchEdge(int edge) {

    if (type == SEEK) {
      Brick nearest = nearestBrick();
      if (nearest != null) {
        float angle = atan((this.x - nearest.x) / (this.y - nearest.y)) - HALF_PI;



        this.dx = cos(angle) * 1;
        this.dy = sin(angle) * 1;

        //this.dx = abs(this.x - nearest.x) * .2;
        //this.dy = abs(this.y - nearest.y) * .2;
      }
    }

    switch(edge) {
    case 0:
      this.dx *= -1;
      break;
    case 1:
      this.dy *= -1;
      break;
    }

    if (this.x <= 0)
      this.x = 1;
    if (this.x >= width)
      this.x = width - this.d - 1;
    if (this.y <= height * 0.1)
      this.y = height * 0.1 + 1;
    if (this.y >= height)
      this.y = height - this.d - 1;
  }
}
