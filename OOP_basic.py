# creating a `blueprint` of an object(parrot) using 'class'
class parrot:
    #class attribute
    species = 'bird'

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def sing(self, song):
        return "{} is singing a {}".format(self.name, song)
    @property
    def recite(self):
        return "{} is reciting a darood".format(self.name)

#instantiate the parrot class
blu = parrot("blue", 10)
print("class attribute is: {}".format(blu.__class__.species))  # accessing the class attribute using __class__
print("instance attribute: {}".format(blu.name))

#call our instance methods
print(blu.sing("naat"))
print(blu.recite)

###inheritance example

#base(parent) class
class bird:
    def __init__(self):
        print("bird is ready")

    def whoIsThis(self):
        print("bird")
    def swim(self):
        print("can swim faster")

#derived(child) class
class penguin(bird):
    def __int__(self):
        # super().__init__()
        print("penguin is ready")

    #changing behavior of parent class method i.e `whoisthis` method from `bird` class
    def whoisthis(self):
        print("penguin")

    def run(self):
        print("can run faster")

#instantite the penguin(derived/child class)
peggy = penguin()
peggy.whoisthis()#changing behavior of bird class
peggy.swim()#inherit the method from bird class
peggy.run()

### Encapsulation example


class Computer:
    def __init__(self):
        self._maxprice = 900

    def sell(self):
        print("The maximum price for sell is {}".format(self._maxprice))

    #setter method
    def setMaxPrice(self):
        self._maxprice = 1000


c = Computer()
c.sell()
c._maxprice = 1000#Changing maxprice, will not allow because maxprice is private i.e "_maxprice
c.sell()
c.setMaxPrice()#Using setter funtion to change maxprice, now it will allow
c.sell()


class A:
    def __init__(self):
        self.__var = 333

    def show(self):
        print("The value is" + " :", self.__var)


# x = A()
# x.show()
# x.__var = 444
# x.show()
# print(x.__dict__)
# print(x.__var)
a = A()
# print(a._A__var)#Allowing you to access the private variable, so not fully private
print(a.__var)#not allowing in normal way
a.show()
# a.__var = 555
# a.show()
# print("this val is {}".format(a.__var))
# print(a.__dict__)