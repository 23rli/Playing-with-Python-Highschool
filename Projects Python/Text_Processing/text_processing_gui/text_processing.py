#!/usr/bin/python
# gui.py

'''provides user with the utilities needed to run the GUI(The machinations 
behind the action)'''

__version__ = "1.0"
__author__ = 'Richard'
import string


def email_checker(address):
    """Checks if Email has the proper format

    :param: address: email address to be analyzed
    :return: String statement about error or correct formating
    """

    # Check Attributes

    if address.count("@") == 1:
        if address.find("@") + 1 < address.find("."):
            if address[0] not in string.digits:
                if address[-4:] in ".org.com.net.edu.gov":
                    return "It's a good email address"
                else:
                    return "Invalid: It does not end in the appropriate way"
            else:
                return "Invalid: The first digit of the email can not be a digit"
        else:
            return "Invalid: The '.' does not come after the @ symbol"

    return "Invalid: There is more than or no '@' symbols in this email"


def password_checker(str):
    """Checks if password has the proper format that makes it storng

    :param: str: password to be analyzed
    :return: String statement about error or that the password is strong
    """
    if len(str) >= 8:
        if variation(str):  # Own restriction = Password must have lowercase
            return "This password is good"
        else:
            return "INVALID: This password is missing variation!\n\
                    it needs one lowercase, uppercase, number, and symbol"
    else:
        return "INVALID: This password is too short"
    return


def variation(str):
    """Checks if password has the proper variations(symbol, lower, upper, num)

    :param: str: password to be analyzed
    :return: True if the password has all the correct part, false if otherwise
    """

    # Components:
    lower = False
    upper = False
    symbol = False
    num = False

    # Checking Componenets
    for i in range(len(str)):
        ascii_value = ord(str[i])
        if ascii_value <= 57 and ascii_value >= 48:
            num = True
        elif ascii_value <= 122 and ascii_value >= 97:
            lower = True
        elif ascii_value <= 90 and ascii_value >= 65:
            upper = True
        else:
            symbol = True

    if upper and lower and num and symbol:
        return True
    return False


def python_analyzer(file):
    """Checks Python code and finds statistics

    :param: file: python code to be analyzed
    :return: String statement detailing the code
    """

    # Find Author, number of lines, functions, and file name
    begin = file[1:].find("#") + 2
    print(begin)
    endin = file.find(".py") + 3
    print(endin)
    name = file[begin: endin]
    begin = file.find("__author__") + 14
    print(begin)
    endin = begin + file[begin:].find("\n") - 1
    print(endin)
    author = file[begin:endin]
    num_lines = file.count("\n") + 1
    functions = ""
    num_func = file.count("\ndef ")

    # Find Function names
    prev_func = 0
    for i in range(num_func):
        beg = prev_func + file[prev_func:].find("\ndef ") + 4
        print(beg)
        end = beg + file[beg:].find("(")
        print(end)
        functions += (file[beg: end] + ", ")
        prev_func = end

    # Find number of for, if, and while statements
    for_loops = file.count("for ")
    if_state = file.count("if ")
    whiles = file.count("while ")

    # Find imports
    prev_import = 0
    imports = ""
    for i in range(file.count("\nimport ")):
        beg = prev_import + file[prev_import:].find("import") + 7
        end = beg + file[beg:].find("\n")
        imports += file[beg:end] + " "
        prev_import = end

    # Find variables changes and conditionals
    variable = file.count(" = ")
    conditional = file.count("=>") + file.count("==") + file.count("=<")\
        + file.count(">=") + file.count(">") + file.count("<=")\
        + file.count("<")

    # Print results
    analyzed = "Analyzing " + name + "...\n...\n...\n" + author \
        + " is the author of this Python program\n" \
        + "it has " + str(num_lines) + " lines of code\n"\
        + "The code defines " + str(num_func) + " functions named " +\
        functions + "\nThe code uses:\n    " + str(for_loops) + " for loops\n"\
        + "    " + str(if_state) + " if statements\n    "\
        + str(whiles) + " while loops\n\n" + "The code imports the "\
        + "following modules: " + imports + "\n\nThere are " + str(variable)\
        + " variable assignments (uses of =, but not ==)\n\nThere are "\
        + str(conditional) + " conditionals using ==, <, >, <=, >="

    return analyzed


def writing_analyzer(text):
    """Checks text/essay stats

    :param: text: text to be analyzed
    :return: String statement with statistics about the text
    """

    # Check number of sentences, words, questions, and exclamations
    num_sentences = text.count(".") - 3 * text.count("...")
    num_words = text.count(" ") + 1
    num_qs = text.count("?")
    nums_ex = text.count("!")

    # find grade level of writing
    avg_word_len = 0
    syllables = 0
    broken = text.split()
    for i in range(len(broken)):
        avg_word_len += len(broken[i])
        syllables += (len(broken[i]) // 3) + 1

    avg_word_len /= len(broken)

    # Flesch-Kincaid formula
    grade = 0.39 * (num_words/num_sentences) + 11.8 * \
        (syllables/num_words) - 15.59

    # Report results
    report = "This piece of text has " + str(num_sentences) + " sentence(s)"\
        + ", and " + str(num_words) + " words.\n\nIt also has " + str(num_qs)\
        + " question(s), and " + str(nums_ex) + " exclamations!\nThe average "\
        + "length of a word in this text is " + str(avg_word_len) \
        + " letters.\n" + "The reading level of this text --"\
        + " considering that the average "\
        + "syllable is 3 letters long, is " + str(grade) + " grade writing" \
        + "(this is extremly inaccurate)"

    return report
