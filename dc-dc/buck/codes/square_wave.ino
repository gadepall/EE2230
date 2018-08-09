void setup(){
  pinMode(13,OUTPUT);
  
}

void loop(){
  digitalWrite(13,LOW);
  delayMicroseconds(10);
  digitalWrite(13,HIGH);
  delayMicroseconds(10);
  
}
