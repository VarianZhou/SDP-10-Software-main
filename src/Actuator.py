"""
Program: Actuator Class
Author: Hongliang Zhou
Date: 18th March 2023
"""

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
    def __init__(self,name:str, id:int):
        super().__init__(name,id)
        self.__state = 0
        self.__initial_state = 0


    def execute(self, angle):
        # TODO: Using the code from HW team to rotate the motor for a certain degree.
        # The state is updated
        self.__state += angle
        return True

    def restore(self):
        '''
        Restore the motor to its initial state, the angle should be 0
        '''
        self.execute(-self.__state)
        self.__state = self.__initial_state
        return True
