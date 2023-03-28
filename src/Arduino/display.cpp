//LCD1602
//You should now see your LCD1602 display the flowing characters "SUNFOUNDER" and "hello, world"
//Email:info@primerobotics.in
//Website:www.primerobotics.in
//2015.5.7
#include <LiquidCrystal.h>// include the library code
#include "rgb_lcd.h"

/**********************************************************/
char array1[]="Laundry Done              ";  //the string to print on the LCD
char array2[]="Stacks Full               ";//the string to print on the LCD
char array3[]="Jam                       ";
char array4[]="Low Battery               ";
char array5[]="Emergency Exit            ";
char array6[]="No Clothing               ";
char array7[]="Unknown Clothing          ";
char array8[]="Shut Down                 ";
char array9[]="Task Failed               ";

int tim = 500;  //the value of delay time
// initialize the library with the numbers of the interface pins
//LiquidCrystal lcd(4, 6, 10, 11, 12, 13);
/*********************************************************/
//include the rgb_lcd library

//assign name lcd to rgb_lcd
rgb_lcd lcd;

void setup()
{
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    // Print Hello, World! to the LCD.
    lcd.print("Hello, World!");
    delay(1000);
}
/*********************************************************/
void loop()
{
    lcd.setCursor(16, 2);
//    lcd.setCursor(15,0);  // set the cursor to column 15, line 0
    char usb = Serial.read();
    if (usb == '1'){
        message = array1
    }
    if (usb == '2'){
        message = array2
    }
    if (usb == '3'){
        message = array3
    }
    if (usb == '4'){
        message = array4
    }
    if (usb == '5'){
        message = array5
    }
    if (usb == '6'){
        message = array6
    }
    if (usb == '7'){
        message = array7
    }
    if (usb == '8'){
        message = array8
    }
    if (usb == '9'){
        message = array9
    }

    if (Serial.available() > 0) {
        for ( int positionCounter = 0; positionCounter < 26; positionCounter++)
        {
          lcd.scrollDisplayLeft();  //Scrolls the contents of the display one space to the left.
          lcd.print(message[positionCounter]);  // Print a message to the LCD.
          delay(tim);  //wait for 250 ms
        }
//        lcd.clear();  //Clears the LCD screen and positions the cursor in the upper-left corner.
//        lcd.setCursor(15,1);  // set the cursor to column 15, line 1
//        for (int positionCounter2 = 0; positionCounter2 < 26; positionCounter2++)
//        {
//          lcd.scrollDisplayLeft();  //Scrolls the contents of the display one space to the left.
//          lcd.print(array2[positionCounter2]);  // Print a message to the LCD.
//          delay(tim);  //wait for 250 ms
//        }
//        lcd.clear();  //Clears the LCD screen and positions the cursor in the upper-left corner.
    }
}
/************************************************************/