import random
quit = "y"
while quit != "n":
    print("")
    randomNumber = random.randint(1,1000)
    guess = 0
    tries = 0
    while guess != randomNumber:
        print(f"Attempts: {tries}")
        guess = int(input("Enter your guess:\n"))
        tries += 1
        print("")
        if guess < randomNumber:
            print("Go higher")
        elif guess> randomNumber:
            print("Go lower")
        else:
            break
    print("")
    print(f"You won, the correct no. was {randomNumber}")
    print(f"No. of attempts: {tries}")
    quit = input("Do you want to play again(Y/n)?").lower()
    print("")