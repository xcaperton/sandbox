
# Create a fish class and terry. You only have to pass the Trout class Terry because
# other objects are already initiliazed
class Fish():
    '''a fish class'''
    def __init__(self,first_name,last_name='Fish',skeleton='Bone',eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print('The fish is swimming')

    def swim_backwards(self):
        print('The fish is swimming backwards')

class Trout(Fish):
    
    def __init__(self, water = 'freshwater'):
        self.water = water
        super().__init__(self)

terry = Trout('Terry')
print(terry.first_name,terry.last_name)

class Clownfish(Fish):

    def live_with_anemone(self):
        print('The clownfish lives with anemone')

casey = Clownfish('Casey')

# Make shark method and override some variables

class Shark(Fish):

    def __init__(self,first_name,last_name='Shark',skeleton='Cartilage',eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print('the shark cannot swim backwards')


sammy = Shark('Sammy')
