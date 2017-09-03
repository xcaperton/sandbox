from func_tools import prompt_selection

# Generate all available surfers


class Surfer():

    surfer_list = []

    def __init__(self, name, gender, speed, power):

        self.name = name
        self.gender = gender
        self.speed = speed
        self.power = power
        self.surfer_list.append(surfer)

    def __repr__(self):
        return 'SURFER \n====== \n{} \n{} \nSpeed: {} \nPower: {}'.format(self.name, self.gender, self.speed, self.power)


for x in [1, 2, 3]:
''' this is going to print the list '''
    print(x)
a

Hannah = Surfer('Hannah', 'Female', 5, 5)
Xan = Surfer('Xan', 'Male', 9, 7)
Britt = Surfer('Britt', 'Male', 7, 10)

surfer_key_map = {'1': Hannah, '2': Xan}


class hello('this_stuff'

class Player():
    ''' Creates a user player '''

    def __init__(self, user_name):
        self.user_name=user_name
        self.surfer=Hannah

        self.plyr_speed=5
        self.plyr_power=5

        self.total_speed=self.plyr_speed + self.surfer.speed
        self.total_power=self.plyr_power + self.surfer.power

    def update_stats(self):
        self.total_speed=self.plyr_speed + self.surfer.speed
        self.total_power=self.plyr_power + self.surfer.power

    def __str__(self):
        return 'This is a player! str'

    def __repr__(self):
        return 'This is a player! repr'

    def change_player(self):
        surfer_select=prompt_selection('Select your surfer:', surfer_key_map)

        if surfer_select is not None:
            self.surfer=surfer_select

            self.update_stats()
            print('Your current surfer is {}: \nSpeed: {} \nPower: {}'.format(self.surfer.name, self.total_speed, self.total_power))

        else:
            print('That didnt work')

# By using the super().__init__(self) I am grabbing attributes from parent since I overwrote init statement in subclass


class Surfer(Player):

    def __init__(self, name, gender):
        self.name=name
        self.gender=gender

        super().__init__(self)
        # self.speed = self.plyr_speed + 5
        # self.power = self.plyr_power + 5

        self.tricks=[]
        self.experience=0

    def __str__(self):
        return 'This is the surfer!'

    def do_trick(self):
        Spray.perform()


class Trick(Surfer):

    def __init__(self, trick_name, score):
        self.trick_name=trick_name
        self.score=score

        super().experience += score


class Spray(Trick):

    def __init__(self):
        super().__init__(trick_name='Spray',
                         score=10)

    def perform():

        print('You did a spray!')
