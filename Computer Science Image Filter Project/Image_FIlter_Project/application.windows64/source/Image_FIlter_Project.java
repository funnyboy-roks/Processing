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

public class Image_FIlter_Project extends PApplet {

boolean PicLoaded = false;
boolean Grayscale = false;
boolean Effect1 = false;
boolean Effect2 = false;
boolean Effect3 = false;
int picWidth = 0;
int picHeight = 0;
PImage img;
float changeAmt = 50;

/***********************************/

public void setup() 
{
  
  background(185);
  textAlign(LEFT);
  textSize(16); 
}

public void draw()
{

  background(185);
  noStroke();
  int picStart = 0;
  int picEnd = 0;
  
  /* draw buttons */

  stroke(0);
  fill(0);
  textSize(16);
  text("File Operations",665,30);
  line(650,0,650,480);
  noStroke();
  
  fill(255);
  rect(660, 50, 130, 40, 10);
  fill(55);
  text("Load Picture", 675, 75);

  fill(255);
  rect(660, 100, 130, 40, 10);
  fill(55);
  text("Save Picture", 675, 125);

  stroke(0);
  line(650,150,800,150);
  noStroke();

  stroke(0);
  fill(0);
  textSize(16);
  text("Filter Effects",675,180);
  line(650,0,650,480);
  noStroke();

  if (Grayscale)
    fill(0xffFFFF7D);    //Effect on means a yellow lighted button
  else
    fill(255);
  rect(660, 200, 130, 40, 10);
  fill(55);
  text("Grayscale", 680, 225);
  
  if (Effect1)
    fill(0xffFFFF7D);    //Effect on means a yellow lighted button
  else
    fill(255);
  rect(660, 250, 130, 40, 10);
  fill(55);
  text("Brighten", 680, 275);

  if (Effect2)
    fill (0xffFFFF7D);     //Effect on means a yellow lighted button 
  else
    fill(255); 
  rect(660, 300, 130, 40, 10);
  fill(55);
  text("Darken", 680, 325);

  if (Effect3)
    fill (0xffFFFF7D);    //Effect on means a yellow lighted button
  else
    fill(255);   
  rect(660, 350, 130, 40, 10);
  fill(55);
  text("Inver Colours", 680, 375);

  noStroke();
  textSize(16);

  //The following loads and displays an image file.
  //The image is resized to best fit in a 640x480 frame.
  if (PicLoaded)
  {     
    picWidth = img.width;
    picHeight = img.height;
    
    if (picWidth > 640)
    {
      picHeight = (int)(picHeight*(640.0f/picWidth));
      picWidth = 640;
    }
    if (picHeight > 480)
    {
      picWidth = (int)(picWidth*(480.0f/picHeight));
      picHeight = 480;
    }
    image(img, 0, 0, picWidth, picHeight);
    
    picStart = 0;
    picEnd = picStart+width*picHeight;

    loadPixels();
    
    /***** Effects Code *****/

    /* This sample grayscale code may serve as an example */
    if (Grayscale)
    {
      int i = picStart;
      while (i < picEnd) 
      {
        int c = pixels[i];
        float gray = (red(c)+green(c)+blue(c))/3.0f;  //average the RGB colors
        pixels[i] = color(gray, gray, gray);
        i = i + 1;
        if (i % width >= picWidth)        // This will ignore anything on the line that 
          i = i + width - picWidth;       // after the image (such as buttons)
      }   
    }

    if (Effect1)
    {
      // Lighten Image
      int i = picStart;
      while (i < picEnd) 
      {
        int c = pixels[i];
         //average the RGB colors
        pixels[i] = color(red(c)+changeAmt, green(c)+changeAmt, blue(c)+changeAmt);
        i = i + 1;
        if (i % width >= picWidth)        // This will ignore anything on the line that 
          i = i + width - picWidth;       // after the image (such as buttons)
      }  
      
    }

    if (Effect2)
    {
      // Darken Image
      int i = picStart;
      while (i < picEnd) 
      {
        int c = pixels[i];
         //average the RGB colors
        pixels[i] = color(red(c)-changeAmt, green(c)-changeAmt, blue(c)-changeAmt);
        i = i + 1;
        if (i % width >= picWidth)        // This will ignore anything on the line that 
          i = i + width - picWidth;       // after the image (such as buttons)
      } 
    }
    
    if (Effect3)
    {
      // Not sure
      int i = picStart;
      while (i < picEnd) 
      {
        int c = pixels[i];
         //average the RGB colors
         float red = map(red(c), 0, 255, 255, 0);
         float green = map(green(c), 0, 255, 255, 0);
         float blue = map(blue(c), 0, 255, 255, 0);
        pixels[i] = color(red, green, blue);
        i = i + 1;
        if (i % width >= picWidth)        // This will ignore anything on the line that 
          i = i + width - picWidth;       // after the image (such as buttons)
      } 
    }
    
    updatePixels(); 
    redraw();
  }
  
  fill(255);
  noStroke();
}

public void mouseClicked() {
  
  redraw();
}

public void mousePressed()
{
  //The following define the clickable bounding boxes for any buttons used.
  //Note that these boundaries should match those drawn in the draw() function.
  
  if (mouseX>660 && mouseX<790 && mouseY>50 && mouseY<90)
  {
    selectInput("Select a file to process:", "infileSelected");
  }
  
  if (mouseX>660 && mouseX<790 && mouseY>100 && mouseY<140)
  {
    selectOutput("Select a file to write to:", "outfileSelected");
  }
  
  if (mouseX>660 && mouseX<790 && mouseY>200 && mouseY<240 && PicLoaded)
  {
    Grayscale = !Grayscale;
  }   
  
  if (mouseX>660 && mouseX<790 && mouseY>250 && mouseY<290 && PicLoaded)
  {
    Effect1 = !Effect1;
  } 

  if (mouseX>660 && mouseX<790 && mouseY>300 && mouseY<340 && PicLoaded)
  {
    Effect2 = !Effect2;
  }  

  if (mouseX>660 && mouseX<790 && mouseY>350 && mouseY<390 && PicLoaded)
  {
    Effect3 = !Effect3;
  } 

  redraw();
}

public void infileSelected(File selection) 
{
  if (selection == null) 
  {
    println("IMAGE NOT LOADED: Window was closed or the user hit cancel.");
  } 
  else 
  {
    println("IMAGE LOADED: User selected " + selection.getAbsolutePath());
    img = loadImage(selection.getAbsolutePath());
    PicLoaded = true;
    Grayscale = false;
    Effect1 = false;
    Effect2 = false;
    Effect3 = false;
    redraw();
  }
}

public void outfileSelected(File selection) 
{
  if (selection == null) 
  {
    println("IMAGE NOT SAVED: Window was closed or the user hit cancel.");
  } 
  else 
  {
    println("IMAGE SAVED: User selected " + selection.getAbsolutePath() + ".png");
    noLoop();
    updatePixels();
    redraw();
    save(selection.getAbsolutePath()+".png");
    redraw();
    loop();
  }
}
  public void settings() {  size(800, 480); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Image_FIlter_Project" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
