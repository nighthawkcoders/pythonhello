"""
Python starting point for Project Hello Series project is this main.py code. This main.py code has been designed to run a text based Menu.

A text base menu has purpose of getting input from user and performing the selected action.  This code has been designed to run  code from multiple files.

Some of the Python files in this Project have a linear organization.  The intention of these files is to introduce, or say hello, to the features of the language.

The Menu code in this file is organized in both functional and objected oriented styles.  By the end of this series, it will be important to understand the topics in the menu and identify code in linear, functional, or objected oriented structures.

Abstraction is talking linear code and turning it into functional or object oriented code.  This is a key idea on the AP CSP exam.
"""


# Menu definitions
class Menu:
    #String file
    def stringy(self):
        exec(open("./stringy.py").read())
        print(self.options[1])
    #Numbers file
    def numy(self):
        exec(open("./stringy.py").read())
        print(self.options[2])
    #List file
    def listy(self):
        exec(open("./stringy.py").read())
        print(self.options[3])
    #Dictionary file
    def dicty(self):
        exec(open("./stringy.py").read())
        print(self.options[4])
    #Meun options and assoicated function calls
    options = {
        0: ["Exit", None],
        1: ["Strings", stringy],
        2: ["Numbers", numy],
        3: ["Lists", listy],
        4: ["Dictionary", dicty]
    }


# Menu control
def menu_control():
    menu: Menu = Menu()

    repeat: bool = True
    while repeat:
        # heading section
        print()
        print("=" * 25)
        print("Please Select An Option")
        print("=" * 25)

        # output menu options
        items = len(menu.options)
        for i in range(0, items):
            print(str(i) + ": " + menu.options.get(i)[0])

        # get choice
        choice = input("Select Option: ")

        # validation section
        try:  # protects/traps errors
            choice = int(choice)  # convert input to Integer                   
            if choice in menu.options:
                if menu.options.get(choice)[1] is None:  # 0 condition
                    return  # exit
                else:  # valid menu
                    menu.options.get(choice)[1](menu)  # call function
            else:
                raise IndexError()  # raise index error
        except ValueError:  # not a number error
            print("Not a Number, enter a number.", choice)
            repeat = True
        except IndexError:
            print("Out of Bounds. {0} doesn't exist.".format(choice))
            repeat = True


# start menu
menu_control()
