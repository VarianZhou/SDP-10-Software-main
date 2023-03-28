"""
Program: Sensor Class
Author: Julia Turner, Hongliang Zhou
Date: 3rd February 2023
"""
import draft
from ClothingType import ClothingType

class Camera:

    def __init__(self, sensor_ID):
        '''
        Constructor for the Sensor class which controls all the input for the machine.
        '''
        self.__sensor_ID = sensor_ID

    def isItemOnBoard(self) -> bool:
        '''
            This function checks whether an item of clothing is on the board
            :return: bool value of whether clothing is on the board.
        '''
        #TODO: get in clothes sensing data
        if (draft.return_clothe_type() == "Empty"):
            return False
        return True
        #TODO: have it return the category

    def getItemOnBoard(self) -> ClothingType:
        '''
            Identify the type of the item of clothing on the board
        '''
        Cloth_Type = draft.return_clothe_type();
        if Cloth_Type == 'Longsleeve' :
            return ClothingType.LONG_SLEEVED_SHIRT
        if Cloth_Type == 'Pants' :
            return ClothingType.TROUSERS
        if Cloth_Type == 'T-Shirt' :
            return ClothingType.TSHIRT
        return ClothingType.OTHER

    def isItemCoveringSides(self) -> bool:
        '''
            This function checks if there is an item of clothing covering the sensors
            on either of the side panels, used in folding long sleeved shirts.
            :param:
                panels: List of Panel objects in the board
            :return: bool value of whether the one of the sides is covered.
        '''
        #TODO: get in clothes sensing data
        if ("clothes_sense" == True and all(p.getMotorId() in [1, 4, 3, 6] for p in panels)): # TODO
            return True
        return False

    def handDetected(self):
        return draft.is_hand_detected();