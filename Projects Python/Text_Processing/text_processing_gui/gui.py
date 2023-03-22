#!/usr/bin/python
# gui.py

'''provides user interface that allows typing into text boxes,
selecting from different functions, and displaying results in a text area'''

__version__ = "2.0"
__author__ = 'beckwith'


import text_processing   # you will write your functions in this module

import tkinter
from tkinter.font import Font


### STEP 11111111111!!!!!!!!!!!!!YOU WILL WRITE YOUR MENU NAMES HERE !!!!!!!!!!!! #####
# these words will appear in the menu:
OPTIONS = [
    "Choose A Function:",
    "Email Address Checker",
    "Password Checker",
    "Python Analyzer",
    "Writing Analyzer"
]


root = tkinter.Tk()  # the base window that all tkinter objects go into
# you can name it anything, but usually root or master or window
# the buttons and windows and menu will all be placed into this window

root.title("GUI + Text Functions")  # set title to something you like

###################################
# FUNCTIONS CALLED BY MENU AND BUTTONS:
###################################


def quitting_time():
    '''called when Quit button is pressed'''
    root.destroy()


def show_instructions(event):
    '''Called when menu item is selected and will show instructions'''

    global menu_var, results_display

    selection = menu_var.get()  # get which item was selected
    # set instructions text for the item selected:

    # STEP 22222222222!!!!!!!!!!!!!!!!!!PUT YOUR MENU ITEMS AND INSTRUCTIONS HERE!!!!!!!!!!!!!
    if selection == "Email Address Checker":
        instructions = "Give me one email in the first box and I will " +\
            "verify if it is valid"
    elif selection == "Password Checker":
        instructions = "Give me a password in the first box and I will " +\
            "verify if it is strong"
    elif selection == "Python Analyzer":
        instructions = "Enter a python file in the big box on the right," +\
            " then click submit"
    elif selection == "Writing Analyzer":
        instructions = "Enter a lot of text or an essay in the big box on " +\
            "the right, then click submit"
    else:
        instructions = "Nothing selected yet"

    ### DISPLAYS INSTRUCTIONS IN THE BIG TEXT AREA: ###
    results_display.configure(state="normal")         # allow editing of text
    results_display.delete(1.0, tkinter.END)          # delete previous text
    # show results in text area
    results_display.insert(tkinter.END, instructions)
    results_display.configure(state="disabled")       # prevent editing of text


def submit():
    '''called when the submit button is clicked'''

    global menu_var, results_display, entry_1, entry_2, entry_3
    global entry_4, input_area, results_label
    # gets values (as strings) from the entry boxes
    arg_1 = entry_1.get()

    # in case you need more:
    arg_2 = entry_2.get()
    arg_3 = entry_3.get()
    arg_4 = entry_4.get()

    ### USE THIS FOR LARGER BODIES OF INPUTTED TEXT THAT WON'T FIT IN THE LITTLE BOXES ###

    # get text from large text area:

    large_text = input_area.get("1.0", tkinter.END)  # see explanation below:

    # EXPLANATION:

    # "1.0" = STARTING point: means the input should be read from line 1, character 0
    #       (something like "2.3" = line 2 character 3)
    # tkinter.END = ENDING point: tkinter.END reads all the way to the end of the text area
    #       (something like END + "-2c" means to not read the last two characters)
    #       (use END + "-1C" to get rid of the newline character at the end!)

    large_text = large_text.strip()   # extra \n needs to be stripped

    # NOW YOU CAN USE THE VARIABLE large_text AND SEND IT TO A FUNCTION
    # (LIKE WITH YOUR ENCRYPTION FUNCTION)

    return_text = ""
    selection = menu_var.get()

    ### STEP 3333333333!!!!!!!!!!!!!!!YOU WILL WRITE YOUR OWN CODE HERE !!!!!!!!!!!!!!!! #####

    # calls selected function, sending it the necessary arguments
    #    and storing the returned string into display_text:

    if selection == "Email Address Checker":
        email = text_processing.email_checker(arg_1)
        display_text = email
    elif selection == "Password Checker":
        password = text_processing.password_checker(arg_1)
        display_text = password
    elif selection == "Python Analyzer":
        pyth = text_processing.python_analyzer(large_text)
        display_text = pyth
    elif selection == "Writing Analyzer":
        writ = text_processing.writing_analyzer(large_text)
        display_text = writ
    else:
        display_text = "No function selected or not ready yet"

    ## NO NEED TO EDIT ANYTHING ELSE FROM HERE DOWN! ##
    # show something in the label:
    results_label.config(
        text="Results of calling function " + selection.upper() + ":")

    # deletes old text and insert results text into the large text area:
    results_display.configure(state="normal")  # allow editing of text
    results_display.delete(1.0, tkinter.END)
    # show results in text area
    results_display.insert(tkinter.END, display_text)
    results_display.configure(state="disabled")  # prevent editing of text


def main():

    global menu_var, results_display, entry_1, entry_2, entry_3
    global entry_4, input_area, results_label
    ###################################
    # SET UP ALL THE DISPLAY COMPONENTS:
    ###################################

    # nice font:
    my_font = Font(family="Verdana", size=15, weight="bold")

    ###################################
    # 1. TEXT AREA THAT DISPLAYS RESULTS, USING THE ABOVE FONT
    ###################################
    results_display = tkinter.Text(root,  # display needs the tkinter window to be put in
                                   height=30,
                                   relief="ridge",
                                   bd=6,
                                   width=60,
                                   font=my_font,
                                   foreground='white',
                                   background='black')

    # (PhotoImages must be .gif)

    results_display.configure(state="normal")  # allow editing of text
    # insesrts default text
    results_display.insert(tkinter.END, "Welcome!")
    results_display.configure(state="disabled")

    ###################################
    # 2. TEXT AREA FOR ENTERING LARGE AMOUNTS OF TEXT
    ###################################
    input_area = tkinter.Text(root,
                              height=30,
                              bd=2,
                              width=60,
                              font=my_font,
                              foreground='red',
                              background='black')

    # inserts default text
    input_area.insert(tkinter.END, "You can paste text in here")
    ###################################
    # 3. TEXT LABEL THAT CAN SHOW RESULTS:
    ###################################
    # default text is 'other info'
    results_label = tkinter.Label(text="other info")

    ###################################
    # 4. BUTTONS
    ###################################

    # will call the submit() function when pressed:
    submit_button = tkinter.Button(text="SUBMIT", command=submit)

    # will call quitting_time when pressed:
    quit_button = tkinter.Button(root, text="Quit", command=quitting_time)

    ###################################
    # 5. SET UP PULLDOWN MENU OF FUNCTION CHOICES:
    ###################################

    # this variable holds the selected value from the menu
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0])  # default value

    # create the optionmenu (pulldown menu) with the options above:
    option_menu = tkinter.OptionMenu(
        root, menu_var, *OPTIONS, command=show_instructions)

    ###################################
    # 6. PLACE EVERYTHING IN THE TKINTER WINDOW:
    #     a "grid" allows you to turn the tkinter window into a series
    #     of rows and columns and specifcy where to place everything
    ###################################
    # place the menu in the top left:
    option_menu.grid(row=0, column=0, columnspan=1)

    # place the buttons in the top middle:
    submit_button.grid(row=0, column=1, columnspan=1)
    quit_button.grid(row=0, column=2, columnspan=1)

    # sets up argument input boxes...ADD MORE IF YOU NEED THEM!!!
    entry_1 = tkinter.Entry()  # makes an Entry object
    entry_2 = tkinter.Entry()
    entry_3 = tkinter.Entry()
    entry_4 = tkinter.Entry()

    # place the entry boxes in the next row, going across...ADD MORE IF NEEDED!!!
    entry_1.grid(row=1, column=0)
    entry_2.grid(row=1, column=1)
    entry_3.grid(row=1, column=2)
    entry_4.grid(row=1, column=3)

    # place the label in the next row (is just one row of text):
    results_label.grid(row=3, column=0, columnspan=4)

    # place the text areas in the next row (is a whole box of text):
    results_display.grid(row=4, column=0, columnspan=2)
    input_area.grid(row=4, column=2, columnspan=2)
    # make it so that words won't get broken up when reach end of text box:
    results_display.config(wrap=tkinter.WORD)
    input_area.config(wrap=tkinter.WORD)

    # waits for button clicks to take actions:
    root.mainloop()


if __name__ == "__main__":
    main()
