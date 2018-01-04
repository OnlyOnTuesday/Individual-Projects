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
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#allows us to find name of calling function
getframe_expr = "sys._getframe({}).f_code.co_name"

def use_numbers():
    #choose 1 or 2; this will determine if the numbers replace letters or are interspersed
    num = randint(1, 2)
    if num == 1:
        #interspersed
        return 1
    else:
        #replace letters
        return 2
            

def interspersed(passwd):
    #will numbers appear at beginning/end or inbetween words, or will they replace letters
    num = randint(1,2)
    if num == 1:
        #inbetween words
        num2 = randint(1, 5)
        passwd = passwd.split()
        for i in range(1, num2):
            if any (char in "ABCDEFGHIJKLMNOPQRSTUVWXYV1234567890" for char in passwd):
                passwd.insert(char, str(randint(1,10)))
        debug = "DEBUG"
        passwd = "".join(passwd)
        return passwd
    elif num == 2:
        #before or after the password
        num2 = randint(1,2)
        if num2 == 1:
            #before word
            passwd = passwd.split()
            num3 = randint(1,5)
            for i in range(1, num3):
                passwd.insert(0, str(randint(1,10)))
            passwd = "".join(passwd)
            return passwd
        elif num2 == 2:
            #after word
            passwd = passwd.split()
            length = len(passwd)
            num3 = randint(1,5)
            for i in range(1, num3):
                passwd.insert(length, str(randint(1,10)))
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
    passwd = "".join(passwd)
    return passwd
            
def get_passwd(color, animal, end):
    #numbers = use_numbers(terminal_args)
    color_choice = choice(color)
    animal_choice = choice(animal)
    end_choice = choice(end)
    passwd = color_choice + animal_choice + end_choice
    #print(color_choice + animal_choice + end_choice)
    if "-n" in terminal_args:
        numbers = use_numbers()
        if numbers == 1:
            new_passwd = interspersed(passwd)
            print(new_passwd)
        elif numbers == 2:
            new_passwd = replace_letters(passwd)
            print(new_passwd)
    else:
        print(passwd)


def start():
    for i in range(1, 10):
        get_passwd(colors, animals, ends)
        print()

start()
