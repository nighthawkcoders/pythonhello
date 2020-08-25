"""
Playground code for Python strings

A string is a collection of one or more characters.

Strings can be put in a single quote, double-quote or triple quote.

Strings are arrays of bytes representing Unicode characters.

Assignment, add 5 things
  1. make a sentence with punctuation
  2. manipulate the sentence
  3. make other words or phrases from sentence
  4. ... you pick ...
  5. ... you pick ...

Explore online tutorials
https://www.geeksforgeeks.org/python-strings/?ref=lbp
"""

# Ouput message
print("Hello, World!")  # message in quotes is a string
print("Hello Series: stringy.py")  # identification message
print()  # blank line

# Using a scalar variable
hello = "Hello Python!"  # variable assignment, put string in variable
print(hello)  # print variable
print()

# Slicing a variable
print(hello + " (slicing)")  # concatenation
print(hello[1])  # this is second character in zero base counting
print("Hello Python!"[1])  # this is same thing without variable
print()

# slicing has n, n:n, n:n:step
print(hello + " (slicing continued)")
print(hello[0:2])  # 0 starts at left
print(hello[-len(hello):2])  # (-)counts from the right
print(hello[-4:len(hello)])  # count -4 from right and go to the end
print(hello[0:len(hello):2])  # every other character
print(hello[::2])  # shorthand for every other character
print(hello[::-1])  # third parameter lets you step
print()

# slicing and concatenation, to make a word out of the words
print(hello + " (slicing and concatenation)")
print(hello[6] + hello[4] + hello[2:4])
print()

# a string "hello" is a class, a class has methods, here we split by space to new variable
print(hello + " (split)")
hello2 = hello.split()  # a new varialbe is formed
print(hello2)  # hello2 is a list
print(hello2[0])  # first word, zero based counting
print(hello2[1])  # second word
print(hello2[1] + " " + hello2[0])  # words backwords
print(hello2[1][0] + " " + hello2[0][0])
print()

print(hello + """ ("quotes") """)  # using triple quotes to put quotes in message
hello3 = hello.split()
hello3.append("""("quotes")""")  # append method adds to the list of words
print(hello3)
print(len(hello3[0]))  # length of word
print(len(hello3))  # length of list
hello3.sort()
print(hello3)  # sort list
print()

monkey1a = "ʕ༼ ◕_◕ ༽ʔ" + "\n" + \
           "  \\_⎏_/ " + "\n" + \
           "  ++1++ " + "\n" + \
           "   ⌋ ⌊  "
monkey1b = "ʕ༼ ◕_◕ ༽ʔ" + "\n" + \
           "  \\___/ " + "\n" + \
           "  +++++ " + "\n" + \
           "   ⌋ ⌊  "
print(monkey1a)
print(monkey1b)
print()

monkey2a = "ʕ(▀ ⍡ ▀)ʔ" + "\n" + \
           "  \\___/ " + "\n" + \
           "  <-2-> " + "\n" + \
           "  〈  〉 "
monkey2b = "ʕ(▀ ⍡ ▀)ʔ" + "\n" + \
           "  \\_⎐_/ " + "\n" + \
           "  <--->  " + "\n" + \
           "   ⌋  ⌊  "
print(monkey2a)
print(monkey2b)
print()

monkey3a = " ʕ ͡° ͜ʖ ° ͡ʔ " + "\n" + \
           "  \\___/" + "\n" + \
           "   ==3== " + "\n" + \
           "   _/ \\_"
monkey3b = " ʕ ͡° ͜ʖ ° ͡ʔ " + "\n" + \
           "  \\_⎐_/ " + "\n" + \
           "   ===== " + "\n" + \
           "   _/ \\_"

print(monkey3a)
print(monkey3b)
print()

monkey4a = "ʕง ͠° ͟ل͜ ͡°)ʔ " + "\n" + \
           "  \\___/" + "\n" + \
           "  --4--  " + "\n" + \
           "  ⎛   ⎞  "
monkey4b = "ʕง ͠° ͟ل͜ ͡°)ʔ "+ "\n" + \
           "  \\_⎐_/ " + "\n" + \
           "  -----  " + "\n" + \
           "  ⌋   ⌊ "

print(monkey4a)
print(monkey4b)
print()
