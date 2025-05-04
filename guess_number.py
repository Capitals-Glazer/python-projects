import random

secret_number = random.randint(1, 100)
guess = 0
x = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while guess != secret_number:
    guess = int(input("Your guess: "))
    x+=1
    if guess < secret_number:
        print("Too low! Try Again.")
    elif guess > secret_number:
        print("Too high! Try Again.")

    if (x > 5):
        print("game over dummy")

    

    



print(f"Congratulations! You guessed it in {x} tries.")