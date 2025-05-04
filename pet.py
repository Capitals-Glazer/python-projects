class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.furry = True
        self.owner = owner;

    def feed(self):
        self.hunger = max(0, self.hunger - 1)
        print(f"{self.name} is eating.")

    def play(self):
        self.happiness += 1
        print(f"{self.name} is having fun!")

    def status(self):
        print(f"{self.name} | Owner: {self.owner} | Hunger: {self.hunger} | Happiness: {self.happiness}")

    def shave(self):
        
        print (f"{self.name} is shaved.")

# Game loop
pet = Pet(input("Name your pet: "), input("Name your pet's owner:"))
while True:
    pet.status()
    action = input("Do you want to [feed], [play], or [quit]? ").lower()
    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "quit":
        break     