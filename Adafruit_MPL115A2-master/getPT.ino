#include <Wire.h>
#include <Adafruit_MPL115A2.h>

Adafruit_MPL115A2 mpl115a2;

void setup(void)
{
  Serial.begin(9600);

  if (! mpl115a2.begin()) {
    Serial.println("Sensor not found! Check wiring");
    while (1);
  }

}

void loop(void)
{
  float pressureKPA = 0, temperatureC = 0;

  mpl115a2.getPT(&pressureKPA,&temperatureC);
  Serial.print(Serial.print(pressureKPA, 4); Serial.print(temperatureC, 1);

  delay(1000);
}
