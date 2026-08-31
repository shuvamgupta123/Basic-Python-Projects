import random
quit = "y"

def near(guess):
    if guess< randomNumber - 30:
        print("Too low")
    elif guess> randomNumber+30:
        print("Too high")

while quit != "n":
    print("")
    randomNumber = random.randint(1,500)
    guess = 0
    tries = 0
    while guess != randomNumber:
        print(f"Attempts: {tries}")
        guess = int(input("Enter your guess:\n"))
        tries += 1
        print("")
        if guess < randomNumber:
            near(guess)
            print("Go higher")
        elif guess> randomNumber:
            near(guess)
            print("Go lower")
        else:
            break

    print("")
    print(f"You won, the correct no. was {randomNumber}")
    print(f"No. of attempts: {tries}")
    quit = input("Do you want to play again(Y/n)?").lower()
    print("")


    #this game was something i enjoyed making