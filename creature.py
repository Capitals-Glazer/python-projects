class Creature:
    def __init__(self, name, species, owner):
        self.name = name
        self.species = species
        self.owner = owner
        self.hunger = 5
        self.happiness = 5
        self.energy = 5
        self.level = 1

    def feed(self):
        self.hunger = max(0, self.hunger - 1)
        self.energy += 1
        print(f"{self.name} devours a hearty meal!")

    def play(self):
        if self.energy > 0:
            self.happiness += 1
            self.energy -= 1
            print(f"{self.name} is playing joyfully!")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self):
        if self.energy >= 2 and self.hunger <= 4:
            self.level += 1
            self.energy -= 2
            self.hunger += 1
            print(f"{self.name} trained hard and reached level {self.level}!")
        else:
            print(f"{self.name} needs rest or food before training.")

    def rest(self):
        self.energy = min(5, self.energy + 2)
        print(f"{self.name} takes a nap and regains energy.")

    def status(self):
        print(f"""🧝 {self.name} the {self.species} Owner: {self.owner}
               Level: {self.level} Hunger: {self.hunger} | 
               Happiness: {self.happiness} | Energy: {self.energy}""")
        
    def whip(self):
        if (self.happiness > 0):
            print(f"{self.name} is whipped!")
            self.happiness -=1
        else:
            print(f"{self.name} dies from excessive whipping")
        

# Game loop
name = input("Name your creature: ")
species = input("What species is it? (e.g., dragon, goblin, cat) ")
owner = input("Who is the owner? ")
creature = Creature(name, species, owner)

while True:
    
    creature.status()
    action = input("Choose an action: [feed], [play], [train], [rest], [whip] or [quit]: ").lower()

    if action == "feed":
        creature.feed()
    elif action == "play":
        creature.play()
    elif action == "train":
        creature.train()
    elif action == "rest":
        creature.rest()
    elif action == "whip":
        if creature.happiness <= 0 or creature.hunger <= 0:
            creature.whip()
            print("Goodbye adventurer.")
            break
        creature.whip()
        
        
    elif action == "quit":
        print("Goodbye adventurer.")
        break
    else:
        print("Invalid action.")