"""
Program: StackSensor Class
Author: Daniel Kim
Date: 7th February 2023
"""


class StackSensor:


    def __init__(self, sensor_ID):
        self.__sensor_ID = sensor_ID

    def getSensorID(self):
        return self.__sensor_ID

    def isStackFull(self):
        return False
    
