# UPDATE SOON when figure out how to set working dir of REPL instance
import os
PROJ_PATH = '/Users/johncaperton/Projects/sandbox/2_projects/surfingtutorial'
os.chdir(PROJ_PATH)

# players.py
from game_inventory import *
from func_tools import prompt_selection


class Player():
    ''' Creates a user player '''

    def __init__(self, user_name):
        self.user_name = user_name
        self.surfer = Hannah
        self.board = Toy

        self.plyr_speed = 5
        self.plyr_power = 5

        self.total_speed = self.plyr_speed + self.surfer.speed + self.board.speed
        self.total_power = self.plyr_power + self.surfer.power + self.board.power

    def update_stats(self):
        self.total_speed = self.plyr_speed + self.surfer.speed + self.board.speed
        self.total_power = self.plyr_power + self.surfer.power + self.board.power

    def __str__(self):
        return 'This is a player! str'

    def __repr__(self):
        return 'This is a player! repr'

    def change_player(self):
        surfer_select = prompt_selection('Select your surfer:', Surfer.item_list)

        if surfer_select is not None:
            self.surfer = surfer_select

            self.update_stats()
            print('Your current surfer is {}: \nSpeed: {} \nPower: {}'.format(self.surfer.name, self.total_speed, self.total_power))

        else:
            print('That didnt work')

# By using the super().__init__(self) I am grabbing attributes from parent since I overwrote init statement in subclass


class Trick(Surfer):

    def __init__(self, trick_name, score):
        self.trick_name = trick_name
        self.score = score

        super().experience += score


class Spray(Trick):

    def __init__(self):
        super().__init__(trick_name='Spray',
                         score=10)

    def perform():

        print('You did a spray!')
