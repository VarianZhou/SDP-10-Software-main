
class Criteria():
    def __init__(self, range_ : tuple):
        self.range = range_

    # Determine if a given data meets the criteria. Note that the detailed implementation should depend on the sensor and
    # data types, so this function should be covered when necessary.
    def success(self, data):
        if (data > self.range[0] and data < self.range[1]):
            return True
        return False

class Motor_Criteria(Criteria):
    def success(self, data):
        if (data > self.range[0] and data < self.range[1]):
            return True
        return False