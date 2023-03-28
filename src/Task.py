
'''Each task should be done'''
''' 
    Note that the tasks are assumed to be done in a sequential manner, they will be done one by one. Our process is that
    after each execution is done, we check if its done successfully. If so, then next execution; otherwise raise an error.
    We give each execution three chances, if it could be finished in three times.
    '''
class Task():
    '''
    @sensors the list of sensors shall be called in sequence in the task, which is defined corresponding to the workflow
    @actuators the list of actuators shall be called in sequence in the task, which is defined corresponding to the workflow
    @parameters the parameters that shall be passed to each actuator.
    '''
    def __init__(self, sensors : list, actuators : list, parameters:list, criteria:list):
        self.sensors = sensors
        self.actuators = actuators
        self.criteria = criteria
        self.parameters = parameters
        self.num_of_sensors = len(sensors)
        # The pointer is used to record the stage of the task.
        self.pointer = 0

    # execute the next task
    def execute_next(self):
        actuator = self.actuators[self.pointer]
        args = self.parameters[self.pointer]
        # activate the actuator with the given args
        actuator.execute(args)

    # report the feedback from the sensor
    def report_state(self):
        sensor = self.sensors[self.pointer]
        return sensor.sense()

    # report the criteria used for the current process
    def send_criteria(self):
        return self.criteria[self.pointer]

    def accrue_pointer(self):
        if self.pointer == self.num_of_sensors-1:
            return True
        self.pointer+=1
        return False

    def report_fault_device(self):
        return self.sensors[self.pointer]
