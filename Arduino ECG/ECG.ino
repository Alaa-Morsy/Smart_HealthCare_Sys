// https://www.youtube.com/watch?v=AK4Lp1Ko0l8

#include <WiFi.h>
#include <ThingSpeak.h>
WiFiClient client;

char ssid[] = "";
char pass[] = "";

unsigned long CHANNEL = 1680330;
const char * API  = "EGGDD5XE4A35W6MB";

void setup() {
// initialize the serial communication:
Serial.begin(9600);
ThingSpeak.begin(client);
pinMode(10, INPUT); // Setup for leads off detection LO +
pinMode(11, INPUT); // Setup for leads off detection LO -
}
 
void loop() {
 
if((digitalRead(10) == 1)||(digitalRead(11) == 1)){
Serial.println('!');
}
else{
// send the value of analog input 0:
delay(10);
Serial.println(analogRead(A0));
}
//Wait for a bit to keep serial data from saturating
delay(10);

//ThingSpeak
ThingSpeak.setField(5,analogRead(A0));
ThingSpeak.writeFields  (CHANNEL, API);
