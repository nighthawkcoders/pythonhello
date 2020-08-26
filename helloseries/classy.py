"""
* Creator: Nighthawk Coding Society
* Mini Lab Name: Hello Series, featuring Monkey Jumpers
* Level: Medium
*
* Exploration Ideas
* 1. Add names or other properties to the monkeys
* 2. Add the poem
* 3. Experiment with animation
* 4. Build a project with your own ascii/unicode art or logo
*
* Learning Considerations
* Note: Classy (OOP Programming Style)
* Project Focus: Animated Monkey Jumpers
* A. Observe logic for print Monkey in row
* B. Learn about constructors
* C. Observe about an object and list of objects
"""

print("Hello Series: classy.py")  # identification message

"""
* A Python Class that supports entry point for creating object and methods execution
"""


class Classy:
    # Constructor occurs when Classy is created
    def __init__(self):
        # Classy contains Monkey List
        self.Monkeys = []
        # Define Diction tags
        self.head = "head"
        self.chin = "chin"
        self.body = "body"
        self.legs = "legs"
        self.part_list = [self.head, self.chin, self.body, self.legs]

        # Monkey 0
        self.Monkeys.append(
            Monkey(
                self.part_list,  # initialize monkey parts
                "ʕ༼ ◕_◕ ༽ʔ",
                "  \\_⎏_/ ",
                "  ++1++ ",
                "   ⌋ ⌊  "
            )
        )
        self.Monkeys[0].add_anime(
                "ʕ༼ ◕_◕ ༽ʔ",
                "  \\_⎏_/ ",
                "  ++1++ ",
                "   ⌋ ⌊  "
        )
        # Monkey 1
        self.Monkeys.append(
            Monkey(
                self.part_list,
                "ʕ(▀ ⍡ ▀)ʔ",
                "  \\___/ ",
                "  <-2-> ",
                "  〈  〉 "
            )
        )
        self.Monkeys[1].add_anime(
                "ʕ(▀ ⍡ ▀)ʔ",
                "  \\_⎐_/ ",
                "  <--->  ",
                "   ⌋  ⌊  "
        )
        # Monkey 2
        self.Monkeys.append(
            Monkey(
                self.part_list,
                " ʕ ͡° ͜ʖ ° ͡ʔ ",
                "   \\___/",
                "   ==3== ",
                "   _/ \\_"
            )
        )
        self.Monkeys[2].add_anime(
                " ʕ ͡° ͜ʖ ° ͡ʔ ",
                "   \\_⍾_/ ",
                "   ===== ",
                "   〈  〉 "
        )
        # Monkey 3
        self.Monkeys.append(
            Monkey(
                self.part_list,
                " ʕ( ◕‿◕✿)ʔ ",
                "   \\_⍾_/ ",
                "   ==4==  ",
                "   _/ \\_  "
            )
        )
        self.Monkeys[3].add_anime(
                " ʕ(◕‿◕✿)ʔ ",
                "   \\___/  ",
                "   =====  ",
                "   〈  〉  "
        )

    # count of monkeys
    def count(self):
        return len(self.Monkeys)

    # getter for monkey list
    def get_monkeys(self):
        return self.Monkeys

    # getter for specific monkey in list
    def get_monkey(self, i):
        return self.Monkeys[i]

    # getter for monkey part list
    def get_monkey_parts(self):
        return self.part_list

    # monkey animation print
    def print_monkeys(self):
        import time
        counter = 0

        # 10 seconds of print
        for i in range(10):
            print("\033[H\033[2J")

            # horizontal print is monkey part 1st
            for part in self.get_monkey_parts():

                # cycle through same parts
                for monkey in self.get_monkeys():
                    index = counter % monkey.get_animations()
                    print(monkey.get_part(index, part), end="\t")
                print()

            time.sleep(1)
            counter += 1


"""
* A Python Class that maintains data for a Monkey object
"""


class Monkey:
    # initialize database
    def __init__(self, part_names, head, chin, body, legs):
        # Database of monkey parts
        self.head = part_names[0]
        self.chin = part_names[1]
        self.body = part_names[2]
        self.legs = part_names[3]
        self.anime = []
        self.add_anime(head, chin, body, legs)

    # add body parts for animation
    def add_anime(self, head, chin, body, legs):
        self.anime.append({self.head: head, self.chin: chin, self.body: body, self.legs: legs})

    # get animation for monkey
    def get_animations(self):
        return len(self.anime)

    # get animation for monkey
    def get_anime(self, index):
        return self.anime[index]

    # get monkey part
    def get_part(self, index, part):
        return self.get_anime(index)[part]
