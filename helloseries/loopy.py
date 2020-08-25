"""
 * Creator: Nighthawk Coding Society
 * Mini Lab Name: Hello Series, featuring Monkey Jumpers
 * Level: Medium
 *
 * Exploration Ideas
 * 1. Build more or entire rhyme for the "Monkey Jumpers" countdown poem
 * 2. Add names or other properties to the monkeys
 * 3. Print these monkeys horizontally
 *
 * Learning Considerations
 * Note: Loopy (Imperative Programming Style)
 * Project Focus: Animated Monkey Jumpers
 * A. Observe variable assignments
 * B. Study loops and zero based counting
 * C. Study two-dimensional (2D) arrays
 * D. Learn about and describe Imperative and Procedural Programming
 * E. Build a class diagram on a monkey as an object versus two-dimensional array
"""


print("Hello Series: loopy.py")  # identification message

# 2D array data assignment
monkeys = [
    [
        "ʕง ͠° ͟ل͜ ͡°)ʔ ",  # [0][0] eyes
        "  \\_⏄_/  ",  # [0][1] chin
        "  --0--   ",  # [0][2] body
        "  ⎛   ⎞   "  # [0][3] legs
    ],
    [
        " ʕ༼ ◕_◕ ༽ʔ ",  # [1][0]
        "  \\_⎏_/  ",
        "  ++1++  ",
        "   ⌋ ⌊   "
    ],
    [
        " ʕ(▀ ⍡ ▀)ʔ",  # [2][0]
        "  \\_⎐_/ ",
        "  <-2->  ",
        "  〈  〉 "
    ],
    [
        "ʕ ͡° ͜ʖ ° ͡ʔ",  # [3][0]
        "  \\_⍾_/  ",
        "  ==3==  ",
        "  _/ \\_  "
    ],
    [
        "  (◕‿◕✿) ",  # [4][0]
        "  \\_⍾_/ ",  # [4][1]
        "  ==4==  ",  # [4][2]
        "  _/ \\_ "  # [4][3]
    ]
]

""" 2D array program logic """
# cycles through 2D array backwards
for i in range(len(monkeys), -1, -1):
    # this print statement shows current count of Monkeys
    # concatenation (+) of the loop variable and string to form a countdown message
    print(str(i) + " little monkeys jumping on the bed...")

    # cycle through monkeys that are left in poem countdown
    for row in range(i-1,-1,-1):  # cycles through remaining monkeys in countdown

        # cycles through monkey part by part
        for col in range(len(monkeys[row])):
            # prints specific part of the monkey from the 2D cell
            print(monkeys[row][col] + " ")

        # this new line gives separation between stanza of poem
        print()

# out of all the loops, prints finishing messages
print("No more monkeys jumping on the bed")
print("0000000000000000000000000000000000")
print("             THE END              ")
