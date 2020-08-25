"""
Python starting point for Project Hello Series project is this main.py code. This main.py code has been designed to run a text based Menu.

A text base menu has purpose of getting input from user and performing the selected action.  This code has been designed to run  code from multiple files.

Some of the Python files in this Project have a linear organization.  The intention of these files is to introduce, or say hello, to the features of the language.

The Menu code in this file is organized in both functional and objected oriented styles.  By the end of this series, it will be important to understand the topics in the menu and identify code in linear, functional, or objected oriented structures.

Abstraction is talking linear code and turning it into functional or object oriented code.  This is a key idea on the AP CSP exam.
"""


# Menu definitions
class Menu:
    # String playground code
    def stringy(self):
        exec(open("./stringy.py").read())

    # Number playground code
    def numby(self):
        exec(open("./numby.py").read())

    # List, Dictionary, Tuple playground code
    def listy(self):
        exec(open("./listy.py").read())

    # ASCII/unicode art imperative style
    def loopy(self):
        exec(open("./loopy.py").read())

    # ASCII/unicode art object oriented style
    def classy(self):
        exec(open("./classy.py").read())

    # Menu index and data
    options = {
        0: ["Exit", None],
        1: ["Strings", stringy],
        2: ["Numbers", numby],
        3: ["Lists", listy],
        4: ["Loops", loopy],
        5: ["Classes", classy]
    }
    # Options data indexes
    title = 0
    func = 1

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
            exe_func(self)  # executes func
        # return true if executed, else false
        return bool(exe_func)


# Menu control
def menu_control():
    # menu object derived from Class Menu
    menu: Menu = Menu()
    # menu control loop
    repeat: bool = True
    while repeat:
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
                # runs the choice, repeat set to false if Exit is picked
                repeat = menu.run(index)
            else:
                # raises index error
                raise IndexError()
        except ValueError:  # not a number error occurs if int(index) fails
            print("Not a number, {0} is not a valid index.".format(index))
        except IndexError:  # error raised above
            print("Out of range. {0} is not a valid index.".format(index))


# start menu
menu_control()
