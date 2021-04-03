#include<Servo.h>

Servo upper;
Servo lower;

void setup() 
{
  
  upper.attach(0);
  lower.attach(2);
  upper.write(90);
  lower.write(90);
  Serial.println("Setup done"); 
  Serial.begin(9600);
}

void loop() 
{
  
  
  if (Serial.available())
  {
    char point = Serial.read();
    switch (point)
    {
      case 'r':
        upper.write(14);
        lower.write(180);
        break;
      case 'p':
        upper.write(90);
        lower.write(90);
        break;
      case 's':
        upper.write(90);
        lower.write(180);
        break;
      case 'a':
        upper.write(90);
        lower.write(90);
        break;
    }  // End of switch
  }  // End of if
  delay(50);  // I have no idea why, but most programs of this sort have a delay in.  (Hope someone explains to me too)
}  // End of functi
 
