#A password generator written in Python


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


##############################################################################
#This section provides the ability to create passwords with special characters
##############################################################################

def use_special_chars():
    #choose 1 or 2; this will determine if the chars come before, after, or occur inbetween words
    if DEBUG == True:
        num = 1
    else:
        num = randint(1,2)
    if num == 1:
        #inbetween letters
        return 1
    else:
        #before or after words
        if DEBUG == True:
            num2 = 1
        else:
            num2 = randint(1,2)
        if num2 == 1:
            #before
            return 2
        else:
            #after
            return 3

def chars_inbetween(passwd):
    #the randomly generated nums do not include 1 because the range function will not do anything if
    #there is no increment
    num = randint(2, 5)
    passwd = passwd.split()
    for i in range(1, num):
        passwd.insert(randint(1, len(passwd)-1), choice(special_chars))
    passwd = "".join(passwd)
    return passwd    

def chars_before(passwd):
    #see chars_inbetween() for why randint does not start at 1
    num = randint(2, 5)
    passwd = passwd.split()
    for i in range(1, num):
        passwd.insert(0, choice(special_chars))
    passwd = "".join(passwd)
    return passwd

def chars_after(passwd):
    #see chars_inbetween() for why randint does not start at 1
    num = randint(2, 5)
    passwd = passwd.split()
    for i in range(1, num):
        passwd.insert(len(passwd), choice(special_chars))
    passwd = "".join(passwd)
    return passwd

###################################################################
#This section provides the ability to create passwords with numbers
###################################################################
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
        passwd = numbers_inbetween(passwd)
        return passwd
    else:
        if DEBUG == True:
            num2 = 1
        else:
            num2 = randint(1,2)
        if num2 == 1:
            passwd = numbers_before(passwd)
            return passwd
        else:
            passwd = numbers_after(passwd)
            return passwd

def numbers_inbetween(passwd):
    #the randomly generated nums do not include 1 because the range function will not do anything if
    #there is no increment
    num = randint(2, 5)
    passwd = passwd.split()
    for i in range(1, num):
        passwd.insert(randint(1, len(passwd)-1), str(randint(1, 9)))
    passwd = "".join(passwd)
    return passwd

def numbers_before(passwd):
    #see numbers_inbetween() for why randint does not start at 1
    num = randint(2, 5)
    passwd = passwd.split()
    for i in range(1, num):
        passwd.insert(0, str(randint(1, 9)))
    passwd = "".join(passwd)
    return passwd

def numbers_after(passwd):
    #see numbers_inbetween() for why randint does not start at 1
    num = randint(2, 5)
    passwd = passwd.split()
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

############################################
#This section will provide the "walkthrough"
############################################
def walkthrough():
    print("What type of password would you like?")
    print("Enter the number of the option you would like to select.")
    print("    1.) Text only")
    print("    2.) Text and numbers")
    print("    3.) Text and special characters")
    print()
    answer = input()
    for i in range(1, 10):
        passwd = make_passwd()
        get_passwd_walkthrough(passwd, answer)
        print()

def get_passwd_walkthrough(passwd, answer):
    #same as get_passwd(); used to prevent the menu dialogue from appearing each time the program loops
    if answer == "1":
        passwd = passwd.split()
        passwd = "".join(passwd)
        print(passwd)
    elif answer == "2":
        numbers = use_numbers()
        if numbers == 1:
            new_passwd = interspersed(passwd)
            print(new_passwd)
        elif numbers == 2:
            new_passwd = replace_letters(passwd)
            print(new_passwd)
    elif answer == "3":
        use_chars = use_special_chars()
        if use_chars == 1:
            new_passwd = chars_inbetween(passwd)
            print(new_passwd)
        elif use_chars == 2:
            new_passwd = chars_before(passwd)
            print(new_passwd)
        else:
            new_passwd = chars_after(passwd)
            print(new_passwd)
    else:
        print("That option is not recognizable.  Please make sure you only typed in the number and try again.")



##############################################################
#This section will provide the list of available shell options
##############################################################
def help():
    print("Shell Options:")
    print("    Default: No arguments: ------------> The program will display a user-friendly menu to choose from")
    print("    -d --------------------------------> The program will print text-only passwords")
    print("    -n --------------------------------> The program will combine text and numbers")
    print("    -s --------------------------------> The program will combine text and special characters")
    print("    -h --------------------------------> The program will display this help text")
    print()


########################################################################
#This section provides the basic functionality of the password generator
#It also initiates the creation of passwords containing numbers and
#special characters
########################################################################
def get_passwd_nums(passwd):
    numbers = use_numbers()
    if numbers == 1:
        new_passwd = interspersed(passwd)
        print(new_passwd)
    elif numbers == 2:
        new_passwd = replace_letters(passwd)
        print(new_passwd)

def get_passwd_chars(passwd):
    use_chars = use_special_chars()
    if use_chars == 1:
        new_passwd = chars_inbetween(passwd)
        print(new_passwd)
    elif use_chars == 2:
        new_passwd = chars_before(passwd)
        print(new_passwd)
    else:
        new_passwd = chars_after(passwd)
        print(new_passwd)

def get_passwd_default(passwd):
    #removes the spaces from the password
    passwd = passwd.split()
    passwd = "".join(passwd)
    print(passwd)

def make_passwd():
    color_choice = choice(colors)
    animal_choice = choice(animals)
    end_choice = choice(ends)
    #spaces added in case the program desires to add numbers inbetween the words
    passwd = color_choice + " " + animal_choice + " " + end_choice
    return passwd

def get_passwd(color, animal, end):
    #how many passwords should be printed with each run of the program
    #This number will not change the output number of the walkthrought function;
    #that must be changed in the walkthrough function
    print_range = 10
    if "-n" in terminal_args:
        for i in range(1, print_range):
            passwd = make_passwd()
            get_passwd_nums(passwd)
            print()
    elif "-s" in terminal_args:
        for i in range(1, print_range):
            passwd = make_passwd()
            get_passwd_chars(passwd)
            print()
    elif "-d" in terminal_args:
        for i in range(1, print_range):
            passwd = make_passwd()
            get_passwd_default(passwd)
            print()
    else:
        #call on walkthrough function
        walkthrough()
        

if "-h" in terminal_args:
    help()
else:
    get_passwd(colors, animals, ends)
