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
head = "head"
chin = "chin"
body = "body"
legs = "legs"


class Classy:
    # initialize database
    def __init__(self):

        self.MonkeyDb = []
        self.group = 0
        self.MonkeyDb.append({self.group: {
            head:"ʕ༼ ◕_◕ ༽ʔ",
            chin:"  \\_⎏_/ ",
            body:"  ++1++ ",
            legs:"   ⌋ ⌊  "
        }})
        self.MonkeyDb.append({self.group: {
            head:"ʕ༼ ◕_◕ ༽ʔ",
            chin:"  \\___/ ",
            body:"  +++++ ",
            legs:"  〈  〉 "
        }})

        self.group += 1
        self.MonkeyDb.append({self.group: {
            head:"ʕ(▀ ⍡ ▀)ʔ",
            chin:"  \\___/ ",
            body:"  <-2-> ",
            legs:"  〈  〉 "
        }})
        self.MonkeyDb.append({self.group: {
            head:"ʕ(▀ ⍡ ▀)ʔ",
            chin:"  \\_⎐_/ ",
            body:"  <--->  ",
            legs:"   ⌋  ⌊  "
        }})

        self.group += 1
        self.MonkeyDb.append({self.group: {
            head:" ʕ ͡° ͜ʖ ° ͡ʔ ",
            chin:"   \\___/",
            body:"   ==3== ",
            legs:"   _/ \\_"
        }})
        self.MonkeyDb.append({self.group: {
            head:" ʕ ͡° ͜ʖ ° ͡ʔ ",
            chin:"   \\_⍾_/ ",
            body:"   ===== ",
            legs:"   〈  〉 "
        }})

        self.group += 1
        self.MonkeyDb.append({self.group: {
            head:" ʕ(◕‿◕✿)ʔ ",
            chin:"   \\_⍾_/ ",
            body:"   ==4==  ",
            legs:"   _/ \\_  "
        }})
        self.MonkeyDb.append({self.group: {
            head:" ʕ(◕‿◕✿)ʔ ",
            chin:"   \\___/  ",
            body:"   =====  ",
            legs:"   〈  〉  "
        }})

        self.group += 1


    def count(self):
        return self.group

    def get_animes(self, index):
        result_db = []
        for record in self.MonkeyDb:
            if index in record:
                result_db.append(record)
        return result_db


monkeys: Classy = Classy()
for i in range(monkeys.count()):
    print(monkeys.get_animes(i))




