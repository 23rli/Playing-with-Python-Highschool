#!/usr/bin/python3
# mad_libs.py

'''Mad Libs'''

__author__ = "Richard Li"
__version__ = "1.0"

import textwrap


def main():

    #######
    #INTRO#
    #######

    name = intro()

    #####################
    #Get words from user#
    #####################

    pres         = input("What's a silly name? : ")
    country      = input("What's the name of a fantasy country? : ")
    cit_name     = input("What would a citizen of " +
                         country + " call themselves? : ")
    animal       = input("What's the plural name of your favorite animal? : ")
    PiT          = input("What's a place in town? : ")
    rando        = input("What's a funny name? : ")
    num          = int(input("What's a random number less than 1,000,000? : "))
    dumb_animal1 = input("What's the dumbest animal in the world? : ")
    dumb_animal2 = input("What's the 2nd dumbest animal in the world? : ")
    vaca_loc     = input("What's your dream vacation location? : ")
    c_verb       = input("What is an aggressive contact verb?(past tense) : ")
    c_verb2      = input("What is an aggressive contact verb?\
                         (present perfect tense (ing)) : ")
    predator     = input("What's the name of an Apex predator(Fake or real)? \
                          : ")
    pastry       = input("What's your favorite pastry? : ")
    ran_noun     = input("What is a plural person,\
                          place or thing(A plural noun por favor)? : ")
    farewell     = input("what is your favorite way to say goodbye? : ")

    # Calculate num variable(random equation)
    age = num % 1538 + 73 + len(predator)

    ##############
    #Create Story#
    ##############

    storyp1 = "After President " + pres + " announced this week that " \
        + country + " was conscripting some " + str(num) + " " + animal \
        + " to reinforce its war effort in " + PiT + ", " \
        + "flights out of " + country \
        + " cities quickly sold out. This latest wave of " + animal \
        + " exodus included " + rando + ", a " + \
        str(age) + "-year-old " + cit_name + "."

    storyp2 = "Mr(s)." + rando + " comments: A few " + dumb_animal1 \
        + " and an army of " + dumb_animal2 + " are leading us to a post apocolyptic " \
        + vaca_loc + ". I say that because " + animal + "s around me in " \
        + country + " behaved as if they had been " \
        + c_verb + " by a " + predator + ", dragging my entire " \
        + pastry + " into a dreadful war. All I saw was " \
        + cit_name + " loser " + animal + " " + c_verb2 + " their " + pastry \
        + ", while the entire " + predator + " " + animal + " " + pastry \
        + " mix has turned my people into an army of " + ran_noun + ""

    ############
    #Tell Story#
    ############
    story(storyp1, storyp2, name, farewell, age)


# Play Intro for user
def intro():
    print("Hello and Welcome to Mad Libs! We will begin shortly!")
    print("This is a game where you'll answer some questions,\n\
    input some words or numbers, and then recieve a funny story!")
    name = input("Are you ready? Please type your name to begin! ")
    print()
    print("Please answer the question below \"" + name + "\"!")
    return name

# Play Story


def story(storyp1, storyp2, name, farewell, age):
    print("\n\n\n Here's your story \"" + name + "\": \n")

    print(textwrap.fill(storyp1, 70))
    print()
    print(textwrap.fill(storyp2, 70))
    print()
    print("That's it, ")
    print(textwrap.fill(((farewell + " ") * age), 410))


# Run code
main()
