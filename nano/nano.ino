/*
 * See documentation at https://nRF24.github.io/RF24
 * See License information at root directory of this library
 * Author: Brendan Doherty (2bndy5)
 */

/**
 * A simple example of sending data from 1 nRF24L01 transceiver to another.
 *
 * This example was written to be used on 2 devices acting as "nodes".
 * Use the Serial Monitor to change each node's behavior.
 */
#include <SPI.h>
#include <RF24.h>

// instantiate an object for the nRF24L01 transceiver
RF24 radio(7, 8);  // using pin 7 for the CE pin, and pin 8 for the CSN pin

const byte address[6] = "00001"; // Define the address of the receiving NRF24L01+ module.

void setup() {

  Serial.begin(115200);
  while (!Serial) {}
  // initialize the transceiver on the SPI bus
  if (!radio.begin()) {
    Serial.println(F("radio hardware is not responding!!"));
    while (1) {}  // hold in infinite loop
  }

  radio.setPALevel(RF24_PA_LOW);  // RF24_PA_MAX is default.
  radio.openWritingPipe(address);  // always uses pipe 0
  radio.stopListening();  // put radio in TX mode
} 

void loop() {
    // change the role via the serial monitor
    byte buf[4];
    if (Serial.available() > 0)  {
      Serial.readBytes(buf,4);
//      Serial.print("Sending value: ");
//      Serial.println(message);
      bool report = radio.write(&buf, 4);
      if (report) {
        Serial.println("Transmited successfully! ");
      }
    }
    delay(50);
}  // loop
