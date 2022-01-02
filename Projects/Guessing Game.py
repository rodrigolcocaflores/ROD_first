#import random library
import random

n = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY! OK? Thanks")

#create a list to store guesses
guesses = [0]

#ask valid guess
while True:
    guess = int(input("Give me a number between 1 and 100.\n What is your guess? "))

    if guess < 1 or guess > 100:
        print('WRONG! try again: ')
        continue

    break

#compare guess to our number
while True:
    guess = int(input("Give me a number between 1 and 100.\n What is your guess?"))

    if guess < 1 or guess > 100:
        print('WRONG! try again: ')
        continue

    #compare player's guess
    if guess == n:
        print(f'Good job!it only took you {len(guesses)} guesses.')
        break

    #if wrong, add it to the list
    guesses.append(guess)

    #First guess, guesses[-2]==0, which is False and brings us down to second section
    if guesses[-2]:
        if abs(n-guess) < abs(n-guesses[-2]):
            print ('Warmer.')
        else:
            print ('Colder.')
    else:
        if abs(n-guess) <= 10:
            print('Warm.')
        else:
            print('Cold.')
