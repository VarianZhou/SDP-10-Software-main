from sys import path
from os import getcwd
path.append(getcwd() + "/src")

from CameraSensor import Sensor
from Panel import Panel
from ClothingType import ClothingType

def runTests():
    initSensorTest()
    stackHeightReachedTest()
    isItemOnBoardTest()
    getItemOnBoardTest()

def initSensorTest():
    sensor = Sensor(1, 2)
    assert sensor.getDistanceSensorID() == 1
    assert sensor.getClothesSensorID() == 2

def stackHeightReachedTest():
    sensor = Sensor(1, 2)
    assert sensor.isStackHeightReached() == True

def isItemOnBoardTest():
    sensor = Sensor(1, 2)
    p1 = Panel(1, 0)
    p4 = Panel(4, 0)
    assert sensor.isItemCoveringSides([p1, p4]) == False

def getItemOnBoardTest():
    sensor = Sensor(1, 2)
    assert sensor.getItemOnBoard() == ClothingType.TSHIRT


if __name__ == "__main__":
    runTests()
