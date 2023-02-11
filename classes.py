# OPP - Object Orietned Programming
# classes use uppercases
class Dog:
    def __init__(self, dog_breed):         # initialisation, dunder (double underscore)
        self.animal_kind = "Canine"           # python sees what parameters have been passed in throughh the init method
        self.legs = 4
        self.breed = dog_breed
        self.hair_length = self.set_hair_length(hair_length)
        print(self.bark())                           # self.breed is a variable, #

    def set_hair_length(self, hair_length):     # python wants us to do a static method
        if hair_length in ("short", "medium", "long"): # can be done outside of the class
            return hair_length
        else:
            print("hair length must be short, medium or long")
            return "medium"

    def bark(self): # method
        return "WOOF!"
    def loud_bark(self):
        return self.bark().upper()

# self is very important in methods
# self exists soley in the a class, when you a defining
# can call functions already made in a class
#

fido = Dog("Dalmation")
lassie = Dog("Collie")
print(fido, type(fido))
print(fido.animal_kind)
print(fido.bark())


class Jaguar:
    def __init__(self, location, spots = None):
        self.animal_kind = "Feline"
        self.tail = 1
        self.location = location
        self.spots = spots

    def growl(self):
        return "GROWL"


    def loud_growl(self):
        return self.growl().upper()


# instantiation i.e a module can be assigned ot multiple variables

fido = Dog("potato")
lassie = Dog("long")
fido.animal_kind = "giraffe"
print(fido.animal_kind)
Dog.animal_kind = "arachnid"
print(fido.animal_kind)
print(lassie.animal_kind)
## we make a cookie cutter, we then

# my own class

panther_onca = Jaguar("South America")
print(panther_onca.location)
