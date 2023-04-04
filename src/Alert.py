"""
Program: Alert Class
Author: Julia Turner
Date: 2nd February 2023
"""
from AlertType import AlertType
import serial

class Alert:

    __light_ID : int
    __beeper_ID : int

    def __init__(self, light_ID: int, beeper_ID: int):
        '''
        Controls the light and beeper features to alert the user of an issue. 
        '''
        self.__light_ID = light_ID
        self.__beeper_ID = beeper_ID
        # self.ser = serial.Serial(port='TODO', baudrate = 9600)

    def alertUser(self, alert_type: AlertType) -> None:
        '''
            Activates the lights and beeper to alert the user.
            :param: 
                alert_type: Enum value of AlertType objects
        '''
        if (alert_type is AlertType.STACKS_FULL):
            # self.ser.write('1')
            print("Stacks full, please remove")
        elif (alert_type is AlertType.LAUNDRY_DONE):
            # self.ser.write('2')
            print("Laundry Done!")
        elif (alert_type is AlertType.JAM): # Integrate with monitoring system
            # self.ser.write('3')
            print("Please remove the jammed clothes")
        elif(alert_type is AlertType.LOW_BATTERY): # Might not be possible with Raspberry Pi 3
            # self.ser.write('4')
            print("Please plug in machine.")
        elif(alert_type is AlertType.EMERGENCY_EXIT):
            # self.ser.write('5')
            print("User called EMERGENCY EXIT, the machine has stopped running.")
        elif(alert_type is AlertType.NO_CLOTHING):
            # self.ser.write('6')
            print("There is no clothes on the board, please put your item on the board!")
        elif (alert_type is AlertType.UNKNOWN_CLOTHING):
            # self.ser.write('7')
            print("The item of clothing on the board is unknown, please put a Tshirt, Long-sleeve shirt, or a pair of trousers!")
        elif (alert_type is AlertType.SHUT_DOWN):
            # self.ser.write('8')
            print('Machine is going to shut down, restoring to its initial state.')
        elif (alert_type is AlertType.TASK_FAILED):
            # self.ser.write('9')
            print("The task is failed!")
    def getLightID(self) -> int:
        return self.__light_ID

    def getBeeperID(self) -> int:
        return self.__beeper_ID

    
