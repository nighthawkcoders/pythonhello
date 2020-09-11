"""
The main.py file is the Python starting point for the Hello Series project. This main.py code has been designed to run a text based Menu.

A text base menu has purpose of getting input from user and performing the selected action.  This code has been designed to run other code from the multiple files within the project.

Some of the Python files in this Project have a linear organization.  The intention of these files is to introduce, or say hello, to the features of the language.  The string, number, and list files are ommisive of structure.  Thus, these files could be considered "ploaygound", meaning the have no formality.

Abstraction is taking linear code and turning it into procedural or object oriented code.  This is typically done when the file has an overall purpose.  The menu, loop, and class code in this project introduce design, structure, and purpose.  These are key practices described in the AP CS Principles course and exam description.

The Menu code in this file is organized in both procedural and objected oriented styles.  By the end of this series, it will be important to understand the menu code and identify linear, procedural, and objected oriented structures.

"""
from helloseries import loopy

""" Section to execute Python files outside of the main.py file, but within the Hello Series project  """


# String playground code
def stringy():
    exec(open("stringy.py").read())


# Number playground code
def numby():
    exec(open("numby.py").read())


# List, Dictionary, Tuple playground code
def listy():
    exec(open("listy.py").read())


# ASCII/unicode art in imperative or procdural style
def loopy():
    import loopy
    loopy.main()


# ASCII/unicode art in object oriented style
def classy():
    import classy
    cl = classy.Classy()
    cl.print_monkeys()

def randomy():
    exec(open("randomy.py").read())


""" Section to define Menu data and the reference methods for that data  """


# Menu data and methods - object oriented style as it contains data definitions and associates methods with that data
class Menu:
    # Initialize menu properties
    def __init__(self):
        # Menu index and data
        self.options = {
            0: ["Exit", None],
            1: ["Strings", stringy],
            2: ["Numbers", numby],
            3: ["Lists", listy],
            4: ["Loops", loopy],
            5: ["Classes", classy],
            6: ["Random", randomy]

        }
        # Options data indexes
        self.title = 0
        self.func = 1

    # returns option from options list
    def get_title(self, index):
        # return key and title from options
        return str(index) + ": " + self.options[index][self.title]

    # runs a function in options list
    def run(self, index):
        # execute func from options
        exe_func = self.options[index][self.func]
        # test if func exists
        if exe_func is not None:
            print(str(type(exe_func)) + " " + str(exe_func))
            exe_func()  # executes func
        # return true if executed, else false
        return bool(exe_func)


""" Section to display Menu data, receive input from user of program and run selected option(s) """


# Menu display and execution - imperative or procedural style using recursive control flow
def menu_control(menu):
    # heading section
    print()
    print("=" * 25)  # print character "=" 25 times
    print("Please Select An Option")
    print("=" * 25)

    # menu options
    items = len(menu.options)
    for i in range(items):
        print(menu.get_title(i))

    # get choice from user
    index = input("Select Option: ")

    # validate choice and run
    try:  # protects/traps errors from user
        # convert input into integer type
        index = int(index)
        # test if choice is in menu index
        if index in menu.options:
            if index == 0:  # exit condition
                return      # exit out of menu_control
            # runs the choice
            menu.run(index)
        else:
            # raises index error
            raise IndexError()
    except ValueError:  # not a number error occurs if int(index) fails
        print("Not a number, {0} is not  valid.".format(index))
    except IndexError:  # error raised above
        print("Out of range. {0} is not a valid option.".format(index))
    menu_control(menu)  # recursion


""" Section to start execution of program  """

# Activate and run Menu - linear flow of control
# a menu object derived from "Class Menu", this is defining an object only.  Flow of control remains linear.
menu: Menu = Menu()
# a call to menu control function "def menu_control", passing menu object as a parameter to the function. Flow of control is shifted to menu_control function.
menu_control(menu)