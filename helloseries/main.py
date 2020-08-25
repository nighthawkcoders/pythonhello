"""
  Assignment 1: Extend 5 things with stringy
  1. make a sentence with punctuation
  2. manipulate the sentence
  3. make other words or phrases from sentence
  4. ... you pick ...
  5. ... you pick ...
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
