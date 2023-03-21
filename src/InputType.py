from enum import Enum

class InputType(Enum):
    '''
    Enum of different input types
    '''
    NONE = 0
    START_RUNNING = 1
    EMERGENCY_EXIT = 2
    SHUT_DOWN = 3