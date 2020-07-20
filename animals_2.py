# import the python datetime module to help us create a timestamp
from datetime import date

# 1


class Llama:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

# 2


class Donkey:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
# 3


class Goat:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
# 4


class Pony:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
# 5


class Turkey:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
# 6


class Copperhead:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 7


class Rat_Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 8


class Northern_Water_Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 9


class King_Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

# 10


class Timber_Rattlesnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 11


class Mallard:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

# 12


class Goldfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
# 13


class Yellow_Bellied_Slider:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
# 14


class Brook_Trout:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

# 15


class Bluegill:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


# 1
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning")
print("1.", miss_fuzz.name)
# 2
mr_long_ears = Donkey("Mr. Long Ears", "domestic donkey", "midday")
print("2.", mr_long_ears.name)
# 3
billy = Goat("Billy", "domestic goat", "afternoon")

print("3.", billy.name)
# 4
teddy = Pony("Teady", "domestic pony", "morning")

print("4.", teddy.name)
# 5
frank = Turkey("Frank", "domestic turkey", "midday")

print("5.", frank.name)
# 6
copper = Copperhead("Copper", "Copperhead Snake")

print("6.", copper.name)
# 7
bigBoi = Rat_Snake("Big Boy", "Rat Snake")

print("7.", bigBoi.name)
# 8
happy = Northern_Water_Snake("Happy", "Rat Snake")

print("8.", happy.name)
# 9
the_king = King_Snake("The King", "King Snake")

print("9.", the_king.name)
# 10
ole_shakey = Timber_Rattlesnake("Shakey Graves", "Timber Rattlesnake")

print("10.", ole_shakey.name)
# 11
donald = Mallard("Donald", "Mallard")

print("11.", donald.name)
# 12
goldie = Goldfish("Goldie", "Goldfish")

print("12.", goldie.name)
# 13
bruce = Yellow_Bellied_Slider("Bruce", "Yellow Bellied Slider")

print("13.", bruce.name)
# 14
grumpy = Brook_Trout("Grumpy", "Brook Trout")

print("14.", grumpy.name)
# 15
blue_boi = Bluegill("Blue Boy", "Bluegill")

print("15.", blue_boi.name)
