#A password generator written in Python

#V0.0 relies on long sentences rather than special characters and numbers

###################################
#####Written by Michael Cooney#####
############Jan 3 2018#############
###################################


from random import choice


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

def get_passwd(color, animal, end):
    color_choice = choice(color)
    animal_choice = choice(animal)
    end_choice = choice(end)
    print(color_choice + animal_choice + end_choice)


for i in range(5):
    get_passwd(colors, animals, ends)
