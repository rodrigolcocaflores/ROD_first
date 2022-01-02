import random

n = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY! OK? Thanks")

guesses = [0]
while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n What is your guess?"))
    if guess < 1 or guess > 100:
        print('Oh no! Please try again: ')
        continue
    break