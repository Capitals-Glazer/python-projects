import random
import time

inventory = []

def print_pause(message, delay=1.2):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You wake up in a dark, damp dungeon with a splitting headache.")
    print_pause("In front of you are two doors — one is made of old wood, the other of cold iron.")
    print_pause("You must choose...")

def choose_first_door():
    door = ""
    while door not in ["wood", "iron"]:
        door = input("Do you choose the wood or iron door? (wood/iron): ").lower()
    return door

def wood_path():
    print_pause("You push the creaky wooden door open and step inside.")
    print_pause("The room smells of herbs. You see a table with two items.")
    choice = ""
    while choice not in ["sword", "potion"]:
        choice = input("Do you take the sword or the potion? (sword/potion): ").lower()
    inventory.append(choice)
    print_pause(f"You pocket the {choice} and move on.")
    hallway()

def iron_path():
    print_pause("You shove open the heavy iron door and enter a dark hallway.")
    print_pause("Torches flicker as you step forward, your footsteps echoing.")
    event = random.choice(["trap", "friend"])
    if event == "trap":
        print_pause("Suddenly, a trap triggers! Arrows fly at you!")
        if "potion" in inventory:
            print_pause("You quickly drink the potion — it's a shield spell! You're safe.")
        else:
            print_pause("You're hit! Game over.")
            return
    else:
        print_pause("A cloaked figure appears and offers you a key.")
        inventory.append("key")
        print_pause("You thank them and keep moving.")
    hallway()

def hallway():
    print_pause("You arrive at a split: stairs up or a tunnel downward.")
    direction = ""
    while direction not in ["stairs", "tunnel"]:
        direction = input("Do you take the stairs or the tunnel? (stairs/tunnel): ").lower()
    if direction == "stairs":
        boss_room()
    else:
        tunnel_path()

def tunnel_path():
    print_pause("You crawl through the tight tunnel...")
    print_pause("...and find a sleeping dragon guarding a chest.")
    if "sword" in inventory:
        print_pause("You draw your sword and quietly slay the dragon.")
        print_pause("Inside the chest is the key to the exit!")
        inventory.append("key")
    else:
        print_pause("You try to sneak past but the dragon wakes and incinerates you.")
        return
    boss_room()
    print_pause("You find a door at the end of the tunnel.")
    print_pause("You use the key to unlock it...")

def boss_room():
    print_pause("You reach a grand chamber with a large door.")
    if "key" in inventory:
        print_pause("You use the key to open it...")
        print_pause("Sunlight floods in. You're free!")
        print("🎉 YOU WIN 🎉")
    else:
        print_pause("The door is locked. You bang on it in vain.")
        print_pause("Looks like you're stuck here... forever.")
        print("💀 GAME OVER 💀")

def play_game():
    global inventory
    inventory = []
    intro()
    door_choice = choose_first_door()
    if door_choice == "wood":
        wood_path()
    else:
        iron_path()

while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing. Watch your step in dark places...")
        break
    