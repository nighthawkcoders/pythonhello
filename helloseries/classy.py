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
n1 = "head"
n2 = "chin"
n3 = "body"
n4 = "legs"


class Monkey:
    # initialize database
    def __init__(self, head, chin, body, legs):
        self.anime = []
        self.head = head
        self.chin = chin
        self.body = body
        self.legs = legs
        self.anime.append({n1: head, n2: chin, n3: body, n4: legs})

    def add_anime(self, head, chin, body, legs):
        self.anime.append({n1: head, n2: chin, n3: body, n4: legs})

    def get_anime(self, index):
        return self.anime[index]

    def get_head(self):
        return self.head

    def get_chin(self):
        return self.chin

    def get_body(self):
        return self.body

    def get_legs(self):
        return self.legs


class Classy:
    # Constructor occurs when Classy is created
    def __init__(self):
        # Classy builds and contains Monkey List
        self.Monkeys = []

        # Monkey 0
        self.Monkeys.append(
            Monkey(  # initialize monkey parts
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
        self.Monkeys.append(
            Monkey(
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
        monkeys = self.Monkeys
        count = 0
        for i in range(10):
            print("\033[H\033[2J")
            index = count % 2
            for monkey in monkeys:
                anime = monkey.get_anime(index)
                print(anime[n1], end="\t")
            print()

            for monkey in monkeys:
                anime = monkey.get_anime(index)
                print(anime[n2], end="\t")
            print()

            for monkey in monkeys:
                anime = monkey.get_anime(index)
                print(anime[n3], end="\t")
            print()

            for monkey in monkeys:
                anime = monkey.get_anime(index)
                print(anime[n4], end="\t")
            print()
            time.sleep(1)
            count += 1


    def print_monkeys(self):
        monkeys = self.Monkeys
        count = 0;

        for monkey in monkeys:
            print(monkey.head, end="\t")
        print()

        for monkey in monkeys:
            print(monkey.chin, end="\t")
        print()

        for monkey in monkeys:
            print(monkey.body, end="\t")
        print()

        for monkey in monkeys:
            print(monkey.legs, end="\t")
        print()

    def print_animes(self):
        monkeys = self.Monkeys
        for monkey in monkeys:
            print(monkey.anime)
        print()
