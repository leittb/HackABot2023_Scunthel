// Basic test of Mona robot including proximity sensors and open-loop motion control

#include <RF24.h>
// instantiate an object for the nRF24L01 transceiver
RF24 radio(7, 8);  // using pin 7 for the CE pin, and pin 8 for the CSN pin
// Let these addresses be used for the pair
int payload = 0;
const byte address[6] = "00001"; // Define the address of the receiving NRF24L01+ module.
// pin config for basic platform test
// Motors
int Motor_right_PWM = 10;  //   0 (min speed) - 255 (max speed) 
int Motor_right_direction = 5;  //   0 Forward - 1 Reverse
int Motor_left_PWM = 9;    //   0 (min speed) - 255 (max speed)  
int Motor_left_direction = 6;   //   0 Forward - 1 Reverse
#define Forward 0
#define Reverse 1

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  // initialize Ports
  pinMode(Motor_left_PWM, OUTPUT);
  pinMode(Motor_right_PWM, OUTPUT);
  radio.begin();
  // Set the PA Level low to try preventing power supply related problems
  // because these examples are likely run with nodes in close proximity to
  // each other.
  radio.setPALevel(RF24_PA_LOW);  // RF24_PA_MAX is default.

  // save on transmission time by setting the radio to only transmit the
  // number of bytes we need to transmit a float
  //radio.setPayloadSize(sizeof(payload));  // float datatype occupies 4 bytes

  // set the RX address of the TX node into a RX pipe
  radio.openReadingPipe(1, address);  // using pipe 1
  //radio.setDataRate(RF24_2MBPS);
  // additional setup specific to the node's role
  radio.startListening();  // put radio in RX mo
}

// the loop routine runs over and over again forever:
void loop() {
    uint8_t pipe;
    if (radio.available(&pipe)) {  
      //uint8_t bytes = radio.getPayloadSize();  // get the size of the payload
      byte data[4];
      radio.read(&data, 4);
      long val = 0;
      val += data[0] << 24;
      val += data[1] << 16;
      val += data[2] << 8;
      val += data[3];
      //Serial.println(data);
      String receivedString = String(val);
      //receivedString.trim(); // remove any leading/trailing white space
      int values[5]; // array to store the split values
      values[0] = receivedString[0]- '0';
      values[1] = receivedString[1]- '0';
      values[2] = receivedString[2]- '0';
      values[3] = receivedString.substring(3,6).toInt();
      values[4] = receivedString.substring(6,9).toInt();
      Serial.print(values[0]);Serial.print(",");
      Serial.print(values[1]);Serial.print(",");
      Serial.print(values[2]);Serial.print(",");
      Serial.print(values[3]);Serial.print(",");
      Serial.print(values[4]);Serial.println(",");
      if (values[0]==7){
        Serial.print("I'm moving!");
        analogWrite(Motor_right_PWM,values[4] ); // right motor
        digitalWrite(Motor_right_direction,values[2]); //right
        analogWrite(Motor_left_PWM, values[3]); // left 
        digitalWrite(Motor_left_direction,values[1]); //left
      }
      /*
      Serial.print(bytes);  // print the size of the payload
      Serial.print(F(" bytes on pipe "));
      Serial.print(pipe);  // print the pipe number
      Serial.print(F(": "));
      Serial.println(payload);  // print the payload's value
      */
      delay(50);        // delay in between reads for stability
    }
 
}
