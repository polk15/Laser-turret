#include <Servo.h>

#define LEFT_BOUND 20
#define RIGHT_BOUND 160
#define DOWN_BOUND 20
#define UP_BOUND 160

Servo serX, serY;

int x = (LEFT_BOUND + RIGHT_BOUND)/2;
int y = (DOWN_BOUND + UP_BOUND)/2;

String serialData;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(5);
  serX.attach(9);
  serY.attach(10);
}

void loop() {
}

void serialEvent() {
  serialData = Serial.readString();
  serX.write(parseDataX(serialData));
  serY.write(parseDataY(serialData));
}

int parseDataX(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parseDataY(String data){
  data.remove(0,data.indexOf("Y") + 1);
  return data.toInt();
}
