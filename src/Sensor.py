
from InputType import InputType
'''The sensor class provides an interface between the monitor system and HW, it is supposed to receive feedbacks from a
particular device(called sense), and send the feedback data to our monitor so that we can check if it is done successfully.'''
class Sensor():
    '''
    @name the name of the sensor
    @instruction_message : the instruction to be sent to the user in case of failure
    @value_type : the value type of the data
    @actuator : the corresponding actuator
    '''
    def __init__(self, name : str, instruction_message : str, value_type : type):
        self.name = name
        self.instruction_message = instruction_message
        self.value_type = value_type

    '''This method receives feedback from the actuator, the implementation details depend on the actual devices used.'''
    def sense(self):
        # TODO:add the sensing method
        return 1

    def print_instruction(self):
        print(f'here is the error message from {self.name}, and its instruction to fix it.')
        print(self.instruction_message)

class Motor_Sensor(Sensor):
    def sense(self):
        # Return the exact angle of a motor
        # for now, it just returns 180 for example, when the sensors are added, it should be able to detect the exact angle
        # of a motor
        return 180

class Input_Sensor(Sensor):
    def sense(self):
        # TODO: detect the type of operations from user
        return InputType.NONE