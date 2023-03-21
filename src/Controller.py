'''
Program: Controller class
Author: Daniel Kim, Hongliang Zhou
Date: 19th March 2023
Description: The Controller is responsible for controlling the overall process, assigning tasks, allocating resources etc.
According to our design, the user is expected to give more than one item of clothing on the board.
'''

from Alert import Alert
from ClothingType import ClothingType
from AlertType import AlertType
from StackSensor import StackSensor
from Camera import Camera
from InputType import InputType
from Actuator import Motor
from Sensor import Sensor, Motor_Sensor
from Task import Task
from Criteria import Criteria, Motor_Criteria
from queue import *
# import RPI.GPIO as GPIO

# define some constants, a list of numbers

# The success criteria of rotating a motor for 180 degrees
motor_180_criteria = Motor_Criteria((170,190))
# The set of sensors that will be used for the Tshirt folding task
TSHIRT_SENSOR_SET = [1,3,8,5]
# The set of motors that will be used for the Tshirt folding task
TSHIRT_MOTOR_SET = [1,3,8,5]
# Angles we expect the motors to rotate
TSHIRT_ANGLE_SET = [180,180,180,180]
SLEEVE_SENSOR_SET = [1,3,8,5]
SLEEVE_MOTOR_SET = [1,3,8,5]
SLEEVE_ANGLE_SET = [180,180,180,180]



class Controller:


    def __init__(self, output: Alert, stack_sensor: StackSensor, camera_sensor: Camera, motors: [Motor], motor_sensors : [Motor_Sensor]):
        '''
        Constructor for Controller class
        __board: Board object
        output: Alert object
        '''
        self.__alert = output
        self.__stack_sensor = stack_sensor
        self.__camera_sensor = camera_sensor
        self.__motors = motors
        self.__motor_sensors = motor_sensors
        self.__currentTask = None
        self.__tolerance = 3

    def __create_task(self, category) -> None:
        '''
        :param:
            category: Clothes enum value
        This method actuates the folding mechanism based on the item's clothing type.
        '''
        if category == ClothingType.TSHIRT:
            self.__createFoldingTshirtTask()
        elif category == ClothingType.LONG_SLEEVED_SHIRT:
            self.__createFoldingLongSLeeveShirtTask()
        elif category == ClothingType.TROUSERS:
            self.__createFoldingTrousersTask()
        elif category == ClothingType.OTHER:
            pass

    def __map_get(self, listOfObjects , indices):
        return list(map(lambda index: listOfObjects[index], indices))


    def __createFoldingTshirtTask(self) -> None:
        '''
        This function actuates panels to fold a T-Shirt
        '''
        sensors = self.__map_get(self.__motor_sensors, TSHIRT_SENSOR_SET)
        actuators = self.__map_get(self.__motors, TSHIRT_MOTOR_SET)
        parameters = TSHIRT_ANGLE_SET
        criteria = [motor_180_criteria] * len(sensors)
        self.__currentTask = Task(sensors, actuators, parameters, criteria)
        # self.__monitor.add_task(task)

    def __createFoldingLongSLeeveShirtTask(self) -> None:
        '''
        This function actuates panels to fold a long sleeved shirt
        '''
        sensors = self.__map_get(self.__motor_sensors, SLEEVE_SENSOR_SET)
        actuators = self.__map_get(self.__motors, SLEEVE_MOTOR_SET)
        parameters = SLEEVE_ANGLE_SET
        criteria = [motor_180_criteria] * len(sensors)
        # create a new task and assign it to the monitor
        self.__currentTask = Task(sensors, actuators, parameters, criteria)
        # self.__monitor.add_task(task)

    def __createFoldingTrousersTask(self) -> None:
        '''
        This function actuates panels to fold trousers
        '''
        self.__createFoldingTshirtTask()

    def __receive_input(self) -> InputType:
        '''
        Detect the input from user
        '''
        # TODO: functions to receive input from users
        return InputType.NONE

    def restore(self):
        '''
        Restore the machine to its initial state
        '''
        for motor in self.__motors:
            motor.restore()

    def check_battery_condition(self):
        # TODO:implement the method to detect the power left in the battery
        power_left = 80
        if power_left > 20:
            pass
        else:
            self.__alert.alertUser(AlertType.LOW_BATTERY)

    '''Add a task to the queue'''
    #
    # def create_Task(self, task: Task):
    #     self.__currentTask = task


    # These methods are imported from the Monitor class in the monitor system directly


    '''Monitor the process of the task at the head of the queue'''

    def monitor_the_task(self):
        self.restore()
        # get the task in the queue
        task = self.__currentTask
        while True:
            # in case of failure
            if not self.execute_next_process(task):
                self.__alert.alertUser(AlertType.TASK_FAILED)
                break
            # accrue the pointer of the task, if true, the task is done
            if task.accrue_pointer():
                self.__alert.alertUser(AlertType.LAUNDRY_DONE)
                break
        self.__currentTask = None
        # Restore all motors to initial states
        self.restore()


    def execute_next_process(self, task):
        # We give the machine a number of chances to operate a task
        for i in range(self.__tolerance):
            if self.__camera_sensor.handDetected():
                # In case that hands are detected on the board, the machine should stop running
                print('Hand detected on the board')
                return False
            input = self.__receive_input()
            if (input is InputType.EMERGENCY_EXIT):
                self.__alert.alertUser(AlertType.EMERGENCY_EXIT)
                return False
            if (input is InputType.SHUT_DOWN):
                self.__alert.alertUser(AlertType.SHUT_DOWN)
                self.restore()
                return False
            task.execute_next()
            criteria = task.send_criteria()
            state = task.report_state()
            # in case of success
            if self.check_criteria_meet(criteria, state):
                return True
        device = task.report_fault_device()
        device.print_instruction()
        # in case of fail for three times
        return False

    # check if the criteria is met by the feedback from a sensor
    def check_criteria_meet(self, criteria: Criteria, data):
        return criteria.success(data)


    def startLoop(self) -> None:
        '''
        This function starts the loop for the system 
        '''
        # As soon as the machine is start and ready to run, this function should be called
        while True:
            self.check_battery_condition()
            input_type = self.__receive_input()
            if input_type is InputType.SHUT_DOWN:
                self.__alert.alertUser(AlertType.SHUT_DOWN)
                break
            if input_type is InputType.EMERGENCY_EXIT:
                self.__alert.alertUser(AlertType.EMERGENCY_EXIT)
                break
            if input_type is InputType.START_RUNNING:
                if self.__camera_sensor.isItemOnBoard():
                    # Detect the type of clothing
                    category = self.__camera_sensor.getItemOnBoard()
                    if category != ClothingType.OTHER:
                        self.__create_task(category)
                        self.monitor_the_task()
                    else:
                        self.__alert.alertUser(AlertType.UNKNOWN_CLOTHING)
                else:
                    self.__alert.alertUser(AlertType.NO_CLOTHING)
