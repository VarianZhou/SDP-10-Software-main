#include <Servo.h>

Servo south;
Servo east;
Servo west;
Servo north;
Servo centre;

void setup()
{
    Serial.begin(9600);//Set Baud Rate to 9600 bps
    south.attach(3);
    east.attach(5);
    west.attach(6);
    north.attach(9);
    centre.attach(10);

}

void actuate(Servo servo, double pos)
{
    servo.write(0);
    delay(750);
    servo.write(pos);
}

void shirt_short()
{
    actuate(south, 100);
    actuate(east, 100);
    actuate(west, 100);
    actuate(centre, 100);
    actuate(north, 150);
}

void shirt_long()
{
    actuate(south, 100);
    actuate(east, 100);
    actuate(west, 100);
    actuate(east, 100);
    actuate(west, 100);
    actuate(centre, 100);
    actuate(north, 150);
}

void trousers()
{
    actuate(centre, 100);
    actuate(east, 100);
    actuate(west, 100);
    actuate(north, 150);
}

float convert_float(char arr[],int start, int end){
//   = {'1', '2', '.', '3', '4', '5', '6', '7', '8', '9'};
//  int start = 2; // Index of the first character in the subarray
//  int end = 5;   // Index of the last character in the subarray
  int len = end - start + 1;

  char* subarr = &arr[start]; // Pointer to the first character in the subarray
  float value = std::strtof(subarr, &subarr[len]);

  return value;
  }

void loop() {
  if (Serial.available() > 0) {
    char usb[6];
    for (int i = 0; i < 6; i++) {
      usb[i] = Serial.read();
    }
    int id = usb[0];
    float angle = convert_float(usb, 2, 5);
    if (id == 1) {
      actuate(south, angle);
    }
    if (id == 2) {
      actuate(east, angle);
    }
    if (id == 3) {
      actuate(west, angle);
    }
    if (id == 4) {
      actuate(north, angle);
    }
    if (id == 5) {
      actuate(centre, angle);
    }
  }
}
