from sys import path
from os import getcwd
path.append(getcwd() + "/src")

from Panel import Panel
from Board import Board


def runTests():
    initialiseBoardTest()
    actuatePanelsTest()


def initialiseBoardTest():
    p1 = Panel(1, 0)
    p2 = Panel(2, 0)
    p3 = Panel(3, 0)
    p4 = Panel(4, 0)
    p5 = Panel(5, 0)
    p6 = Panel(6, 0)
    p7 = Panel(7, 0)
    p8 = Panel(8, 0)
    p9 = Panel(9, 0)
    board = Board([p1, p2, p3, p4, p5, p6, p7, p8, p9])
    assert [p.getMotorId() for p in board.getBoardPanels()] == [i for i in range(1, 10)]

def actuatePanelsTest():
    p1 = Panel(1, 0)
    p2 = Panel(2, 0)
    p3 = Panel(3, 0)
    p4 = Panel(4, 0)
    p5 = Panel(5, 0)
    p6 = Panel(6, 0)
    p7 = Panel(7, 0)
    p8 = Panel(8, 0)
    p9 = Panel(9, 0)
    board = Board([p1, p2, p3, p4, p5, p6, p7, p8, p9])
    board.actuatePanels([p7, p8, p9])
    board.actuatePanels([p1, p4])
    board.actuatePanels([p3, p6])
    board.actuatePanels([p5])
    board.actuatePanels([p2])



if __name__ == "__main__":
    runTests()