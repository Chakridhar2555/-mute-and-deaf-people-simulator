

LiquidCrystal lcd(13, 12, 11, 10, 9, 8); // Check circuit diagram for pin connections

void setup()

{

lcd.begin(16, 2);

}

void loop()

{

lcd.clear();

int val0 = analogRead(0); // read the input pin flex sensor pin 1

val0 = map(val0, 465, 590, 0, 9); // convert it into window of 0 to 9

int val1 = analogRead(1); // read the input pin flex sensor pin 2

val1 = map(val1, 435, 535, 0, 9);

// read the input pin

int val2 = analogRead(2); // read the input pin X axis pin

val2 = map(val2, 260, 415, 0, 9);

int val3 = analogRead(3); // read the input pin y axis pin

val3 = map(val3, 260, 420, 0, 9);

if (val0>=0 && val0<=0 && val1>=3 && val1<=4 && val2>=7 && val2<=8 && val3>=4 && val3<=5) // match the signs to standard store values values depend on wearing hands

{

lcd.print("I am __________________"); // Show message on LCD

digitalWrite(0,HIGH ); // select voice command 1 on APR 33A3

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7, LOW);

delay (100);

digitalWrite(0, LOW); // make it off

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else if (val0>=6 && val0<=7 && val1>=1 && val1<=2 && val2>=7 && val2<=8 && val3>=2 && val3<=3)

{

lcd.print("sorry");

digitalWrite(0,LOW ); // select voice command 2 on APR 33A3

digitalWrite(1,HIGH);

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7, LOW);

delay (100);

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else if (val0>=-1 && val0<=0 && val1>=3 && val1<=4 && val2>=1 && val2<=3 && val3>=0 && val3<=2)

{

lcd.print("Hello");

digitalWrite(0,LOW ); // select voice command 3 on APR 33A3

digitalWrite(1,LOW );

digitalWrite(2, HIGH);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7, LOW);

delay (100);

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else if (val0>=0 && val0<=0 && val1>=0 && val1<=1 && val2>=5 && val2<=6 && val3>=-0 && val3<=1)

{

lcd.print("Thank You");

digitalWrite(0,LOW ); // select voice command 4 on APR 33A3

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, HIGH);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7, LOW);

delay (100);

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else if (val0>=2 && val0<=3 && val1>=1 && val1<=1 && val2>=3 && val2<=5 && val3>=1 && val3<=2)

{

lcd.print("drink");

digitalWrite(0,LOW ); // select voice command 5 on APR 33A3

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, HIGH);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7, LOW);

delay (100);

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else if (val0>=4 && val0<=5 && val1>=2 && val1<=3 && val2>=4 && val2<=6 && val3>=0 && val3<=2)

{

lcd.print("beautiful");

digitalWrite(0,LOW ); // select voice command 6 on APR 33A3

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, HIGH);

digitalWrite(6, LOW);

digitalWrite(7, LOW);

delay (100);

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else if (val0>=0 && val0<=0 && val1>=4 && val1<=6 && val2>=4 && val2<=5 && val3>=1 && val3<=2)

{

lcd.print("bye");

digitalWrite(0,LOW ); // select voice command 7 on APR 33A3

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, HIGH);

digitalWrite(7, LOW);

delay (100);

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else if (val0>=0 && val0<=1 && val1>=0 && val1<=1 && val2>=7 && val2<=8 && val3>=1 && val3<=2)

{

lcd.print("sick");

digitalWrite(0,LOW ); // select voice command 8 on APR 33A3

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7, HIGH);

delay (100);

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

delay(5000);

}

else

{

lcd.print(" System on "); // inital message

digitalWrite(0, LOW);

digitalWrite(1,LOW );

digitalWrite(2, LOW);

digitalWrite(3, LOW);

digitalWrite(4, LOW);

digitalWrite(5, LOW);

digitalWrite(6, LOW);

digitalWrite(7,LOW);

}

delay(200); // delay of 200 msec


