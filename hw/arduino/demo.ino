/**
 * Amanda Justiniano eCards Project
 * 
 * This program is for arduino nano board.
 * The functions of this program are tasked with listening
 * through i2c GPIOs for information in order to print information
 * to ePaper display connected to the Arduino Nano. 
 * 
 * References: https://oscarliang.com/raspberry-pi-arduino-connected-i2c/
 * 
 */

#include <Adafruit_GFX.h>    // Core graphics library
#include "Adafruit_EPD.h"
#include <Wire.h>

// Define Pins for the 2.13 Diagonal E-Ink Display Adafruit Industries
#define EPD_CS     10
#define EPD_DC      9
#define SRAM_CS     8
#define EPD_RESET   7 // can set to -1 and share with microcontroller Reset!
#define EPD_BUSY    6 // can set to -1 to not use a pin (will wait a fixed delay)

// Define colors
#define COLOR1 EPD_BLACK
#define COLOR2 EPD_RED

// Define address where Raspberry Pi can connect to
#define SLAVE_ADDRESS 0x04
char temp[50];
bool receiveFlag = false;
//int state = 0;

// Define the display that we are using. In this case: 2.13" tricolor EPD
Adafruit_IL0373 display(212, 104, EPD_DC, EPD_RESET, EPD_CS, SRAM_CS, EPD_BUSY);

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output

  // Init the display
  display.begin();
  
  // Initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  // Callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  
  Serial.println("Ready!");
}

void loop() {
  
  if (receiveFlag == true) {
    Serial.println(temp);
    receiveFlag = false;
  }
  delay(100);
}

// Callback for receiving data
void receiveData(int byteCount){
  for (int i = 0; i < byteCount; i++) {
    temp[i] = Wire.read();
    temp[i + 1] = '\0'; //add null after ea. char
  }

  //RPi first byte is cmd byte so shift everything to the left 1 pos so temp contains our string
  for (int i = 0; i < byteCount; ++i) {
    temp[i] = temp[i + 1];
  }

  // large block of text
  if (temp[0] == 'R') {
    display.clearBuffer();
    drawtext(temp, COLOR2);
    display.display();
  }else if (temp[0] == 'B') {
    display.clearBuffer();
    drawtext(temp, COLOR1);
    display.display();
  }

  receiveFlag = true;
}

// Callback for sending data
void sendData() {
  Wire.write(0);
}

// Draw text function
void drawtext(char *text, uint16_t color) {
  display.setCursor(0, 0);
  display.setTextColor(color);
  display.setTextWrap(true);
  display.print(text);
}
