#include<SoftwareSerial.h>
SoftwareSerial sim(11,12);
String number="+917708092094";
char inByte;
String temp;
String idata;
void setup() {
  Serial.begin(9600);
  sim.begin(9600);
  
}

void loop() {
  
 String s1 = Serial.readString();
 if(s1!="")
 {
 temp+=s1;
 sim.println("AT+CMGF=1"); 
  delay(1000); 
  sim.println("AT+CMGS=\"+919790050049\""); 
  delay(1000);
 sim.println(s1);
  delay(100);
  sim.println((char)26);
 }
 if(s1.equals("end"))
 {
  //
 }
 
 Serial.end();
 Serial.begin(9600);
}
