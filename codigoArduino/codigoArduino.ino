#include <Servo.h>

Servo servo1, servo2, servo3, servo4, servo5;

const unsigned int BAUD_RATE = 9600;
int byteEnt;
int angulo1 = 90, angulo2 = 175, angulo3 = 10, angulo4 = 90, angulo5 = 90;

void setup() {
  // put your setup code here, to run once:
  servo1.attach(D3);
  servo2.attach(D4);
  servo3.attach(D5);
  servo4.attach(D6);
  servo5.attach(D7);
  
  Serial.begin(BAUD_RATE);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    /*for(int i = 0; i<=12; i++){
      byteEnt[i] = Serial.read();
      }*/
     byteEnt = Serial.read();
    if(byteEnt == 'a'){
      angulo1 = angulo1 + 5;
      servo1.write(angulo1);
      delay(100);
      }else if(byteEnt == 'b'){
        angulo1 = angulo1 - 5;
        servo1.write(angulo1);
        delay(100);
        }

    if(byteEnt == 'c'){
      angulo2 = angulo2 + 5;
      servo2.write(angulo2);
      delay(100);
      }else if(byteEnt == 'd'){
        angulo2 = angulo2 - 5;
        servo2.write(angulo2);
        delay(100);
        }

    if(byteEnt == 'e'){
      angulo3 = angulo3 + 5;
      servo3.write(angulo3);
      delay(100);
      }else if(byteEnt == 'f'){
        angulo3 = angulo3 - 5;
        servo3.write(angulo3);
        delay(100);
        }

    if(byteEnt == 'g'){
      angulo4 = angulo4 + 5;
      servo4.write(angulo4);
      delay(100);
      }else if(byteEnt == 'h'){
        angulo4 = angulo4 - 5;
        servo4.write(angulo4);
        delay(100);
        }

    if(byteEnt == 'i'){
      angulo5 = angulo5 + 5;
      servo5.write(angulo5);
      delay(100);
      }else if(byteEnt == 'j'){
        angulo5 = angulo5 - 5;
        servo5.write(angulo5);
        delay(100);
        }

    /*if(byteEnt[0] == 'u'){
        //posicion 1
        servo1.write(byteEnt[1]);
        servo2.write(byteEnt[2]);
        servo3.write(byteEnt[3]);
        servo4.write(byteEnt[4]);
        servo5.write(byteEnt[5]);
        delay(100);
        //posicion 2
        servo1.write(byteEnt[6]);
        servo2.write(byteEnt[7]);
        servo3.write(byteEnt[8]);
        servo4.write(byteEnt[9]);
        servo5.write(byteEnt[10]);
        
      }*/

    if(byteEnt == 'r'){
      angulo1=90;
      servo1.write(angulo1);
      angulo2=175;
      servo2.write(angulo2);
      angulo3=10;
      servo3.write(angulo3);
      angulo4=90;
      servo4.write(angulo4);
      angulo5=90;
      servo5.write(angulo5);
      delay(100);
      }
    }
}
