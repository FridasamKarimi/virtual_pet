class Pet:
    """A virtual pet that can eat, sleep, play, and learn tricks."""
    def __init__(self, name):
        """Initializing a new pet with given name and default stats."""
        self.name = name
        self.hunger = 5 # Range: 0 (full) to 10 (starving)
        self.energy = 5 # Range: 0 (exhausted) to 10 (energized)
        self.happiness = 5 # Range: 0 (miserable) to 10 (elated)
        self.tricks = [] # List of tricks the pet knows
    
    def _adjust_attribute(self, attr, change, min_val=0, max_val=10):
        """adjust attributes   attr (str): Attribute to modify ('hunger', 'energy', 'happiness')
            change (int): Amount to add/subtract from attribute
            min_val (int): Minimum allowed value (default 0)
            max_val (int): Maximum allowed value (default 10)
        """
        current = getattr(self, attr)
        setattr(self, attr, max(min_val, min(max_val, current + change)))
    
    def eat(self):
        
        self._adjust_attribute('hunger', -3) # Reduce hunger
        self._adjust_attribute('happiness', 1) # Eating makes pet happy
        print(f"{self.name} says YUM!")
    
    def sleep(self):
        self._adjust_attribute('energy', 5)
        print(f"{self.name} time to catch some zzzZZZ...") # Big energy boost
    
    def play(self):
        if self.energy >= 2:
            self._adjust_attribute('energy', -2) # Playing is tiring
            self._adjust_attribute('happiness', 2) # Playing is fun
            self._adjust_attribute('hunger', 1) # Playing burns calories
            print(f"{self.name} plays ;moving up and down, and all over the place!")
        else:
            print(f"{self.name} is too tired to play")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        # Create visual bars for each attribute
        for attr in ['hunger', 'energy', 'happiness']:
            value = getattr(self, attr)
             # Filled squares represent current level, empty squares show remaining capacity
            print(f"{attr.capitalize()}: {'▮' * value}{'▯' * (10 - value)} {value}/10")
    
    # Training day
    def train(self, trick):
         # Case-insensitive comparison to avoid duplicates like "Sit" vs "sit"
        if trick.lower() in [t.lower() for t in self.tricks]:
            print(f"{self.name} already knows '{trick}'!")
        else:
            self.tricks.append(trick)
            self._adjust_attribute('happiness', 1) # Learning is rewarding
            print(f"{self.name} learned '{trick}'! Good job!")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")



