import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class dots extends PApplet {


int dotTotal = 10;
int popped = 0;
Dot[] dots = new Dot[dotTotal];
//Dot dot;
public void setup() {
  ellipseMode(CENTER);
  //size(800,600);
  
  background(0);

  //dot = new Dot(300,300, 10);
  for (int i = 0; i < dotTotal; i ++) {
    float w = random(50, 150);
    dots[i] = new Dot(random((w/2), width-(w/2)), random((w/2), height-(w/2)), w, i, dotTotal);
  }
}

public void draw() {
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

public void keyPressed() {
  setup();
}

public void mousePressed() {
  for (Dot dot : dots) {
    dot.click();
  }
}
class Dot {
  public float x;
  public float y;
  public float angle, r, d;
  public float speedX = .01f;
  public float speedY = .01f;
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
  public void move() {
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
  public void show() {
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

  public void click() {
    if (dist(this.x, this.y, mouseX, mouseY) <= this.r && this.visible) {
      //print("Dot Clicked \n");
      this.visible = false;
      popped++;
    }
  }
}
  public void settings() {  fullScreen(); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "dots" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
