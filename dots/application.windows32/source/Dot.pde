class Dot {
  public float x;
  public float y;
  public float angle, r, d;
  public float speedX = .01;
  public float speedY = .01;
  public int id, maxNum;
  public Boolean visible;
  Dot(float x, float y, float d, int num, int maxNum) {
    this.x = x;
    this.y = y;
    this.r = d/2;
    this.d = d;
    this.id = num;
    this.maxNum = maxNum;
    this.visible = true;
    noStroke();
    //fill(255, 255, 255, 100);
    this.angle = random(0, TWO_PI);
    //ellipse(this.x, this.y, this.d, this.d);
  }
  void move() {
    if (width - this.x <= this.r || this.x <= this.r) {
      this.speedX = -this.speedX;
    }
    if (height - this.y <= this.r || this.y <= this.r) {
      this.speedY = -this.speedY;
    }




    float moveX = ((this.r * this.speedX ) * cos(this.angle))+this.x;
    float moveY = ((this.r * this.speedY ) * sin(this.angle))+this.y;
    this.x = moveX;
    this.y = moveY;
  }
  void show() {
    noStroke();

    float r = map(this.y, 0 + (this.r/2), height - (this.r/2), 0, 255);
    float g = map(this.x, 0 + (this.r/2), width - (this.r/2), 0, 255);
    float b = map(this.angle, 0, TWO_PI, 0, 255);
    float a = map(this.id, 0, this.maxNum, 50, 255);

    push();
    fill(r, g, b, a);

    if (this.visible) {
      ellipse(this.x, this.y, this.d, this.d);
    }
    pop();
    push();
    stroke(255);
    //point(this.x, this.y);
    pop();
  }

  void click() {
    if (dist(this.x, this.y, mouseX, mouseY) <= this.r && this.visible) {
      //print("Dot Clicked \n");
      this.visible = false;
      popped++;
    }
  }
}
