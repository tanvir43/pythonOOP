"""
Inheritance example(basic)
"""


class Bird:
    #  class attribute
    species = "bird"

    #  instantiator of instances defines instance attributes
    def __init__(self, no_of_leg, no_of_wings):
        self.legs = no_of_leg
        self.wings = no_of_wings

    #  class method
    @classmethod  # to make an instance method to class method
    def can_do(cls):
        print("Most of bird can fly")

    def whoIsThis(self):
        print("A bird")


class Parrot(Bird):
    def __init__(self, name, age, color):
        super().__init__("2", "2")
        self.name = name
        self.age = age
        self.color = color

    #  instance method
    def can_fly(self, running_type):
        print(self.name + " " + "can run" " " + running_type)

    def whoIsThis(self):
        print("a Parrot")


#  Intstantiating objects(specific instances)
Bird.can_do()  # accessing the class method without instantiating new instance of Bird class
brd = Bird("2","2")
print(brd.__class__.species)  # accessing the class attributes with __class__

parry = Parrot("perry", "2", "green")
print("Name of the bird is {}".format(parry.name))
print("{} has {} legs".format(parry.name, parry.legs))
print("{} has {} wings".format(parry.name, parry.wings))
parry.can_fly("Faster")
