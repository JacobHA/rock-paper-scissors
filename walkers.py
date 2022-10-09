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
    def __init__(name=None, max_x=100, max_y=100, BCs=None):
        assert name is not None, "Walker must have a name"
        self.name = name
        if name == "Rock":
            self.type = Rock()
        elif name == "Paper":
            self.type = Paper()
        elif name == "Scissors":
            self.type = Scissors()
        else:
            raise ValueError("Walker must be Rock, Paper, or Scissors")

        self.place()
        if BCs is None:
            self.BCs = "reflective"
        else:
            self.BCs = BCs
        
        
    def __str__(self):
        return f'{self.name} Random Walker'
    
    @property

    def place(self):
        self.x = random.randint(0, max_x)
        self.y = random.randint(0, max_y)

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        if self.BCs == "reflective":
            self.x = max(0, self.x)
            self.y = max(0, self.y)
            self.x = min(max_x, self.x)
            self.y = min(max_y, self.y)

        if self.BCs == "periodic":
            self.x = self.x % max_x
            self.y = self.y % max_y
        
    def interact(self, other):
        if self.type.beats == other.type.name:
            # self wins, destroy other
            other.destroy()
            return self
        elif self.type.loses_to == other.type.name:
            # other wins, destroy self
            self.destroy()
            return other
        else:
            return None

    def destroy(self):
        if self.repopulate:
            self.place()
        else:
            self.x = None
            self.y = None

