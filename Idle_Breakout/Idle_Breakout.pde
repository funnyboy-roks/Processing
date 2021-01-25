String SEEK = "seek", NORM = "norm"; //SEEKing or NORMal ball types

int mouseClickAmount = 1;
int money = 0;
int level = 1;

int w = 16, h = 18;

//Ball ball = new Ball(1);
ArrayList<Ball>  balls  = new ArrayList();
ArrayList<Brick> bricks = new ArrayList();

Boolean startGame = true, gameActive = false, endGame = false;

//Brick brick = new Brick(400, 300, 5);

void setup() {
  size(800, 500);
  //frameRate(10);

  //bricks.add(new Brick(width/2, height/2, 100, 0));
  //bricks.add(new Brick(width/2 +200, height/2+200, 5, 1));


  balls.add (new Ball(5, SEEK));
  generateBricks();
}

void draw() {
  background(230);
  if (!gameActive && startGame) {
    drawStart();
  } else {
  }



  for (Ball ball : balls) {
    ball.move();
    ball.show();
  }

  for (Brick brick : bricks) {
    brick.show();
  }


  noStroke();
  rect(0, 0, width, height *.1);
  stroke(0);
  line(0, 0, width, 0);
  push();
  fill(0);
  textSize(32);
  text("$" + nfc(money), width-150, height *.075);
  pop();

  if (bricks.size() == 0) {
    level++;
    generateBricks();
  }




  if (keyPressed && key == 'g') {
    drawGrid();
  }
}

void mousePressed() {
  for (Brick brick : bricks) {
    if (mouseX >= brick.left && mouseX <= brick.right && mouseY >= brick.top && mouseY <= brick.bottom) {
      brick.collide(mouseClickAmount); 
      break;
    }
  }
}

void generateBricks() {
  for (int x = 0; x < width; x += 50) {
    for (float y = (height * 0.1); y < height; y += 25) {
      if (random(1) < 0.2) {
        bricks.add(new Brick(x, y, level));
      }
    }
  }
}

void drawStart() {
}


void drawGrid() {
  push();
  stroke(50);
  for (int x = 50; x < width; x+= 50) {
    line(x, 0, x, height);
  }

  for (int y = int(height * .1) + 25; y < height; y += 25) {
    line(0, y, width, y);
  }
  pop();
}
