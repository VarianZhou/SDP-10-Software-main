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
import random
# import RPI.GPIO as GPIO

# define some constants, a list of numbers

# The success criteria of rotating a motor for 180 degrees
motor_100_criteria = Motor_Criteria((90,110))
motor_150_criteria = Motor_Criteria((140,160))
# The set of sensors that will be used for the Tshirt folding task
TSHIRT_SENSOR_SET = [1,2,3,5,4]
# The set of motors that will be used for the Tshirt folding task
TSHIRT_MOTOR_SET = [1,2,3,5,4]
# Angles we expect the motors to rotate
TSHIRT_ANGLE_SET = [100,100,100,100,150]
TSHIRT_CRITERIA_SET = [motor_100_criteria,motor_100_criteria,motor_100_criteria,motor_100_criteria,motor_150_criteria]
SLEEVE_SENSOR_SET = [1,2,3,2,3,5,4]
SLEEVE_MOTOR_SET = [1,2,3,2,3,5,4]
SLEEVE_ANGLE_SET = [100,100,100,100,100,100,150]
SLEEVE_CRITERIA_SET = [motor_100_criteria,motor_100_criteria,motor_100_criteria,motor_100_criteria,motor_100_criteria,motor_100_criteria,motor_150_criteria]
TROUSER_SENSOR_SET = [5,2,3,4]
TROUSER_MOTOR_SET = [5,2,3,4]
TROUSER_ANGLE_SET = [100,100,100,150]
TROUSER_CRITERIA_SET = [motor_100_criteria,motor_100_criteria,motor_100_criteria,motor_150_criteria]

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
        self.power_left = 100
        # For test purpose only
        self.counter = 0

    def __create_task(self, category : ClothingType) -> None:
        '''
        :param:
            category: Clothes enum value
        This method actuates the folding mechanism based on the item's clothing type.
        '''
        if category is ClothingType.TSHIRT:
            self.__createFoldingTshirtTask()
        elif category is ClothingType.LONG_SLEEVED_SHIRT:
            self.__createFoldingLongSLeeveShirtTask()
        elif category is ClothingType.TROUSERS:
            self.__createFoldingTrousersTask()
        elif category is ClothingType.OTHER:
            pass

    def __map_get(self, listOfObjects , indices):
        return list(map(lambda index: listOfObjects[index-1], indices))


    def __createFoldingTshirtTask(self) -> None:
        '''
        This function actuates panels to fold a T-Shirt
        '''
        sensors = self.__map_get(self.__motor_sensors, TSHIRT_SENSOR_SET)
        actuators = self.__map_get(self.__motors, TSHIRT_MOTOR_SET)
        parameters = TSHIRT_ANGLE_SET
        criteria = TSHIRT_CRITERIA_SET
        # criteria = [motor_180_criteria] * len(sensors)
        self.__currentTask = Task(sensors, actuators, parameters, criteria)
        # self.__monitor.add_task(task)

    def __createFoldingLongSLeeveShirtTask(self) -> None:
        '''
        This function actuates panels to fold a long sleeved shirt
        '''
        sensors = self.__map_get(self.__motor_sensors, SLEEVE_SENSOR_SET)
        actuators = self.__map_get(self.__motors, SLEEVE_MOTOR_SET)
        parameters = SLEEVE_ANGLE_SET
        criteria = SLEEVE_CRITERIA_SET
        # create a new task and assign it to the monitor
        self.__currentTask = Task(sensors, actuators, parameters, criteria)
        # self.__monitor.add_task(task)

    def __createFoldingTrousersTask(self) -> None:
        '''
        This function actuates panels to fold trousers
        '''

        sensors = self.__map_get(self.__motor_sensors, TROUSER_SENSOR_SET)
        actuators = self.__map_get(self.__motors, TROUSER_MOTOR_SET)
        parameters = TROUSER_ANGLE_SET
        criteria = TROUSER_CRITERIA_SET
        # create a new task and assign it to the monitor
        self.__currentTask = Task(sensors, actuators, parameters, criteria)

    def __receive_input(self) -> InputType:
        '''
        Detect the input from user
        '''
        # counter = self.counter
        # if counter in [1,100,200,357,351,151,161,858,2000,1515,151,616]:
        #     return InputType.START_RUNNING
        # if counter in [157,203,355]:
        #     return InputType.EMERGENCY_EXIT
        # if counter == 2500:
        #     return InputType.SHUT_DOWN
        typs = [0,1,2,3]
        probs = [.4,.0999,.001,.5]
        detected = random.choices(typs,probs,k=1)[0]
        if detected == 0:
            return InputType.START_RUNNING
        if detected == 1:
            return InputType.EMERGENCY_EXIT
        if detected == 2:
            return InputType.SHUT_DOWN
        if detected == 3:
            return InputType.NONE

    def restore(self):
        '''
        Restore the machine to its initial state
        '''
        for motor in self.__motors:
            motor.restore()

    def check_battery_condition(self):
        # TODO:implement the method to detect the power left in the battery
        if self.power_left > 20:
            pass
        else:
            self.__alert.alertUser(AlertType.LOW_BATTERY)


    # These methods are imported from the Monitor class in the monitor system directly
    '''Monitor the process of the task at the head of the queue'''

    def monitor_the_task(self):
        self.restore()
        # get the task in the queue
        task = self.__currentTask
        while True:
            # in case of hand detected
            if self.__camera_sensor.handDetected():
                # In case that hands are detected on the board, the machine should stop running
                print('Hand was detected on the board')
                continue
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
            print(criteria)
            state = task.report_state()
            # in case of success
            if self.check_criteria_meet(criteria, state):
                print('Step executed')
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
            if self.power_left == 0:
                print('runs out of power')
                break
            self.power_left -= .02
            input_type = self.__receive_input()
            if input_type is InputType.SHUT_DOWN:
                self.__alert.alertUser(AlertType.SHUT_DOWN)
                break
            if input_type is InputType.EMERGENCY_EXIT:
                self.__alert.alertUser(AlertType.EMERGENCY_EXIT)
                continue
            if input_type is InputType.START_RUNNING:
                if self.__camera_sensor.isItemOnBoard():
                    # Detect the type of clothing
                    category = self.__camera_sensor.getItemOnBoard()
                    print(category)
                    if category != ClothingType.OTHER:
                        print(f'Clothing type of {category} is detected! We are starting folding')
                        self.__create_task(category)
                        self.monitor_the_task()
                    else:
                        self.__alert.alertUser(AlertType.UNKNOWN_CLOTHING)
                else:
                    self.__alert.alertUser(AlertType.NO_CLOTHING)

    # implementation for the second design
    # def startLoop2(self):
    #     while True
    #         # First we check the battery condition
    #         self.check_battery_condition()
    #         if self.power_left == 0:
    #             print('runs out of power')
    #             break
    #         # We detect if there are inputs from the users, like shut down, start running, in this case, emergence exit
    #         # will not be processed.
    #         input_type = self.__receive_input()
