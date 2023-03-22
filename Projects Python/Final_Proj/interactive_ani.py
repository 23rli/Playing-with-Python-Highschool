#!/usr/bin/python
# gui.py

'''An Interactive animation --- using turtle and tkinter. Change colors, shapes,
and other designs while the animation is playing'''

##########
# NOTE: Anthony Beckwith stated on 1/13/23 that not using modules was fine given
# the nature of my project --- Please reflect this in my grade. Thank You
# - CAN YOU PROVE THIS?  - Mr. B  :)

__version__ = "1.0"
__author__ = 'li'

from random import randint
from tkinter import *
import turtle

# arrays for drop down menus
COLORS = [
    "White",
    "Red",
    "Blue",
    "Green",
    "Purple",
    "Yellow",
    "Sky Blue"
]

OPTIONS = [
    "Choose an Animation:",
    "Expanding Animation",
    "Spiral Animation"
]

# screen setup
root = Tk()
root.title("Turtle Animations")
s = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
s.tracer(9)
s.delay(1000)
s.screensize(1440, 900)
s.colormode(255)


def quitting_time():
    '''called when Quit button is pressed'''
    root.destroy()


def main():
    '''main functions: Created Tkinter Menu'''

    # other functions get accesibility
    global menu_var, color_var, size_scale, shape_scale, num_scale, radius_scale

    #################################
    # Creation of all aspects of menu#
    #################################

    # Creation of descriptions
    label1 = Label(root, text="Select Animation and Press Submit")
    label1.config(font=("Courier", 14))
    label2 = Label(root, text="Universal settings: Change Animation")
    label2.config(font=("Courier", 14))
    label3 = Label(root, text="Settings only for Expanding Animation")
    label3.config(font=("Courier", 14))

    # Create button for changing animations
    submit_button = Button(text="SUBMIT", command=call_action)

    # Create button to quit menu
    quit_button = Button(root, text="Quit", command=quitting_time)

    menu_var = StringVar(root)  # holds menu for option_menu
    menu_var.set(OPTIONS[0])  # default value

    # create the option_menu (pulldown menu) with the options above:
    option_menu = OptionMenu(
        root, menu_var, *OPTIONS)

    # Create Menu for color choices
    color_var = StringVar(root)
    color_var.set(COLORS[0])  # default value
    color_menu = OptionMenu(
        root, color_var, *COLORS)

    # Create sliders for size, shape, number of shapes, and radii
    size_scale = Scale(root, digit=1000, length=200, sliderlength=50,
                       label="Animation Size", from_=2, to=70, orient=HORIZONTAL)

    shape_scale = Scale(root, digit=1000, length=200, sliderlength=50,
                        label="Shape Sides", from_=3, to=10, orient=HORIZONTAL)

    num_scale = Scale(root, digit=1000, length=200, sliderlength=50,
                      label="# of Circling Shapes(Radius > 0)",
                      from_=1, to=9, orient=HORIZONTAL)

    radius_scale = Scale(root, digit=1000, length=200, sliderlength=50,
                         label="Radius of Circle", from_=0, to=5,
                         orient=HORIZONTAL)

    # place all created widgets in window
    label1.grid(row=0, column=0, columnspan=1)
    option_menu.grid(row=1, column=0, columnspan=1)
    submit_button.grid(row=2, column=0, columnspan=1)
    label2.grid(row=3, column=0, columnspan=1)
    color_menu.grid(row=4, column=0, columnspan=1)
    size_scale.grid(row=5, column=0, columnspan=1)
    label3.grid(row=6, column=0, columnspan=1)
    shape_scale.grid(row=8, column=0, columnspan=1)
    num_scale.grid(row=9, column=0, columnspan=1)
    radius_scale.grid(row=10, column=0, columnspan=1)
    quit_button.grid(row=0, column=1, columnspan=1)

    root.mainloop()


def call_action():
    '''Called when menu item is selected and will show instructions'''

    global menu_var

    selection = menu_var.get()  # get which item was selected

    # Run animation depending on selection
    if selection == "Expanding Animation":
        while True:
            expanding_ani()

    elif selection == "Spiral Animation":
        while True:
            spiral_ani()
    else:
        pass

################################  Animations  ##################################


def spiral_ani():
    """Generate Spiral Animation"""

    # set default size to 10
    size_scale.set(10)
    length = size_scale.get()

    # set up background
    s.bgcolor("black")

    # display animation
    for j in range(3):
        for i in range(2, 8, 1):
            draw_polygon(0, 0, i, size_scale.get(), 0, j)
        for i in range(8, 2, -1):
            draw_polygon(0, 0, i, size_scale.get(), 0, j)


def expanding_ani():
    """Generate Expanding Animation"""

    # set default shape to triangle
    shape_scale.set(3)

    # display animation for extended time
    for j in range(4000):
        spin_cube(radius_scale.get(), shape_scale.get(), num_scale.get(),
                  j % 12)
        s.reset()


def spin_cube(r, sides, num, angle):
    """Generate 1 cycle of expanding animation

    :param: r: radius of said animation that sets how far shapes are drawn from
    the center
    :param: sides: the number of sides the shapes drawn have
    :param: num: the number of shapes drawn at each angle
    :param: angle: the angle at which these shapes are drawn at"""

    SQRT2 = 1.41421356

    # Background, turtle and Color setup
    s.bgcolor("black")
    t.hideturtle()
    setchange(r % 128)

    # Begin individual angle animations
    for i in range(0, 360, 12):
        for j in range(1, num + 1, 1):
            display(r, i, j, sides, SQRT2)
        s.update()


def display(r, i, j, sides, SQRT2):
    """Generate 1 cycle of expanding animation

    :param: r: radius of said animation that sets how far shapes are drawn from
    the center
    :param: i: the angle at which these shapes are drawn at
    :param: j: the number of shapes drawn at each angle
    :param: sides: the number of sides the shapes drawn have
    :param: SQRT2: literally the Square root of 2 --- 
    used to calculate shape size"""

    # setup turtle + find right coords for new shape
    t.penup()
    t.goto(0, 0)
    t.setheading(i)
    t.forward(r * (j * size_scale.get()/4))
    t.right(90 + 90 - 360/sides)
    t.pd()

    # draw shape
    for k in range(sides):
        t.forward(size_scale.get() * SQRT2)
        t.right(360 / sides)

    # display
    s.update()


def draw_polygon(x, y, num_sides, length, iterator, growth):
    """draw a polygon specified via inputs

    :param: x: x coordinate of the turtle
    :param: y: y coordinate of the turtle
    :param: num_sides: number of sides to the shape
    :param: length: distance of shape away from oriin
    :param: iterator: counter for the number of shapes previously displayed
    :param: growth: number of sides of shape drawn before new coords for next
    shape are selected and recorded"""

    # Setup turtle
    t.hideturtle()
    s.colormode(255)
    if iterator >= 40:
        print("here")
        return
    t.pu()
    t.goto(x, y)
    t.left(360//num_sides)
    t.pd()
    newcoord = [0, 0]
    dir = t.heading()

    # set fill and color
    setchange(iterator)

    # draw a polygon + set new coord:
    if (num_sides % 2 == 1 and growth != 0 or growth == 2):
        t.begin_fill()
        for i in range(num_sides):
            t.fd(length)
            t.lt(360 / num_sides)
            if (i == num_sides - growth):
                newcoord[0] = t.xcor()
                newcoord[1] = t.ycor()
        t.end_fill()
    else:
        for i in range(num_sides):
            t.fd(length)
            t.lt(360 / num_sides)
            if (i == growth):
                newcoord[0] = t.xcor()
                newcoord[1] = t.ycor()

    # display drawing
    s.update()

    # Recursive call funciton for next object
    draw_polygon(newcoord[0], newcoord[1],
                 num_sides, (length // size_scale.get() + 1) *
                 size_scale.get(),
                 iterator + 1, growth)

    # delete drawing in post
    for i in range(num_sides):
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()
        t.undo()

##################################  Interactions  ##############################


def setchange(fade):
    """change the color of the lines in the animation
    :param: fade: distance from origin deciding fill opacity"""

    # setup vairables
    selection = color_var.get()

    fade_variability = 2

    # increase severity
    i = fade * fade_variability

    # address all possibilities - color + fill
    if selection == "White":
        t.color("white")
        t.fillcolor(i, i, i)
    elif selection == "Red":
        t.color("red")
        t.fillcolor(i, 0, 0)
    elif selection == "Blue":
        t.color("blue")
        t.fillcolor(0, 0, i)
    elif selection == "Green":
        t.color("green")
        t.fillcolor(0, i, 0)
    elif selection == "Purple":
        t.color("purple")
        t.fillcolor(i, 0, i)
    elif selection == "Yellow":
        t.color("yellow")
        t.fillcolor(i, i, 0)
    elif selection == "Sky Blue":
        t.color(135, 206, 235)
        t.fillcolor(0, i, i)
    else:
        pass


main()
