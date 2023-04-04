"""
Program: Actuator Class
Author: Hongliang Zhou
Date: 18th March 2023
"""
import time

import serial
class Actuator():
    '''
    The Actuator class is a real HW device that could perform a particular task, e.g. like motor rotating for a
    certain degree.
     '''

    def __init__(self,name:str, id:int):
        self.__name = name
        self.__id = id
        self.__state = None
        self.__initial_state = None

    def getId(self):
        return self.__id

    def currentState(self):
        return self.__state
    '''This method sends activation signal to the actuator to request proceeding, return True when the execution is done.'''
    def execute(self, *args):
        # To be implemented by the particular actuator type
        return True

class Motor(Actuator):
    def __init__(self,name:str, id:int, port = '/dev/ttyACM0', baud_rate = 9600):
        super().__init__(name,id)
        self.__state = 0
        self.__initial_state = 0
        self.ser = serial.Serial(port, baud_rate)
        self.ser.reset_input_buffer()


    def execute(self, angle):
        msg = self.getId()
        print(self.getId())
        if angle == 0:
            msg += 5
        if msg == 10:
            msg = 'a'
        else:
            msg = str(msg)[0]
        print(msg)
        self.ser.write(msg.encode())
        time.sleep(2)
        self.__state = angle
        return True

    def restore(self):
        '''
        Restore the motor to its initial state, the angle should be 0
        '''
        self.execute(0)
        return True
