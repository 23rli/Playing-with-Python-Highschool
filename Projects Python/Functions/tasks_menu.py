#!/usr/bin/python3
# tasks_menu.py
'''Random Utility Task Menu'''
__author__ = "Richard li"
__version__ = "1.0"


import turtle_tasks as tt
import tasks
import turtle
import boolconvert as bc


def main():
    """Runs the task menu which then runs the execution functions"""

    done = False
    screen_made = False
    # allows the user to keep selecting menu items until done:
    while not done:

        # tasks

        print(
            "\nAVAILABLE TASKS: \nSELECT FROM THE FOLLOWING MENU ITEMS: \n"
            "1: Draw a polygon \n"
            "2: Draw random polygons! \n"
            "3: Draw some stairs \n"
            "4: Circling Spiral \n"
            "5: Should you answer your phone?\n"
            "6: Test if a car has the capacity of 4 others\n"
            "7: How much would a speeding ticket cost?\n"
            "8: Can you move (game logic)\n"
            "9: What's the length of the hypotenuse?\n"
            "10: Text Pyramids\n"
            "11: Prime Number Counter\n"
            "12: Character Art\n"
            "0: QUIT!\n"
        )

        selection = int(input("YOUR SELECTION: "))

        if selection in [1, 2, 3, 4]:  # if this is a turtle task, set up a screen
            # don't make a new one if a turtle task has already been executed
            if not screen_made:
                s = turtle.Screen()
                s.bgcolor("black")  # or a color of your choosing
                screen_made = True
                s.tracer(0)

            t = turtle.Turtle()
            s.colormode(255)
            t.color("white")  # or a color of your choosing

        print()  # looks better with a blank line

        ####################
        #  turtle tasks:   #
        ####################

        if selection == 1:  # draw polygon

            # get variables
            num_sides = int(
                s.numinput(
                    "Sides",
                    "How many sides should your polygon have?",
                    default=3,
                    minval=3,
                    maxval=1000,
                )
            )
            side_length = int(
                s.numinput(
                    "Length",
                    "How long should each side be?",
                    default=50,
                    minval=20,
                    maxval=1000,
                )
            )

            # CALL THE FUNCTION!
            tt.draw_polygon(t, num_sides, side_length, s)

        elif selection == 2:  # draw random polygons
            t.color("blue")

            num_polygons = int(
                s.numinput(
                    "Polygons",
                    "How many Polygons should be created?",
                    default=50,
                    minval=20,
                    maxval=1000,
                )
            )

            # CALL THE FUNCTION!
            # change 5 to your variable
            tt.draw_random_polygons(t, num_polygons, s)

        elif selection == 3:  # draw stairs

            # get variables
            num_stairs = int(
                s.numinput(
                    "Sides",
                    "How many stairs do you want?",
                    default=3,
                    minval=3,
                    maxval=100,
                )
            )
            stair_width = int(
                s.numinput(
                    "Length",
                    "How wide should each stair be?",
                    default=50,
                    minval=20,
                    maxval=1000,
                )
            )

            # function call
            tt.draw_stairs(t, num_stairs, stair_width, s)

        elif selection == 4:  # draw mandala spiral

            # get variables
            length = int(
                s.numinput(
                    "Length",
                    "How wide should the diameter of a circle be?",
                    default=2,
                    minval=1,
                    maxval=3,
                )
            )

            # function call
            tt.circling_spiral(t, length, s)

        ########################
        #  non-turtle tasks:   #
        ########################
        elif selection == 5:  # should you pick up the phone?

            # get variables
            print("Please type yes for true, or no for false\n")
            is_morn = bc.convert((input("Is it morning? ")))
            is_mom = bc.convert((input("Is it your mom? ")))
            asleep = bc.convert((input("Is it morning?")))
            grumpy = bc.convert((input("Is it morning? \n")))

            # call the function
            should_answer = tasks.should_answer_cell(
                is_morn, is_mom, asleep, grumpy)
            if should_answer:
                print(
                    "You should answer your phone"
                )
            else:
                print("You don't need to answer your phone")

        elif selection == 6:  # Can four cars fit into one
            print("How many people can fit in your carpool cars?")

            # get variables
            car1_size = int(input("Human capcity of first car: "))
            car2_size = int(input("Human capcity of second car: "))
            car3_size = int(input("Human capcity of thrid car: "))
            car4_size = int(input("Human capcity of fourth car: "))
            car5_size = int(input("Human capcity of fifth car: "))

            # function call
            can_fit = tasks.four_fit_in_one(
                car1_size, car2_size, car3_size, car4_size, car5_size
            )

            # results
            if can_fit == -1:
                print("\nNo car is big enough to hold everyone...")
            else:
                print("\nCar number", str(can_fit), "can fit everyone!")

        elif selection == 7:  # get speeding ticket
            print("Did you get a ticket for speeding???\n")

            # get variables
            print("Answer or just press enter for default")
            speed = int(
                input("What speed were you driving at(in mph): ") or 70)
            is_birthday = bc.convert(
                int(
                    input("Was it your Birthday? "
                          + "(Answer 'yes' for true or 'no' for false): "
                          )
                    or False
                )
            )

            # function call
            ticket = tasks.get_ticket(speed, is_birthday)

            # results
            if ticket == 0:
                print("\nYou got no ticket!!!")
            else:
                print("\nYou got a", str(ticket), "dollar ticket...")

        elif selection == 8:  # can move
            print("Are you stuck?\n")
            print(
                "Please answer in numerals, the numbers 'yes' for true and 'no'"
                + " for false, or letters depedning on the question\n"
            )

            # get variable + function cost
            direction = input(
                "What is your dircection? ('N', 'S', 'E', or 'W'): ")
            reality = tasks.can_move(
                bc.convert(input("Is the north blocked(yes, no): ")),
                bc.convert(input("Is the south blocked(yes, no): ")),
                bc.convert(input("Is the east blocked(yes, no): ")),
                bc.convert(input("Is the west blocked(yes, no): ")),
                bc.convert(input("What is your power level (Int): ")),
                direction
            )

            # results
            if reality:
                print("\n You can move in", direction + " direction!")
            else:
                print("\nOh no! You're stuck in place...")

        elif selection == 9:  # find hypotenuse of triangle
            print("What are the side lengths of the Triangle?\n")

            # get variables + call function
            hypo = tasks.hypotenuse(
                float(input("What is the length of the first side? ")),
                float(input("What is the length of the second side? ")),
                float(input("What is the length of the third side? "))
            )

            # result
            if hypo == -1:
                print("\nThis right triangle doesn't exist")
            else:
                print("\nThe hypotenuse has a length of", str(hypo))

        elif selection == 10:  # text pyramid
            print("Let's make a text pyramid!!!")
            print("Answer or just press enter for default")

            # get variables & call functions
            tasks.text_pyramid(
                int(
                    input(
                        "How many rows do you want the pyramid to be? ")
                    or 16),
                input(
                    "What symbol do you want the pyramid to be made up of? "),
                bc.convert(
                    input(
                        "Do you want the pyramid to be upside-down?"
                        + "(answer 'yes' for true, or 'no' for false): "
                    ) or False
                )
            )

        elif selection == 11:  # counting prime numbers
            print(
                "Let's count some prime numbers! This function will count"
                + " all prime numbers within a range(inclusive) and with a counter"
            )

            # get variables and call function
            primes = tasks.special_primes_counter(
                int(input("\nWhat integer would you like to start at? ")),
                int(input("What integer would you like to end at? ")),
                int(input("What ones digit integers would you like to "
                          + "count by? "))
            )

            # results
            if len(primes) == 0:
                print("There are no primes here ending with your digit")
            else:
                print("\nThe primes we found are:")
                for i in range(len(primes)):
                    print(primes[i])

        elif selection == 12:  # dragon character art
            print("Let's do some word art!\n")

            # get variables + call function
            art = tasks.draw_painting(
                input("What character do you think is used in the drawing? ")
            )

            # print result
            for i in range(len(art)):
                print(art[i])

        elif selection == 0:  # user has quit
            done = True

        if not done:  # only do this if they didn't just quit:
            input("\nHIT ENTER TO CONTINUE")
            if selection in [1, 2, 3, 4] and screen_made:
                s.resetscreen()  # clear any previous drawings from the turtle Screen before new ones


main()
