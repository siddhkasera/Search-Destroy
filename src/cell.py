import random


class cell:
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
        self.target = not self.target

    def search_cell(self):
        choices = [True, False]
        result = random.choices(choices, weights=[1 - self.false_negative, self.false_negative], k=1)
        return result[0]

    def set_terrain(self, newTerrain='flat'):
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

