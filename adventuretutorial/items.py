class Item():
    """The base class for all items"""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return '{}\n====\n{}\nValue: {}\n'.format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name='Gold',
                         description='A round coin with {} stamp on the front'.format(str(self.value)),
                         value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage

    def __str__(self):
        return '{}\n====\n{}\nValue: {}\nDamage: {}'.format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name='Rock',
                         description='A fist-sized rock, suitable for stuff',
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name='Dagger',
                         description='A small knife',
                         value=10,
                         damage=10)
