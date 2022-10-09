import random

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
        self.x = random.randint(0, self.max_x)
        self.y = random.randint(0, self.max_y)

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        if self.BCs == "reflective":
            self.x = max(0, self.x)
            self.y = max(0, self.y)
            self.x = min(self.max_x, self.x)
            self.y = min(self.max_y, self.y)

        if self.BCs == "periodic":
            self.x = self.x % self.max_x
            self.y = self.y % self.max_y
        
    def interact(self, other):
        # Check if the other walker is in the same place
        if (self.x == other.x and self.y == other.y):
            
            if self.player.beats == other.player.name:
                # self wins, destroy other
                other.destroy()
                return self

            elif self.player.loses_to == other.player.name:
                # other wins, destroy self
                self.destroy()
                return other

            else:
                # self and other are the same type, continue
                return None

    def destroy(self):
        if self.repopulate:
            self.place()
        else:
            self.x = None
            self.y = None

