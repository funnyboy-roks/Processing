
int dotTotal = 10;
int popped = 0;
Dot[] dots = new Dot[dotTotal];
//Dot dot;
void setup() {
  ellipseMode(CENTER);
  //size(800,600);
  fullScreen();
  background(0);

  //dot = new Dot(300,300, 10);
  for (int i = 0; i < dotTotal; i ++) {
    float w = random(50, 150);
    dots[i] = new Dot(random((w/2), width-(w/2)), random((w/2), height-(w/2)), w, i, dotTotal);
  }
}

void draw() {
  background(0);

  //if (frameCount % 10 == 0) {
  for (Dot dot : dots) {
    dot.move();
    dot.show();
  }
  //}

  //dot.move();
  text(popped, 100, 100);
  if (mousePressed) {
    for (Dot dot : dots) {
      dot.click();
    }
  }
}

void keyPressed() {
  setup();
}

void mousePressed() {
  for (Dot dot : dots) {
    dot.click();
  }
}
