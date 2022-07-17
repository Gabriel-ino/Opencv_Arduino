#include <Arduino.h>
#include <./cvzone.h>


SerialData serialData(1,1);
int valsRec[1];


#define LED_BITWISE (1<<5)
#define ANALOG_BITWISE (1<<0)

void setup() {
  // put your setup code here, to run once:
  serialData.begin();
  DDRB |= LED_BITWISE;
  DDRC |= ANALOG_BITWISE;
  while (1){
    serialData.Get(valsRec);
    digitalWrite(13, valsRec[0]);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}