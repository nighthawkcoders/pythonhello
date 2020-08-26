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
* A Java utility Class that supports entry point for execution
"""

# Dictionary Tags defined as scalars
head = "head"
chin = "chin"


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
    def get_anime(self, index):
        return self.anime[index]


class Classy:
    # Constructor occurs when Classy is created
    def __init__(self):
        # Classy builds and contains Monkey List
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

    def count(self):
        return len(self.Monkeys)

    def get_monkeys(self):
        return self.Monkeys

    def get_monkey(self, i):
        return self.Monkeys[i]

    def print_anime_monkeys(self):
        import time
        count = 0

        for i in range(10):
            print("\033[H\033[2J")
            index = count % 2
            for part in self.part_list:
                for monkey in self.Monkeys:
                    print(monkey.get_anime(index)[part], end="\t")
                print()

            time.sleep(1)
            count += 1

    def print_animes(self):
        monkeys = self.Monkeys
        for monkey in monkeys:
            print(monkey.anime)
        print()
