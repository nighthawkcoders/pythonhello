
menu_choices = ["Exit", "Strings", "Numbers", "Lists","Dictionaries"]

class Selections(object):
    """
    Assignment 1: do 5 things with stringy
    1. make a sentence with punctuation
    2. manipulate the sentence
    3. make other words or phrases from sentence
    4. ... you pick ...
    5. ... you pick ...
    """
    def stringy(self):
        #run stringy.py file
        print(menu_choices[1])
        exec(open("./stringy.py").read())

    def numy(self):
        print(menu_choices[2])

    def listy(self):
        print(menu_choices[3])

    def dicty(self):
        print(menu_choices[4])

def menu():
    funcs = Selections()
    options = {
        0: [menu_choices[0], funcs],
        1: [menu_choices[1], funcs.stringy],
        2: [menu_choices[2], funcs.numy],
        3: [menu_choices[3], funcs.listy],
        4: [menu_choices[4], funcs.dicty]
    }
    repeat: bool = True
    while repeat:
        #heading section
        print()
        print("=" * 25)
        print("Please Select An Option")
        print("=" * 25)

        #output menu options
        items = len(options)
        for i in range(0, items):
            print(str(i) + ": " + options.get(i)[0])

        #get choice
        choice = input("Select Option: ")

        #validation section
        try:                                #protects/traps errors
            choice = int(choice)
            if choice == 0:
                return                      #exit function
            elif choice in options:
                options.get(choice)[1]()    #call function from list
            else:
                raise IndexError()          #raise error
        except ValueError:                  #not a number error
            print("Not a Number, you need to enter a number.", choice)
            repeat = True
        except IndexError:
            print("Out of Bounds. Option {0} doesn't exist.".format(choice))
            repeat = True


#start the display
menu()