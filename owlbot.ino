#include <Servo.h>
Servo head;
Servo leftWing;
Servo rightWing;

int headpos = 90;
int leftWingpos = 0;
int rightWingpos = 90;

//Variables
int speaker = 3;
int servo1 = 8;
int servo2 = 7;
int servo3 = 12;
int pir = 2;
int eyes = 9;
int light = 5;
int brightness;
int motion;
bool lastMotion = false;
int ran;
int direct;

void setup() {
  Serial.begin(9600);
  head.attach(servo1);
  leftWing.attach(servo2);
  rightWing.attach(servo3);
  
  for (int i = 0; i < 2; i++){
    analogWrite(eyes, 255);
    tone(speaker,1000); 
    delay(100);
    analogWrite(eyes, 0);
    noTone(speaker);
    delay(100);
  }
  pinMode(pir, INPUT);
  headSweep(); 
  //wingFlap();
}

void loop() {
  brightness = digitalRead(light);
  if (brightness == HIGH){
    analogWrite(eyes, 255);
  }else{
    analogWrite(eyes, 0);
  }

  motion = digitalRead(pir);
  //Serial.println(motion);
  if ((motion == HIGH)&&(lastMotion == false)){
    for (int i = 0; i < 2; i++){
      tone(speaker,250); 
      delay(200);
      noTone(speaker);
      delay(100);
    }
   direct = random(1,3);
   Serial.println(direct);
   if (direct == 1){
    for (headpos = 90; headpos <= 180; headpos++){
      head.write(headpos);
      delay(15);  
    }
    delay(1000);
    for (headpos = 180; headpos >= 90; headpos--){
      head.write(headpos);
      delay(15);
    }
   }else {
    for (headpos = 90; headpos >= 0; headpos--){
      head.write(headpos);
      delay(15);
    }
    delay(1000);
    for (headpos = 0; headpos <= 90; headpos++){
      head.write(headpos);
      delay(15);
    }
   }
  lastMotion = true;
  }
  
  if (motion == LOW){
    lastMotion = false;
  }

//new and untested!!!
  ran = random(1, 15000);
  Serial.println(ran);
  if (ran < 5){
    tone(speaker, 250);
    delay(1000);
    noTone(speaker);
  } else if((ran == 10)||(ran == 100)){
    wingFlap();
  } else if (ran == 50){
    wingFlap();
    delay(1500);
    wingFlap();
  } else if ((ran == 25)||(ran == 26)){
      for (int i = random(1, 5); i > 0; i--){
        analogWrite(eyes, 255);
        delay(100);
        analogWrite(eyes, 0);
        delay(100);
      }
  } else if ((ran == 30)||(ran == 35)){
    headSweep();
  }
}

void headSweep() {
  for (headpos = 90; headpos <= 180; headpos++){
    head.write(headpos);
    delay(15);
  }
  for (headpos = 180; headpos >= 0; headpos--){
    head.write(headpos);
    delay(15);
  }
  for (headpos = 0; headpos <= 90; headpos++){
    head.write(headpos);
    delay(15);
  }
}

void wingFlap(){
  for (leftWingpos = 90; leftWingpos <= 180; leftWingpos++){
    rightWingpos--;
    leftWing.write(leftWingpos);
    rightWing.write(rightWingpos);
    delay(15);
  }
  delay(100);
  for (leftWingpos = 180; leftWingpos >= 90; leftWingpos--){
    rightWingpos++;
    leftWing.write(leftWingpos);
    rightWing.write(rightWingpos);
    delay(15);
  }
}

