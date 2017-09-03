# Testing classes


class Fish():

    def __init__(self,name,color):
        self.name = name
        self.color = color


class Goldfish(Fish):

    def __init(self,)





class Animal(object):
    '''A simple attempt at class'''

    def __init__(self, name, location, hp):
        '''initizate car attributes'''
        self.name = name
        self.location = location
        self.hp = hp

        # Fuel capacity and level in gallons
        self.magic_dust_capacity = 100
        self.magic_dust_level = 0

    def __str__(self):
        return '''this is it!!'''

    def fill_magic_dust(self):
        '''Fill magic dust to the top'''
        self.magic_dust_level = self.magic_dust_capacity
        print('This {} has been fully replenished to {} magic dust!'.format(self.style, self.magic_dust_capacity))


class Dolphin(Animal):
    '''Simple dolphins'''

    def __init__(self, nail_color, fin_color):
        self.nail_color = nail_color
        self.fin_color = fin_color

        super().__init__(name='Dolphin',
                         location='The Sea',
                         hp=100)

    def paint_nails(self):
        ui = input('What color do you want to paint the nails?')
        self.nail_color = ui
        print('The {} now has {} nails'.format(self.name, ui))

    def __str__(self):
        return '''this is it!!'''
