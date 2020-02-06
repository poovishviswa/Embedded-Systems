#include<SoftwareSerial.h>
int rx=5;
int tx=6;          
char inByte=' ';                
     String temp=" ";
     String s2;                        
SoftwareSerial myserial(rx,tx);
void setup() {
Serial.begin(9600);
myserial.begin(9600);  
s2="end";
}

void loop() {
 
 String s1 = Serial.readString();
 if(s1!="")
 {
 myserial.println(s1);
 temp+=s1;
 }
 if(s1.equals("end"))
 {
  myserial.println("final");
  myserial.println(temp);
 }
 
 Serial.end();
 Serial.begin(9600);
 
}
