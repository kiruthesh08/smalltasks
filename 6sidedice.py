import random

class Die:
    """Class for creating and rolling a 6-sided die."""
    
    def __init__(self):
        self.value = 1
        """Creates a new die object, with value 1 facing up"""

    def getValue(self):  # Corrected method name to 'getValue'
        return self.value

    def roll(self):
        self.value = random.randint(1, 6)

amount = int(input("Please enter the number of throws: "))

d = Die()

print(d.getValue())  # Initial value before rolling

for _ in range(amount):
    d.roll()
    print("Result of the roll:", d.getValue())
