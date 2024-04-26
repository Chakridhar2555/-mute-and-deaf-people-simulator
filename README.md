# -mute-and-deaf-people-simulator
Digital vocalizer is a project for social purpose. we are trying to implement a system which make a communication gap between deaf peoples and hearing people as less as possible. Deaf people make use of sign language or gestures to make understand what he/she trying to say but it is impossible to understand by hearing people. So, that we come on conclusion to make a simple prototype by taking some of those gesture and convert it into audio and visual form so that they can understand by everyone. For that we are making use of arduino UNO Board as Atmega 328 Controller board to interface all of the sensors and actuators.

Basically an Artificial Neural Network is the concept of our prototype. Some sensors are placed on the hand of deaf people which converts the parameter like finger bend hand position angle into electrical signal and provide it to Atmega 328 controller and controller take action according to the sign.

Advantages of innovation

1. It is a social cause project

2. Deaf people can easily communicate with normal people

3. Easy to implement

4. Easy to make change of sensor windows according to wearing hand

5. Portable design works on 9V small Radio battery

6. Audio as well as Visual output

Limitations of innovations

1. Currently due to cost of sensors and funds limitation we choose limited gestures which can perform by single hand

2. We have divided our project in three parts for simplicity

· Sensor board

For this we required two type of sensors and following components

1. Flex sensors 2 unit to measure bend of fingers

2. ADXL 335 to get x and y axis x coordinates of hand

3. 10K ohms resistance 2 unit to form voltage divider bias with flex sensor

4. small PCB (copper clad 2 inch X 2 inch) to build sensor circuit

5. Bug strips for connections

· Controller Section

We try to implement this prototype using two methods using Arduino UNO board and another by making own breakout board for Atmega 328 but we are still using Arduino UNO to burn bootloader and uploading a code in Atmega 328.

so here we required

1. Arduino UNO

2. Atmega 328p-pu

3. 22p F Capacitors 2 unit Filter capacitor for crystal

4. 16 MHz Crystal Oscillator 1 unit Operating frequency for Atmega 328

5. 10K Ohms resistance 1 unit reset resistor

6. Reset button 1 unit to reset Atmega 328

7. Bug strips for connections

8. 7805 5V voltage regulator to get 5V regulated voltage from 9V battery

9. BC 547 npn Transistors 8 unit to control channels of Audio processor IC

10. 1K Ohms resistance 8 unit to connect port pin of Atmega 328 to base of transistor

· Audio Processing and LCD unit

1. APR 33A3 Audio processor store and playback sound 1unit

2. LCD 16X2 1unit to display message

3. Microphone 1unit to record audio message

4. Speaker 16 Ohms 1unit to play audio signal

5. 10K Ohms Potentiometer 1unit to control brightness of LCD

6. And all miscellaneous components to support APR 33A3

· 47K Ohms resistance

· 4.7K Ohms resistance

· 100K Ohms resistance

· 470 Ohms Resistance

· 1nF Capacitor

· 100nF Capacitor

· 100 micro F Capacitor Electrolytic

· 10 micro F Capacitor

· 1 micro F Capacitor

· Wires for connections

for miscellaneous component quantity please follow circuit diagram or data sheet of APR 33A3PCB WIZARD is simplest one software to design circuit, even beginner can use it directly because this software is very much user friendly ..... it has number of function which is reduced time consumption to design circuit like DRAG and Drop option ....

Once circuit design completed, we have attached the .pcb file a designed PCB

Take print out of the Art work of that circuit layout on Photo paper or glossy paper then trace the printed art work of circuit on copper clad board by ironing process,

During ironing process you must pay attention that all art work of circuit layout should traced completely on copper clad board , after tracing art work of circuit layout on copper clad completely, make solution of Fecl3 with water and keep it traced copper clad into that solution about 30 to 40 minutes ...... during this process you should continuously check the copper clad within some interval, copper of copper clad board should disappear except traced part of art work of circuit layout...... means only circuit should remain...

Once it complete take out board from solution then clean it and polish with sand paper for drilling , after drilling holes apply soldering flux and complete tinning process with the help of soldering iron after tinning start mounting component and soldering operation .........

Use images to follow all processes and position of each components.

Please follow the circuit diagram to make your own PCB.

If we are using Arduino UNO on the place of own made breakout board then only Atmega 328 controller section get neglected rest of connections are same and connect it on Arduino UNO.

Attachments
Guys here we learn to burn bootloader on blank ATmega 328/168/8 chips using Arduino IDE and Arduino UNO.

So, what we need

1 Step Connect Hardware

Breakout board for blank chip of ATmega 328/168/8

Here we can make connections on breadboard also as your choice I suggest make one special board so that no need to do same process again and again just save your time. Make connections same as shown in figure 1

Watch figure 2 This is my board which I used to burn bootloader.

Just be alert while buying your ATmega 328 Blank chip

ATMega328P-PU

ATMega328-PU

As you may have notice, the difference between this is just a mere P after the 328. This P means pico for pico power which is a technology ATMEL has developed that allows the microcontroller to run with less power.

That dosent matter for small application but guys while burning bootloader every chip has its unique key signature so need to edit that key signature before burning bootloader.

so what are those key signatures for this ICs

ATmega328 0x1E 0x95 0x14

ATmega328P 0x1E 0x95 0x0F

So we need to change those signatures before burning bootloader follow basic steps for that

· Navigate to ...\arduino-1.0.5\hardware\tools\avr\etc

· Make a backup copy of the file: avrdude.conf

· Open the file avrdude.conf in a text editor

· Search for: “0x1e 0x95 0x0F” (this is the ATmega328P signature)

· Replace it with: “0x1e 0x95 0x14” (this is the ATmega328 signature)

· Save the file

· Restart the Arduino IDE

· Continue with the rest of the steps of bootloding, and once bootloading is complete restore the backup copy you made.

Make Connections same as show in figure 3

Now we are complete with hardware setup

2 Step Preparing the software

Open Arduino IDE make sure that u have changed your signature as per targeted AVR ATmega

1. Open Arduino IDE

2. File > Examples > Arduino ISP

3. Select Arduino328 from Tools > Board

4. Select your serial port .

5. Burn in your Arduino board.

6. Select Arduino as ISP from Tools > Programmer

7. Select Burn Bootloader then install the code in arudio

8. Thats it you're gesture vocalizer for deaf people is ready you can use it 😇
