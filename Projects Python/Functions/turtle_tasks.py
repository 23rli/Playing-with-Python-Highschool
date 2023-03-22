#!/usr/bin/python3
# tasks_menu.py
'''Turtle task functions - Execution'''
__author__ = "Richard li"
__version__ = "1.0"

import turtle
import random


def ani_body():
    turtle t = new turtle()


def draw_polygon(t, num_sides, length, s):
    """draw a polygon specified via inputs

    :param: t: turtle import to perform turtle drawings
    :param: num_sides: the positive integer for the number of sides
    :param: length: a positive integer for the length of the sides of the shape
    :param: s: a function to display the screen"""

    # draw a polygon:
    for i in range(num_sides):
        t.fd(length)
        t.lt(360 / num_sides)
        s.update()


def draw_random_polygons(t, num, s):
    """draw multiple polygon specified via inputs

    :param: t: turtle import to perform turtle drawings
    :param: num: number of polygons to be drawn
    :param: s: a function to display the screen"""

    # draw random polygons:
    for i in range(num):
        draw_polygon(t, random.randint(3, 12), random.randint(10, 80), s)
        t.lt(random.randint(60, 120))


def draw_stairs(t, num_stairs, stair_width, s):
    """draw stairs(2D) specified via inputs

    :param: t: turtle import to perform turtle drawings
    :param: num_stairs: positive integer of amount of stairs to be drawn
    :param: stair_width: positive integer detailing the size of stairs
    :param: s: a function to display the screen"""

    # draw stairs
    t.begin_fill()
    t.fd(stair_width * num_stairs)
    s.tracer(9)
    t.lt(90)
    for i in range(num_stairs):
        t.fd(stair_width)
        t.lt(90)
        t.fd(stair_width)
        t.rt(90)
    t.lt(180)
    t.fd(stair_width * num_stairs)
    t.end_fill()


def circling_spiral(t, length, s):
    """Own Function, drawing a spiral made up of concentric circles

    :param: t: turtle import to perform turtle drawings
    :param: length: a positive integer for the size of the mandala thing?
    :param: s: a function to display the screen"""

    # setup colors
    colors = ["white", "red", "orange", "yellow",
              "limegreen", "blue", "purple", "gray"]
    temp = length

    # draw mandala
    for g in range(7, -1, -1):
        temp = length * (g + 1)
        for h in range(8):
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.seth(360 - 45 * h)
            for i in range(40):
                for j in range(0, temp, 2):
                    t.pencolor(colors[g])
                    t.circle(j)
                t.rt(i)
                t.fd(temp)
            s.update()
