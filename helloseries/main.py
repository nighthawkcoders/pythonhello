"""
  Assignment 1: Extend 5 things with stringy
  1. make a sentence with punctuation
  2. manipulate the sentence
  3. make other words or phrases from sentence
  4. ... you pick ...
  5. ... you pick ...
"""
# Menu names
menu_choices = ["Exit", "Strings", "Numbers", "Lists", "Dictionaries"]


# Menu definitions
class Menu:

    def stringy(self):
        # run stringy.py file
        print(menu_choices[1])
        exec(open("./stringy.py").read())

    def numy(self):
        print(menu_choices[2])

    def listy(self):
        print(menu_choices[3])

    def dicty(self):
        print(menu_choices[4])

    options = {
        0: [menu_choices[0], None],
        1: [menu_choices[1], stringy],
        2: [menu_choices[2], numy],
        3: [menu_choices[3], listy],
        4: [menu_choices[4], dicty]
    }


# Menu control
def menu_control():
    menu = Menu()

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
