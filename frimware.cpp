#include <EEPROM.h>

#define BAUD_RATE 2400
#define EEPROM_SIZE 1024 // Assume EEPROM size is 1024 bytes

void setup() {
  Serial.begin(BAUD_RATE);
}

void loop() {
  if (Serial.available()) {
    int index = 0;
    while (Serial.available() && index < EEPROM_SIZE) {
      char c = Serial.read();
      EEPROM.write(index++, c);
      Serial.print(c); // Echo back to PC
    }
  }
}
