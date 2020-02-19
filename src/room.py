# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, action):
        self.name = name
        self.action = action
    
    def __str__(self):
        return self.name

    def entered(self):
        output = f'You entered {self.name} and {self.action}'
        return output