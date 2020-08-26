"""
* Creator: Nighthawk Coding Society
* Mini Lab Name: Hello Series, featuring Monkey Jumpers
* Level: Medium
*
* Exploration Ideas
* 1. Add methods or logic to print monkeys vertically
* 2. Add names or other properties to the monkeys
* 3. Add to poem, ie animation of monkey breaking head
* 4. Build a project with your own ascii/unicode art or logo, experiment with animation
* 5. Learn to deploy your Java class or JAR to run animation from shell (deployed java).  FYI, the shell has properties (character sequences ) to clear and improve animation.
*
* Learning Considerations
* Note: Classy (OOP Programming Style)
* Project Focus: Animated Monkey Jumpers
* A. Observe logic for 5 to 1 monkey in countdown and timer
* B. Learn about constructors
* C. Learn about an object and list of objects
* D. Learn about HashMap (Name-Value pairs)
* E. Learn about StringBuilder
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
        self.anime.append({n1: head, n2: chin, n3: body, n4: legs})
        self.head = head
        self.chin = chin
        self.body = body
        self.legs = legs

    def add_anime(self, head, chin, body, legs):
        self.anime.append({n1: head, n2: chin, n3: body, n4: legs})

    def get_anime(self):
        return self.anime

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
        self.Monkeys.append(
            Monkey(
                "ʕ(▀ ⍡ ▀)ʔ",
                "  \\___/ ",
                "  <-2-> ",
                "  〈  〉 "
            )
        )

        self.Monkeys.append(
            Monkey(
                " ʕ ͡° ͜ʖ ° ͡ʔ ",
                "   \\___/",
                "   ==3== ",
                "   _/ \\_"
            )
        )

        self.Monkeys.append(
            Monkey(
                " ʕ( ◕‿◕✿)ʔ ",
                "   \\_⍾_/ ",
                "   ==4==  ",
                "   _/ \\_  "
            )
        )

        """
        self.Monkeys.append(
            Monkey(  # initialize monkey parts
                "ʕ༼ ◕_◕ ༽ʔ",
                "  \\_⎏_/ ",
                "  ++1++ ",
                "   ⌋ ⌊  "
            ).add_anime(  # add alternate part for animation
                "ʕ༼ ◕_◕ ༽ʔ",
                "  \\_⎏_/ ",
                "  ++1++ ",
                "   ⌋ ⌊  "
            )
        )
        # Monkey 1
        self.Monkeys.append(
            Monkey(
                "ʕ(▀ ⍡ ▀)ʔ",
                "  \\___/ ",
                "  <-2-> ",
                "  〈  〉 "
            ).add_anime(
                "ʕ(▀ ⍡ ▀)ʔ",
                "  \\_⎐_/ ",
                "  <--->  ",
                "   ⌋  ⌊  "
            )
        )
        # Monkey 2
        self.Monkeys.append(
            Monkey(
                " ʕ ͡° ͜ʖ ° ͡ʔ ",
                "   \\___/",
                "   ==3== ",
                "   _/ \\_"
            ).add_anime(
                " ʕ ͡° ͜ʖ ° ͡ʔ ",
                "   \\_⍾_/ ",
                "   ===== ",
                "   〈  〉 "
            )
        )
        # Monkey 3
        self.Monkeys.append(
            Monkey(
                " ʕ(◕‿◕✿)ʔ ",
                "   \\_⍾_/ ",
                "   ==4==  ",
                "   _/ \\_  "
            ).add_anime(
                " ʕ(◕‿◕✿)ʔ ",
                "   \\___/  ",
                "   =====  ",
                "   〈  〉  "
            )
        )
        """

    def count(self):
        return len(self.Monkeys)

    def get_monkeys(self):
        return self.Monkeys

    def get_monkey(self, i):
        return self.Monkeys[i]

    def print_monkeys(self):
        monkeys = self.Monkeys
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


classy: Classy = Classy()
classy.print_monkeys()
