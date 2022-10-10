import random
import numpy as np

class Rock:
    def __init__(self):
        self.name = "Rock"
        self.beats = "Scissors"
        self.loses_to = "Paper"

    def __str__(self):
        return self.name

class Paper:
    def __init__(self):
        self.name = "Paper"
        self.beats = "Rock"
        self.loses_to = "Scissors"

    def __str__(self):
        return self.name

class Scissors:
    def __init__(self):
        self.name = "Scissors"
        self.beats = "Paper"
        self.loses_to = "Rock"

    def __str__(self):
        return self.name

class Walker:
    def __init__(self, name=None, max_x=100, max_y=100, BCs=None, repopulate=False):
        assert name is not None, "Walker must have a player type, e.g. rock, paper, or scissors"

        if name == "Rock":
            self.player = Rock()
        elif name == "Paper":
            self.player = Paper()
        elif name == "Scissors":
            self.player = Scissors()
        else:
            raise ValueError("Walker must be Rock, Paper, or Scissors")

        if BCs is None:
            self.BCs = "reflective"
        else:
            self.BCs = BCs
        
        self.repopulate = repopulate
        self.max_x = max_x
        self.max_y = max_y

        self.place()


    def __str__(self):
        return f'{self.name} Random Walker'
    
    def place(self):
        self.x = random.uniform(0, self.max_x)
        self.y = random.uniform(0, self.max_y)
        print("Placed", self.player.name, "at", self.x, self.y)
        
    def move(self):
        self.x += random.uniform(-1/4, 1/4)
        self.y += random.uniform(-1/4, 1/4)

        if self.BCs == "reflective":
            self.x = max(0, self.x)
            self.y = max(0, self.y)
            self.x = min(self.max_x, self.x)
            self.y = min(self.max_y, self.y)

        if self.BCs == "periodic":
            self.x = self.x % self.max_x
            self.y = self.y % self.max_y
        
    def nearby(self, other):
        # calculate distance between self and other
        dx = self.x - other.x
        dy = self.y - other.y
        distance = np.sqrt(dx**2 + dy**2)

        if distance < 6:
            return True
        else:
            return False


    def interact(self, other):
        # Check if the other walker is in the same place
        if self.nearby(other):
            
            if self.player.beats == other.player.name:
                # self wins, change other
                other.outcome(self.player.name)
                

            elif self.player.loses_to == other.player.name:
                # other wins, destroy self
                self.outcome(other.player.name)
                

            else:
                # self and other are the same type, continue
                pass

    def outcome(self, name):
        if self.repopulate:
            self.place()
        else:
            if name == "Rock":
                self.player = Rock()
            elif name == "Paper":
                self.player = Paper()
            elif name == "Scissors":
                self.player = Scissors()
            # self.player = name
            # self.x = None
            # self.y = None

