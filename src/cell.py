import random


class cell:
    """Cell object, which is the most basic unit in this project"""
    def __init__(self, terrain='flat'):
        self.terrain = terrain
        self.target = False

        if terrain == 'flat':
            self.false_negative = 0.1
        elif terrain == 'hilly':
            self.false_negative = 0.3
        elif terrain == 'forest':
            self.false_negative = 0.7
        elif terrain == 'cave':
            self.false_negative = 0.9
        else:  # default case
            self.false_negative = 0.1

    def set_target(self):
        """
        Inverts the value of self.target: if target was True, it turns to False, and vice versa
        :return:
        """
        self.target = not self.target

    def search_cell(self):
        """
        Searches the cell to determine if it contains the target. Return False if not found and True if found
        Take into account the false negative rate

        :return: boolean
        """
        if not self.target:
            return False

        choices = [True, False]
        result = random.choices(choices, weights=[1 - self.false_negative, self.false_negative], k=1)
        return result[0]

    def set_terrain(self, newTerrain='flat'):
        """
        Changes terrain of cell. Default is 'flat'

        :param: newTerrain
        :return
        """
        if newTerrain == 'flat':
            self.false_negative = 0.1
        elif newTerrain == 'hilly':
            self.false_negative = 0.3
        elif newTerrain == 'forest':
            self.false_negative = 0.7
        elif newTerrain == 'cave':
            self.false_negative = 0.9
        else:  # default case
            self.false_negative = 0.1

        self.terrain = newTerrain
