from enum import Enum

class AlertType(Enum):
    '''
    Enum of different alert types
    '''
    LAUNDRY_DONE = 0 # Maybe when no input is detected for 5 minutes (?)
    STACKS_FULL = 1
    JAM = 2
    LOW_BATTERY = 3
    EMERGENCY_EXIT = 4
    NO_CLOTHING = 5
    UNKNOWN_CLOTHING = 6
    SHUT_DOWN = 7
    TASK_FAILED = 8