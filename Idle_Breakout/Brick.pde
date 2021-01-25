class Brick {
  public float x, y, w, h, hue, top, left, right, bottom;
  public int val;
  public Boolean visible;
  public String type;
  Brick(float x, float y, int val) {
    this.x = x;
    this.y = y;
    this.val = val;
    this.w = 50;
    this.h = 25;
    visible = true;


    top = y;
    left = x;
    right = x + w;
    bottom = y + h;
  }

  void show() {
    visible = val > 0;
    push();
    //noStroke();
    colorMode(HSB);
    hue = map(val % 10, 0, 9, 0, 255);
    fill(hue, 255, 255);
    if (visible) {
      stroke(0);
      strokeWeight(1);
      rect(this.x+.5, this.y+.5, this.w-1, this.h-1, 7);
      fill(0);
      text(val, x+w/2, y +h/2);
    }
    colorMode(RGB);
    pop();
  }

  void collide(int amt) {
    if (visible) {
      amt = constrain(amt, 1, val);
      val -= amt;
      money += amt;
      if (val <= 0) {
        bricks.remove(this);
      }
    }
  }
}
