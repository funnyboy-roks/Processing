float angle = 0;
int starMax = 100;
int houseHeight = 750;
ArrayList<PVector> stars = new ArrayList<PVector>();
PImage cloud;

void setup() {
  fullScreen();
  for (int i = 0; i < starMax; i++) {
    stars.add(new PVector(random(0, width), random(0, height-220)));
  }
  cloud = loadImage("cloud.png");
}



void draw() {

  // Background, Stars, and Clouds
  if (mouseX < 900 || mouseX > 1840) {
    background(#003366);
    for (PVector star : stars) {
      stroke(#FFFF00);
      strokeWeight(5);
      point(star.x, star.y);
    }
  } else {
    background(#87ceeb);
     float x = map(mouseX, 0, width, 0, width/2);
    image(cloud, x -cloud.width/2, 0);
    image(cloud, x/2 +cloud.width/2, 0);
    image(cloud, x -cloud.width, 0);
    image(cloud, x/2 -cloud.width *2 , 0);
    
  }
  

  stroke(0);
  strokeWeight(2);
  // Grass Layer
  fill(#00FF00);
  rect(0, height-220, width, height-200);

  // Dirt Layer
  fill(#654321);
  rect(0, height-200, width, height);

  // House Thing
  push();
  fill(255);
  strokeWeight(5);
  stroke(0);
  rect(1000, 1600, 750, -houseHeight);
  pop();

  // Sun Thing
  angle = map(mouseX, 0, width, 0, TWO_PI);
  push();
  noStroke();
  translate(width/2, height);
  rotate(angle);
  fill(#FDB813);
  ellipse(0, height-200, 100, 100);
  pop();
}

void keyPressed(){
  if(keyCode == UP){
    houseHeight += 50;
  }
  if(keyCode == DOWN){
    houseHeight -= 50;
  }
}
