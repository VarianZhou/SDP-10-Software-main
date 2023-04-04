import serial;
import time;

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyAcM0',3600)
    ser.write('1')
    time.sleep(3)
    ser.write('2')
    time.sleep(3)
    ser.write('3')
    time.sleep(3)
    ser.write('4')
    time.sleep(3)
    ser.write('5')
    time.sleep(3)
    ser.write('6')