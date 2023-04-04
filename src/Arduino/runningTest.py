import serial;
import time;

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0',9600)
    ser.reset_input_buffer()
    ser.write('1'.encode())
    time.sleep(3)
    ser.write('2'.encode())
    time.sleep(3)
    ser.write('3'.encode())
    time.sleep(3)
    ser.write('4'.encode())
    time.sleep(3)
    ser.write('5'.encode())
    time.sleep(3)
    ser.write('6'.encode())