class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 10
        self.energy = 10
        self.happiness = 10
        self.tricks = []
    
    def eat(self):

        self.hunger = max(0, self.hunger -3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):

        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger +1)

    def get_status(self):
        """Prints the current state of the pet"""
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        """Teaches the pet a new trick if not already known"""
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned {trick}!")
        else:
            print(f"{self.name} already knows {trick}!")

    def show_tricks(self):
        """Prints all learned tricks"""
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")