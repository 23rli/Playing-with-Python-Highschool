#!/usr/bin/python3
# city_scape.py

'''A simulator that creates a simplifed street with the number of "buildings"
and building addresses stemming from user inputs'''

__author__ = "Richard Li"
__version__ = "1.0"

import turtle
import random
import time

# SPECIAL FEATURES: Included Roof in classical design
# Fancier outline in Classical Style
# Use if statement on height to draw trees?

###############
#MAIN FUNCTION#
###############

# main function, runs all others


def main():
    global s

    # start intro
    setup_mats = intro()

    # setup screen
    s = turtle.Screen()
    s.tracer(0)
    s.screensize(1440, 900)
    s.colormode(255)
    s.bgcolor(135, 206, 235)

    # start & end drawing
    build2d(setup_mats)
    turtle.done()

######
#RACE#
######

# run the turtle race and proclaim victor


def race(start_coor, length, style):
    s.tracer(1)
    # setup racers
    player_1 = turtle.Turtle()
    player_2 = turtle.Turtle()

    player_1.hideturtle()
    player_2.hideturtle()
    player_1.penup()
    player_2.penup()

    if style == 0:
        player_1.goto(start_coor[0], start_coor[1] - 12)
        player_2.goto(start_coor[0], start_coor[1] - 37)
    else:
        player_1.goto(start_coor[0], start_coor[1] - 10)
        player_2.goto(start_coor[0], start_coor[1] - 30)

    player_1.shape("arrow")
    player_2.shape("turtle")

    player_1.showturtle()
    player_2.showturtle()

    sum_1 = 0
    sum_2 = 0

    # countdown start
    countdown()

    # display "go"
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pu()
    pen.goto(0, -100)
    pen.pencolor("red")
    pen.pd()
    pen.write("GO!",
              True, "center", font=("Verdana", 40, "normal"))

    # start race
    while sum_1 < length and sum_2 < length:
        if sum_1 < length and sum_2 < length:
            foward_amount_1 = random.randint(1, 10)
            foward_amount_2 = random.randint(1, 10)

            player_1.forward(foward_amount_1)
            player_2.forward(foward_amount_2)

            sum_1 += foward_amount_1
            sum_2 += foward_amount_2

    pen.clear()

    # proclaim victor
    if(sum_1 >= length):
        proclaim_victor(1)
    else:
        proclaim_victor(2)

# displays countrdown for race


def countdown():

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pu()
    pen.goto(-20, -100)
    pen.pencolor("red")

    # display countdown
    for count in range(3, 0, -1):
        pen.write(count,
                  True, "center", font=("Verdana", 40, "normal"))
        time.sleep(1)
        pen.clear()

# declares winner of race


def proclaim_victor(winner):

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pu()
    pen.goto(0, -100)

    # Arrow win = write win w/ arrow
    if winner == 1:
        pen.write("The Arrow Wins!!!",
                  True, "center", font=("Verdana", 20, "normal"))

    # Turtle win = write win w/ turtle
    else:
        pen.write("The Turtle Wins!!!",
                  True, "center", font=("Verdana", 20, "normal"))

###############
#ANNOUNCE AREA#
###############

# announce approximate area of the structures in the screen


def announce_area(bld_height, width):

    # setup turtle
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.color("red")
    writer.goto(200, 400)

    # setup variable
    area = 0

    # find + calibrate area
    for i in range(0, len(bld_height)):
        area += width * bld_height[i]

    area = str(area)

    # write area
    writer.write("The total surface area is approximately " + area,
                 True, "center", font=("Verdana", 30, "normal"))


#################
#BUILD CITYSCAPE#
#################

# main function for all 2d drawings + starts race


def build2d(setup_mats):

    # setup variables and style
    bld_height = []
    buildstyle = ["skyscraper", "classical"]
    style = random.randint(0, 1)
    width = 0
    if style == 0:
        width = 30
    elif style == 1:
        width = 50
    start_coor = [int(-1 * (setup_mats[0] * (width + 10)) / 2), 0]

    # create buildings
    for structures in range(0, setup_mats[0]):

        # generate building heights
        height = random.randint(40, 200)

        # draw trees
        if 30 < height < 60:
            drawtree2d(height, width, start_coor, buildstyle, style)

        # draw and decorate buildings
        else:
            drawbuild2d(height, width, start_coor, buildstyle, style)
            deco_bld(width, start_coor, style, setup_mats[1])

        # readjust for next building
        start_coor[0] += width + 10
        setup_mats[1] += random.randint(1, 3)
        bld_height.append(height)

    # announce area
    announce_area(bld_height, width)

    # setup variable for road
    start_coor = [int(-1 * (setup_mats[0] * (width + 10)) / 2), - 10]

    # draw road
    buildinfra2d(start_coor, int(setup_mats[0] * (width + 10)), style)

    # setup up variables for race
    start_coor = [int(-1 * (setup_mats[0] * (width + 10)) / 2), - 10]

    # start race
    race(start_coor, int(setup_mats[0] * (width + 10)), style)

# draw 2d road in both styles


def buildinfra2d(start_coor, length, style):

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    # draw city stule road
    if style == 0:

        # turtle setup for road
        pen.penup()
        pen.pencolor("grey")
        pen.fillcolor("grey")
        pen.goto(start_coor[0], start_coor[1])
        pen.pd()

        # draw road
        pen.begin_fill()
        pen.fd(length)
        pen.rt(90)
        pen.fd(50)
        pen.rt(90)
        pen.fd(length)
        pen.end_fill()

        # readjust turtle for stripes
        pen.pu()
        start_coor[1] -= 25
        pen.rt(180)
        pen.goto(start_coor[0], start_coor[1])
        pen.pd()
        pen.pencolor('yellow')

        # draw yellow lines
        for strip in range(0, length // 30):
            pen.fd(20)
            pen.pu()
            pen.fd(10)
            pen.down()
    # draw road for classical style
    elif style == 1:

        # setup turtle for road
        pen.penup()
        pen.pencolor(231, 223, 197)
        pen.fillcolor(231, 223, 197)
        pen.goto(start_coor[0], start_coor[1])
        pen.pd()

        # draw stone road
        pen.begin_fill()
        pen.fd(length)
        pen.rt(90)
        pen.fd(40)
        pen.rt(90)
        pen.fd(length)
        pen.end_fill()


# decorate builds, both styles with addresses, modern wth doors as well
def deco_bld(width, start_coor, style, address):

    # setup turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()

    # reformat address
    address = str(address)

    # decorate city style
    if style == 0:

        # turtle setup for doors
        pen.penup()

        pen.goto(start_coor[0] + 7, start_coor[1])
        pen.fillcolor(35, 172, 196)  # blue window

        pen.pd()

        # draw door
        pen.begin_fill()

        for _ in range(0, 2):
            pen.fd(16)
            pen.lt(90)
            pen.fd(8)
            pen.lt(90)

        pen.end_fill()

        # setup for addresses
        pen.pu()
        pen.goto(start_coor[0] + (width * 2) // 3, start_coor[1] + 20)
        pen.pencolor(231, 223, 197)  # light gray
        pen.fillcolor(231, 223, 197)  # light gray
        pen.pd()
        pen.lt(90)

        # create metal plates
        pen.begin_fill()

        for _ in range(0, 2):
            pen.fd(8)
            pen.rt(90)
            pen.fd(10)
            pen.rt(90)

        pen.end_fill()

        # setup for writing address
        pen.goto(start_coor[0] + (width * 2) // 3 + 5, start_coor[1] + 20)
        pen.pencolor("black")
        pen.pu()

        # write address
        pen.write(address, True, "center", font=("Verdana", 6, "normal"))

    # decorate classical buildings
    elif style == 1:

        # setup turtle for signs
        pen.penup()
        pen.goto(start_coor[0] + (width * 2) // 3 + 8, start_coor[1])
        pen.fillcolor(231, 223, 197)
        pen.pd()
        pen.lt(90)

        # draw signpost
        pen.begin_fill()
        for _ in range(0, 2):
            pen.fd(40)
            pen.rt(90)
            pen.fd(4)
            pen.rt(90)
        pen.end_fill()

        # readjust for signboard
        pen.pu()
        pen.goto(start_coor[0] + (width * 2) // 3, start_coor[1] + 20)
        pen.pd()

        # draw signboard
        pen.begin_fill()
        for _ in range(0, 2):
            pen.fd(15)
            pen.rt(90)
            pen.fd(20)
            pen.rt(90)
        pen.end_fill()

        # readjust for address #
        pen.goto(start_coor[0] + (width * 2) // 3 + 10, start_coor[1] + 20)
        pen.pu()

        # write address
        pen.write(address, True, "center", font=("Verdana", 10, "normal"))


# draw 2d trees in both styles


def drawtree2d(height, width, start_coor, buildstyle, style):

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    # draw city trees
    if style == 0:

        # setup turtle for tree
        pen.penup()
        pen.goto(start_coor[0] + 11, start_coor[1])
        pen.pendown()
        pen.lt(90)
        pen.fillcolor(92, 64, 51)  # green

        pen.begin_fill()

        # draw trunk
        for _ in range(0, 2):
            pen.fd(50)
            pen.rt(90)
            pen.fd(8)
            pen.rt(90)
        pen.end_fill()

        # readjust turtle for leaves
        pen.penup()

        pen.rt(90)
        pen.goto(start_coor[0] + 15, start_coor[1] + height - 15)

        pen.pendown()

        # draw leaves
        pen.fillcolor(69, 139, 0)
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()

    # draw classical trees
    elif style == 1:

        # setup turtle
        pen.penup()
        mid = width // 2
        pen.goto(start_coor[0] + mid - 4, start_coor[1])
        pen.pencolor(107, 66, 38)

        pen.pendown()
        pen.lt(90)
        pen.fillcolor(107, 66, 38)
        pen.begin_fill()

        # draw trunk
        for _ in range(0, 2):
            pen.fd(30)
            pen.rt(90)
            pen.fd(8)
            pen.rt(90)
        pen.end_fill()

        # readjust turtle for leaves
        pen.penup()
        pen.rt(180)
        pen.goto(start_coor[0] + mid - 16, start_coor[1] + 38)
        pen.pendown()
        pen.fillcolor(105, 139, 34)
        pen.pencolor(105, 139, 34)

        # draw leaves
        pen.begin_fill()
        pen.circle(16)
        pen.end_fill()

        pen.penup()
        pen.lt(90)
        pen.goto(start_coor[0] + mid - 16, start_coor[1] + 38)
        pen.pendown()
        pen.begin_fill()
        pen.lt(80)
        pen.fd(50)
        pen.rt(80)
        pen.fd(15)
        pen.rt(80)
        pen.fd(50)

        pen.end_fill()
        pen.pu()
        pen.rt(180)
        pen.goto(start_coor[0] + mid - 6.75, start_coor[1] + 87)
        pen.pd()
        pen.begin_fill()

        pen.rt(180)
        pen.circle(7.5)

        pen.end_fill()

# draw 2d buildings in both styles


def drawbuild2d(height, width, start_coor, buildstyle, style):

    # setup
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(10)
    pen.penup()
    pen.goto(start_coor[0], start_coor[1])

    # draw skyscrapers
    if style == 0:

        pen.pd()
        pen.lt(90)

        for _ in range(0, 2):
            gray = random.randint(50, 225)
            pen.fillcolor(gray, gray, gray)
            pen.begin_fill()
            pen.fd(height)
            pen.rt(90)
            pen.fd(width)
            pen.rt(90)
            pen.end_fill()

    # prep and create classical buildings
    elif style == 1:

        # setup variables
        height = height // 5
        sort = 0
        coor = [start_coor[0], start_coor[1]]
        pillar_heights = []

        # randomizing pillar heights
        while sort < height:
            temp = random.randint(10, 30)
            sort += temp
            pillar_heights.append(temp)
        pillar_heights.append(pillar_heights[len(pillar_heights) - 1] - 1)

        # draw classical buildings
        classic_base(pillar_heights, coor, width)
        for i in range(0, len(pillar_heights)):

            # draw floors
            platform(coor, width)

            # setup coord of turtle for pillars
            coor[1] += 10
            coor[0] += 4

            # draw pillars
            for _ in range(0, 3):
                pillar(pillar_heights[i], coor)
                coor[0] += 15

            # setup coords for roof
            coor[1] += pillar_heights[i] + 2
            coor[0] = start_coor[0]

        # draw tile roof
        tile_roof(coor)

# draw floors for each floor of buildings for classical style build


def classic_base(pillar_heights, coor, WIDTH):

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(10)
    pen.penup()
    pen.goto(coor[0], coor[1])
    pen.fillcolor(255, 255, 240)

    # find current height of build
    height = 0
    for i in range(0, len(pillar_heights) - 1):
        height += 12
        height += pillar_heights[i]

    height += 10
    pen.begin_fill()
    pen.pd()

    # draw floor
    pen.lt(90)

    for _ in range(0, 2):
        pen.fd(height)
        pen.rt(90)
        pen.fd(WIDTH)
        pen.rt(90)

    pen.end_fill()

# draw tile roof for classical style build


def tile_roof(coor):

    # constant
    RF_BASE = 50
    RF_SIDE = 29

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    pen.penup()
    pen.goto(coor[0], coor[1])
    pen.pendown()
    pen.fillcolor(198, 110, 78)  # terrecota color
    pen.begin_fill()

    # draw roof
    pen.lt(30)
    pen.fd(RF_SIDE)
    pen.rt(60)
    pen.fd(RF_SIDE)
    pen.rt(150)
    pen.fd(RF_BASE)

    pen.end_fill()

# create backdrop for classical style build


def platform(coor, WIDTH):

    # constant
    BD_ANGLES = 90
    BD_HEIGHT = 10

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    pen.penup()
    pen.goto(coor[0], coor[1])
    pen.pendown()
    pen.fillcolor(255, 255, 240)  # creme color

    pen.begin_fill()

    # draw backdrop
    for _ in range(0, 2):

        pen.fd(WIDTH)
        pen.lt(BD_ANGLES)
        pen.fd(BD_HEIGHT)
        pen.lt(BD_ANGLES)

    pen.end_fill()

# draw pillar for classical style build


def pillar(HEIGHT, coor):
    # constants
    EDGE_ANGLES_L = 135
    EDGE_ANGLES_R = 45
    PILLAR_WIDTH = 12
    EMBELLISH_LENGTH = 1

    # setup turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    pen.penup()
    pen.goto(coor[0], coor[1])
    pen.pendown()
    pen.fillcolor(255, 255, 240)  # creme color
    pen.begin_fill()

    # draw pillar
    for _ in range(0, 2):

        pen.fd(PILLAR_WIDTH)
        pen.lt(EDGE_ANGLES_L)
        pen.fd(EMBELLISH_LENGTH)
        pen.rt(EDGE_ANGLES_R)
        pen.fd(HEIGHT)
        pen.rt(EDGE_ANGLES_R)
        pen.fd(EMBELLISH_LENGTH)
        pen.lt(EDGE_ANGLES_L)

    pen.end_fill()


#######
#INTRO#
#######

# welcome User, recieve input: address # and # of buildings


def intro():

    # determine readiness sequence
    ready = False
    while ready != True:
        get_ready_q = turtle.textinput("Welcome to City Road Simulation!",
                                       "This program will create"
                                       + " a city street with classical or city"
                                       + " buildings. Before the \nsimulation"
                                       + " we will ask you a couple questions."
                                       + " Please type \"yes\" if you're"
                                       + " ready.")
        if get_ready_q == "yes":
            ready = True

    # c ollect info
    num_build = int(turtle.textinput("Welcome Tab", "How many buildings do you"
                                     + " want to build?"))

    num_add = int(turtle.textinput("Welcome Tab", "What is the address number"
                                   + " your first building?"))

    # share info
    setup_mats = [num_build, num_add]

    return setup_mats


# run entire code
main()
