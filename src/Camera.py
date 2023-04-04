"""
Program: Sensor Class
Author: Julia Turner, Hongliang Zhou
Date: 3rd February 2023
"""

from ClothingType import ClothingType
import random
class Camera:

    def __init__(self, sensor_ID):
        '''
        Constructor for the Sensor class which controls all the input for the machine.
        '''
        self.__sensor_ID = sensor_ID
        self.counter = 0

    def isItemOnBoard(self) -> bool:
        '''
            This function checks whether an item of clothing is on the board
            :return: bool value of whether clothing is on the board.
        '''
        #TODO: get in clothes sensing data
        # if (draft.return_clothe_type() == "Empty"):
        #     return False
        results = [True, False]
        probs = [.9, .1]
        detected = random.choices(results, probs, k=1)[0]
        return detected
        #TODO: have it return the category

    def getItemOnBoard(self) -> ClothingType:
        '''
            Identify the type of the item of clothing on the board
        '''
        # Cloth_Type = draft.return_clothe_type();
        # if Cloth_Type == 'Longsleeve' :
        #     return ClothingType.LONG_SLEEVED_SHIRT
        # if Cloth_Type == 'Pants' :
        #     return ClothingType.TROUSERS
        # if Cloth_Type == 'T-Shirt' :
        #     return ClothingType.TSHIRT
        # return ClothingType.OTHER
        '''
        For test purpose only, randomly select a type of clothing
        '''
        my_list = [0,1,2,3 ]
        probs = [.33,.33,.33,.01]
        result = random.choices(my_list, probs,k=1)[0]
        if result == 0:
            return ClothingType.TSHIRT
        if result == 1:
            return ClothingType.TROUSERS
        if result ==2:
            return ClothingType.LONG_SLEEVED_SHIRT
        if result == 3:
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
        # if ("clothes_sense" == True and all(p.getMotorId() in [1, 4, 3, 6] for p in panels)): # TODO
        #     return True
        # return False
        results = [True, False]
        probs = [.8, .2]
        detected = random.choices(results, probs, k=1)[0]
        return detected

    def handDetected(self):
        # return draft.is_hand_detected();
        results = [True,False]
        probs = [.1,.9]
        detected = random.choices(results, probs,k=1)[0]
        return detected
        # return False