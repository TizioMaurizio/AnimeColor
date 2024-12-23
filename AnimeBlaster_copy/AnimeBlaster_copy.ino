#include <IRremote.h>

const int IR_SEND_PIN = 3; // Pin connected to the IR LED
IRsend irsend;

void setup() {
  Serial.begin(9600);
  irsend.begin(IR_SEND_PIN);
  Serial.println("IR Remote ready. Send a color code via Serial.");
}

void loop() {
  if (Serial.available() > 0) {
    char color = Serial.read();
    switch (color) {
      case '8':  // OFF
        irsend.sendNEC(0xFF609F, 32);
        Serial.println("OFF");
        break;
      case '9':  // ON
        irsend.sendNEC(0xFFE01F, 32);
        Serial.println("ON");
        break;
      case '0':  // RED
        irsend.sendNEC(0xFF10EF, 32);
        Serial.println("RED");
        break;
      case '3':  // YELLOW
        irsend.sendNEC(0xFF18E7, 32);
        Serial.println("YELLOW");
        break;
      case '2':  // GREEN
        irsend.sendNEC(0xFF906F, 32);
        Serial.println("GREEN");
        break;
      case '4':  // CYAN
        irsend.sendNEC(0xFF9867, 32);
        Serial.println("CYAN");
        break;
      case '1':  // BLUE
        irsend.sendNEC(0xFF50AF, 32);
        Serial.println("BLUE");
        break;
      case '5':  // PINK
        irsend.sendNEC(0xFF58A7, 32);
        Serial.println("PINK");
        break;
      case '6':  // WHITE
        irsend.sendNEC(0xFFC03F, 32);
        Serial.println("WHITE");
        break;
      default:
        Serial.println("Invalid color code");
        break;
    }
  }
}
