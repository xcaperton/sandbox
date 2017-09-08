# =================================
#   CLASSES
# =================================


class Dog():
    """A simple representation of a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """simple sit methed"""
        print("{} is now sitting".format(self.name))

    def roll_over(self):
        """A dog rolling over"""
        print("{} rolled over!".format(self.name))


my_dog = Dog('Hoover', 8)


class Restaurant():
    """A restaurant string"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_resto(self):
        """Print it"""
        print("\n {} serves {} food.".format(self.name, self.cuisine_type))

    def open_resto(self):
        """Opens a resto"""
        print("{} is now open!".format(self.name))


chipotle = Restaurant('Chipotle', 'Mexicon')
donnies = Restaurant('McDonalds', 'Fast Food')
panera = Restaurant('Panera', 'Sandwiches')


class User():
    """A user class"""

    def __init__(self, username, email, first, last):
        self.username = username
        self.email = email
        self.first = first
        self.last = last

    def describe_user(self):
        """Print info"""
        print("{} \n===== \nEmail: {} \nFirst Name: {} \nLast Name: {}".format(
            self.username, self.email, self.first, self.last))

    def update_email(self, email):
        """Change the user email address"""
        self.email = email
        print("Email has been updated to: {}".format(self.email))


xan = User('xcaperton', 'capertja@gmail.com', 'Xan', 'Cape')


# =================================
#   WORKING WITH CLASSES AND INSTANCES
# =================================

class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_tank_max = 16  # In Gallons
        self.fuel_tank_current = 0

    def get_descriptive_name(self):
        """Return a descriptive format"""
        long_name = str("({}) {} {}".format(self.year, self.make, self.model))
        return long_name.title()

    def read_odometer(self):
        """Return the level on the O"""
        print("This car has {} miles on it.".format(self.odometer_reading))

    def update_odometer(self, mileage):
        """Update the number of miles on the car"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back dat meter son!")

    def increment_odometer(self, miles):
        """Increment that joint"""
        self.odometer_reading += miles

    def read_tank(self):
        """Return tank level"""
        print("Current Tank Level: {} ({}% full)".format(self.fuel_tank_current,
                                                         str(self.fuel_tank_current / self.fuel_tank_max)))

    def fill_tank(self, fuel=''):
        """Fill up the cars tanks"""

        if fuel:
            if fuel > (self.fuel_tank_max - self.fuel_tank_current):
                self.fuel_tank_current = self.fuel_tank_max
            else:
                self.fuel_tank_current += fuel
            print("You added {} gallons".format(fuel))
        else:
            self.fuel_tank_current = self.fuel_tank_max
            print("You filled the car to the top!")


my_new_car = Car('Audi', 'a4', 2016)
my_new_car.odometer_reading = 27  # Change the value directly through the instance
my_new_car.update_odometer(10)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


class ElectricCar(Car):
    """A type of car that is electric"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        super().__init__(make, model, year)
        self.weight = 2100
        self.battery = Battery(self.weight)

    def describte_battery(self):
        """DS it"""
        print("This car has a {}-kWh batter.".format(self.battery_size))

    def fill_tank(self):
        """Definition"""

    def read_tank(self):
        """Over ride since electric"""
        print("This is an electric car - it has no gas!")


class Battery():
    """A battery class"""

    def __init__(self, weight, battery_size=70):
        self.battery_size = battery_size
        self.weight = weight

    def describe_battery(self):
        """Describe it"""
        print("This car has a {}-kWh battery.".format(self.battery_size))


tesla = ElectricCar('Tesla', 'SuperX', 2017)

# =================================
#   USER CLASS TEST!!
# =================================


class User():
    """A user class"""

    def __init__(self, username, email, first, last):
        self.username = username
        self.email = email
        self.first = first
        self.last = last

    def describe_user(self):
        """Print info"""
        print("{} \n===== \nEmail: {} \nFirst Name: {} \nLast Name: {}".format(
            self.username, self.email, self.first, self.last))

    def update_email(self, email):
        """Change the user email address"""
        self.email = email
        print("Email has been updated to: {}".format(self.email))


class Admin(User):
    """This user has special priveles"""

    def __init__(self, username, email, first, last):
        self.username = username
        self.email = email
        self.first = first
        self.last = last
        self.priveleges = Priveleges()

        super().__init__(username, email, first, last)


class Priveleges():
    """A list of priveleges a user can have"""

    def __init__(self):
        pass

    def blog_post(self):
        """A blog post"""
        print("You can write a blog!")

    def check_users(self):
        """check the number of users"""
        print("You can check the number of users!")

    def print_email(self, User):
        print("The user's email is {}".format(User.email))


xan = User('xcaperton', 'capertja@gmail.com', 'Xan', 'Cape')
hannah = Admin('hwpace', 'hwpace@gmail.com', 'Hannah', 'Pace')

from random import randint


class Die():
    """A dice to roll"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """This will roll a die"""
        return randint(1, self.sides)
