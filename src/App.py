'''
Program: App class
Author: Daniel Kim
Date: 3rd February 2023
'''
from Alert import Alert
from Camera import Camera
from Controller import Controller
from StackSensor import StackSensor
from Sensor import Motor_Sensor
from Actuator import Motor
import time


def main():
    '''
    This function is the main function to start the system
    '''
    
    start_time = time.time()
    # camera_sensor = CameraSensor(8)
    # controller = Controller(output, stack_sensor, camera_sensor, panels)
    # controller.startLoop()
    output = Alert(1, 2)
    stack_sensor = StackSensor(3)
    camera = Camera(4)
    msg1 = '''1. Please remove the tap of the machine using a screw driver,
                  2. Please remove the motor at left top,
                  3. Please replace it with a new motor,
                  4. Put the tap back,
                  5. Try to restart the machine.'''
    msg2 = '''1. Please remove the tap of the machine using a screw driver,
                  2. Please remove the motor at middle top,
                  3. Please replace it with a new motor,
                  4. Put the tap back,
                  5. Try to restart the machine.'''
    msg3 = '''1. Please remove the tap of the machine using a screw driver,
                          2. Please remove the motor at right top,
                          3. Please replace it with a new motor,
                          4. Put the tap back,
                          5. Try to restart the machine.'''
    msg4 = '''1. Please remove the tap of the machine using a screw driver,
                          2. Please remove the motor at middle left,
                          3. Please replace it with a new motor,
                          4. Put the tap back,
                          5. Try to restart the machine.'''
    msg5 = '''1. Please remove the tap of the machine using a screw driver,
                          2. Please remove the motor at center,
                          3. Please replace it with a new motor,
                          4. Put the tap back,
                          5. Try to restart the machine.'''
    motor_sensor1 = Motor_Sensor('Motor Sensor 1', msg1, int)
    motor_sensor2 = Motor_Sensor('Motor Sensor 2', msg2, int)
    motor_sensor3 = Motor_Sensor('Motor Sensor 3', msg3, int)
    motor_sensor4 = Motor_Sensor('Motor Sensor 4', msg4, int)
    motor_sensor5 = Motor_Sensor('Motor Sensor 5', msg5, int)

    south_actuator = Motor('South Actuator',1)
    east_actuator = Motor('East Actuator',2)
    west_actuator = Motor('West Actuator',3)
    north_actuator = Motor('North Actuator',4)
    center_actuator = Motor('Center Actuator',5)

    # We define the sensor and task lists
    sensors = [motor_sensor1, motor_sensor2, motor_sensor3, motor_sensor4, motor_sensor5]
    actuators = [south_actuator, east_actuator, west_actuator, north_actuator, center_actuator]
    # parameters1 = [180, 180,180,180,180,180,180,180,180]

    controller = Controller(output, stack_sensor, camera, actuators, sensors)
    controller.startLoop()
    end_time = time.time()
    print(f'The total running time is "{end_time-start_time}"')
    #

# Your program code here
main()

# class App:
#     def main():
#         '''
#         This function is the main function to start the system
#         '''
#
#         # camera_sensor = CameraSensor(8)
#         # controller = Controller(output, stack_sensor, camera_sensor, panels)
#         # controller.startLoop()
#         output = Alert(1, 2)
#         stack_sensor = StackSensor(3)
#         camera = Camera(4)
#         msg1 = '''1. Please remove the tap of the machine using a screw driver,
#                       2. Please remove the motor at left top,
#                       3. Please replace it with a new motor,
#                       4. Put the tap back,
#                       5. Try to restart the machine.'''
#         msg2 = '''1. Please remove the tap of the machine using a screw driver,
#                       2. Please remove the motor at middle top,
#                       3. Please replace it with a new motor,
#                       4. Put the tap back,
#                       5. Try to restart the machine.'''
#         msg3 = '''1. Please remove the tap of the machine using a screw driver,
#                               2. Please remove the motor at right top,
#                               3. Please replace it with a new motor,
#                               4. Put the tap back,
#                               5. Try to restart the machine.'''
#         msg4 = '''1. Please remove the tap of the machine using a screw driver,
#                               2. Please remove the motor at middle left,
#                               3. Please replace it with a new motor,
#                               4. Put the tap back,
#                               5. Try to restart the machine.'''
#         msg5 = '''1. Please remove the tap of the machine using a screw driver,
#                               2. Please remove the motor at center,
#                               3. Please replace it with a new motor,
#                               4. Put the tap back,
#                               5. Try to restart the machine.'''
#         msg6 = '''1. Please remove the tap of the machine using a screw driver,
#                               2. Please remove the motor at middle right,
#                               3. Please replace it with a new motor,
#                               4. Put the tap back,
#                               5. Try to restart the machine.'''
#         msg7 = '''1. Please remove the tap of the machine using a screw driver,
#                               2. Please remove the motor at left bottom,
#                               3. Please replace it with a new motor,
#                               4. Put the tap back,
#                               5. Try to restart the machine.'''
#         msg8 = '''1. Please remove the tap of the machine using a screw driver,
#                               2. Please remove the motor at middle bottom,
#                               3. Please replace it with a new motor,
#                               4. Put the tap back,
#                               5. Try to restart the machine.'''
#         msg9 = '''1. Please remove the tap of the machine using a screw driver,
#                               2. Please remove the motor at right bottom,
#                               3. Please replace it with a new motor,
#                               4. Put the tap back,
#                               5. Try to restart the machine.'''
#         motor_sensor1 = Motor_Sensor('Motor Sensor 1', msg1, int)
#         motor_sensor2 = Motor_Sensor('Motor Sensor 2', msg2, int)
#         motor_sensor3 = Motor_Sensor('Motor Sensor 3', msg3, int)
#         motor_sensor4 = Motor_Sensor('Motor Sensor 4', msg4, int)
#         motor_sensor5 = Motor_Sensor('Motor Sensor 5', msg5, int)
#         motor_sensor6 = Motor_Sensor('Motor Sensor 6', msg6, int)
#         motor_sensor7 = Motor_Sensor('Motor Sensor 7', msg7, int)
#         motor_sensor8 = Motor_Sensor('Motor Sensor 8', msg8, int)
#         motor_sensor9 = Motor_Sensor('Motor Sensor 9', msg9, int)
#
#         motor_actuator1 = Motor('Motor Actuator 1')
#         motor_actuator2 = Motor('Motor Actuator 2')
#         motor_actuator3 = Motor('Motor Actuator 2')
#         motor_actuator4 = Motor('Motor Actuator 2')
#         motor_actuator5 = Motor('Motor Actuator 2')
#         motor_actuator6 = Motor('Motor Actuator 2')
#         motor_actuator7 = Motor('Motor Actuator 2')
#         motor_actuator8 = Motor('Motor Actuator 2')
#         motor_actuator9 = Motor('Motor Actuator 2')
#
#
#         # We define the sensor and task lists
#         sensors = [motor_sensor1, motor_sensor2,motor_sensor3,motor_sensor4,motor_sensor5,motor_sensor6,motor_sensor7,motor_sensor8, motor_sensor9]
#         actuators = [motor_actuator1, motor_actuator2,motor_actuator3, motor_actuator4,motor_actuator5, motor_actuator6,motor_actuator7, motor_actuator8,motor_actuator9]
#         # parameters1 = [180, 180,180,180,180,180,180,180,180]
#
#         controller = Controller(output, stack_sensor, camera, actuators, sensors)
#         controller.startLoop()
#
#
#     if __name__ == "__main__":
#         main()
#
