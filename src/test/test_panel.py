from sys import path
from os import getcwd
path.append(getcwd() + "/src")

from Panel import Panel

def runTests():
    initPanelTest()
    actuatePanelTest()

def initPanelTest():
    panel = Panel(1, 130)
    assert panel.getMotorId() == 1
    assert panel.getAngle() == 130

def actuatePanelTest():
    panel = Panel(1, 130)
    panel.actuate()

if __name__ == "__main__":
    runTests()