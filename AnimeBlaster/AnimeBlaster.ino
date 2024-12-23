#include <IRremote.h> //adds the library code to the sketch
const int irReceiverPin = 8; //receiver module S pin is connected to arduino D8
IRrecv irrecv(irReceiverPin);  
decode_results results;  
IRsend irsend;  // Create an instance of the IRsend class
int sender = 3;  // The pin number connected to the IR LED


void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn();
  pinMode(sender, OUTPUT);  // Set the IR LED pin as an output
}


void loop() {
  if (Serial.available() > 0) {  // Check if data is available to read
    int color = Serial.read();  // Read one byte from serial
    sendIRCommand(color);  // Function to send IR commands
  }
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    Serial.println();
    irrecv.resume(); 
  }
}

void sendIRCommand(int color) {
  switch (color) {
    case 'a':  // OFF
      irsend.sendNEC(0xFF609F, 32);
      break;
    case 'b':  // ON
      irsend.sendNEC(0xFFE01F, 32);
      break;
    case '0':  // RED
      irsend.sendNEC(0xFF10EF, 32);
      break;
    case 93:  // R1
      irsend.sendNEC(0xFF30CF, 32);
      break;
    case '7':  // R2
      irsend.sendNEC(0xFF08F7, 32);
      break;
    case 95:  // R4
      irsend.sendNEC(0xFF28D7, 32);
      break;
    case '3':  // YELLOW
      irsend.sendNEC(0xFF18E7, 32);
      break;
    case '2':  // GREEN
      irsend.sendNEC(0xFF906F, 32);
      break;
    case '8':  // G1
      irsend.sendNEC(0xFFB04F, 32);
      break;
    case 9:  // G2
      irsend.sendNEC(0xFF8877, 32);
      break;
    case 10:  // G3
      irsend.sendNEC(0xFFA857, 32);
      break;
    case '4':  // CYAN
      irsend.sendNEC(0xFF9867, 32);
      break;
    case '1':  // BLUE
      irsend.sendNEC(0xFF50AF, 32);
      break;
    case 13:  // B1
      irsend.sendNEC(0xFF708F, 32);
      break;
    case '9':  // B2
      irsend.sendNEC(0xFF48B7, 32);
      break;
    case 15:  // B3
      irsend.sendNEC(0xFF6897, 32);
      break;
    case '5':  // PINK
      irsend.sendNEC(0xFF58A7, 32);
      break;
    case '6':  // WHITE
      irsend.sendNEC(0xFFC03F, 32);
      break;
    case 'u':  // UP
      irsend.sendNEC(0xFF00FF, 32);
      break;
    case 'd':  // DOWN
      irsend.sendNEC(0xFF40BF, 32);
      break;
    default:
      irsend.sendNEC(0xFFB04F, 32);  // Default command if none match
      break;
  }
  //send feedback
  Serial.print("Confirmed: ");
  Serial.println(color);
}
