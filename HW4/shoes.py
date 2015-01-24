# Homework 4.4


class Pet():
    def __init__(self, color, species):
        self.color = color
        self.species = species


class Dog(Pet):
    def __init__(self, size, collarColor, species='Canine'):
        Pet.__init__(self)
        self.size = size
        self.collarColor = collarColor
        self.species = species


class Cat(Pet):
    def __init__(self, , size, fixed, species='Feline'):
        Pet.__init__(self)
        self.size = size
        self.fixed = fixed


class Bird(Pet):
    def __init__(self, birdType, cost, species='Bird'):
        Pet.__init__(self)
        self.birdType = birdType
        self.cost = cost



# Homework 4.6

class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num


class CampusAddress(Address):
    def __init__(self, office_number):
        Address.__init__(self, 'Massachusetts Ave', 77)
        self.office_number = office_number



