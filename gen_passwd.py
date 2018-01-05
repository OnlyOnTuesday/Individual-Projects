#A password generator written in Python

#V0.0 relies on long sentences rather than special characters and numbers

## BUGS
## In the interspersed function, the instructions to insert numbers inbetween words does not work
## This needs to be fixed
##
## Not a bug, but support for special characters still needs to be built in

###################################
#####Written by Michael Cooney#####
############Jan 3 2018#############
###################################


from random import choice, randint
import sys

DEBUG = False

terminal_args = list(sys.argv)

# Colors will be oraganized in the following order:
# the primaries, their basic mixtures along with white, black, grey, and brown.
# Then various shades of blue, red, yellow, white, black, grey, and brown in that order.
# Other colors will be put where it is thought they fit best (i.e. a shade of purple would
# be put with blue or red)
colors = ["blue", "red", "yellow", "purple", "orange", "green", "white", "black", "grey", "brown", \
          "azure", "cerulean", "cobalt", "cyan", "indigo", "crimson", "raspberry", "rose", "maroon", \
          "rustRed", "ruby", "scarlet", "amber", "golden", "marigold", "goldenrod", "beige", \
          "honeydew", "ivory", "pearl", "snowWhite", "vanilla", "ebony", "jetBlack", "onyx", \
          "platinum", "silver", "charcoal", "burgandy", "chocolate", "coffeeBrown", "khaki", \
          "mahogany"]

# List of animals, picked randomly from wikipedia, aplhabetical order begins after GuineaPigs.
animals = ["Cats", "Kittens", "Tigers", "Lions", "Dogs", "Wolves", "Puppies", "Horses", "Rats", \
           "Mice", "Chickens", "Chicks", "Pigs", "Sheep", "GuineaPigs", "Aardvarks", "Alpacas", \
           "Baboons", "Bears", "Bees", "Snakes", "Birds", "Dolphin", "Deer", "Eagles", "Eels", \
           "Emu", "Ferrets", "Flamingo", "Frogs", "Hamsters", "Hawks", "Jellyfish", "Kangaroo", \
           "Lizards", "Lemurs", "MountainGoats", "Pigeons", "Pumas", "Quail", "Unicorns", "Yaks",]

# These make up the last part of the sentence (for now).
ends = ["AreAttractive", "AreBald", "LikeCleanliness", "AreDazzling", "AreDrab", "AreElegant", \
              "AreMuscular", "ArePlump", "AreUgly", "AreQuaint", "AreUnsightly", "PlanWell", \
              "OraganizeQuickly", "BuildRobots", "OperateRobots", "SynthesizeEmotions", \
              "CoachBaseball", "PilotJets", "AdviseLeaders", "MentorActors", "EmployDirtyTricks", \
              "PopulateQuickly", "ElectDictators", "ConfrontDeath", "TriangulateCircles"]

# Add special character support.
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", " ", "+", "=", "-", "_", ",", ".", "~", \
                 "{", "}", "[", "]", "(", ")"]

# add number support.  This will either add a series of numbers to the beginning or end of password,
# or it will replace certain characters with numbers (such as "o" with "0").  The choice will be
# made by the program based on a random outcome.
caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", \
        "S", "T", "U", "V", "W", "X", "Y", "Z"]

#allows us to find name of calling function
getframe_expr = "sys._getframe({}).f_code.co_name"

def use_numbers():
    #choose 1 or 2; this will determine if the numbers replace letters or are interspersed
    if DEBUG == True:
        num = 1
    else:
        num = randint(1, 2)
    if num == 1:
        #interspersed
        return 1
    else:
        #replace letters
        return 2

def interspersed(passwd):
    if DEBUG == True:
        num = 2
    else:
        num = randint(1, 2)
    if num == 1:
        passwd = inbetween(passwd)
        return passwd
    else:
        if DEBUG == True:
            num2 = 1
        else:
            num2 = randint(1,2)
        if num2 == 1:
            passwd = before(passwd)
            return passwd
        else:
            passwd = after(passwd)
            return passwd

def inbetween(passwd):
    num = randint(2, 5)
    passwd = passwd.split()
    for i in range(1, num):
        passwd.insert(randint(1, len(passwd)-1), str(randint(1, 9)))
    passwd = "".join(passwd)
    return passwd

def before(passwd):
    passwd = passwd.split()
    num = randint(2, 5)
    for i in range(1, num):
        passwd.insert(0, str(randint(1, 9)))
    passwd = "".join(passwd)
    return passwd

def after(passwd):
    passwd = passwd.split()
    num = randint(2, 5)
    for i in range(1, num):
        passwd.insert(len(passwd), str(randint(1, 9)))
    passwd = "".join(passwd)
    return passwd

def replace_letters(passwd):
    #replace letters inside of words.
    #requires certain letters to be paired with certain numbers
    passwd = list(passwd)
    for char in passwd:
        if char == "o" or char == "O":
            passwd[passwd.index(char)] = "0"
        elif char == "i" or char == "I":
            passwd[passwd.index(char)] = "1"
    #will first include spaces, so we have to split it and rejoin it again
    passwd = "".join(passwd)
    passwd = passwd.split()
    passwd = "".join(passwd)
    return passwd
            
def get_passwd(color, animal, end):
    #numbers = use_numbers(terminal_args)
    color_choice = choice(color)
    animal_choice = choice(animal)
    end_choice = choice(end)
    #spaces added in case the program desires to add numbers inbetween the words
    passwd = color_choice + " " + animal_choice + " " + end_choice
    if "-n" in terminal_args:
        numbers = use_numbers()
        if numbers == 1:
            new_passwd = interspersed(passwd)
            print(new_passwd)
        elif numbers == 2:
            new_passwd = replace_letters(passwd)
            print(new_passwd)
    else:
        #removes the spaces from the password
        passwd = passwd.split()
        passwd = "".join(passwd)
        print(passwd)


def start():
    for i in range(1, 10):
        get_passwd(colors, animals, ends)
        print()

start()
