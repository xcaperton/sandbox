# UPDATE SOON when figure out how to set working dir of REPL instance
import os
PROJ_PATH = '/Users/johncaperton/Projects/sandbox/2_projects/surfingtutorial'
os.chdir(PROJ_PATH)
from func_tools import prompt_selection

class Surfer():
    ''' All surfers have general class '''
    item_list = {}

    def __init__(self, name, gender, speed, power):

        self.name = name
        self.gender = gender
        self.speed = speed
        self.power = power

        # Keep dict of all surfers
        self.item_list[str(len(self.item_list))] = self

    def __repr__(self):
        return self.name

    def __str__(self):
        return 'SURFER \n====== \n{} \n{} \nSpeed: {} \nPower: {}'.format(self.name, self.gender, self.speed, self.power)

class Board():
    ''' All surfers have general class '''
    item_list = {}

    def __init__(self, name, speed, power):

        self.name = name
        self.speed = speed
        self.power = power

        # Keep dict of all surfers
        self.item_list[str(len(self.item_list))] = self

    def __repr__(self):
        return self.name

    def __str__(self):
        return 'BOARD \n====== \n{} \nSpeed: {} \nPower: {}'.format(self.name, self.speed, self.power)

