import random

words = ["hello", "meow"]

while quit != "y":
    quit = "n"
    lives = 5
    spaces =[]
    guessLetter = ""
    randWord = random.choice(words)

    print("Welcome")
    print("You have 5 lives to guess the word")
    print("")

    for i in range(len(randWord)):
        spaces.append("_")

    while lives > 0:
        print(" ".join(spaces))
        guessLetter = input("Guess a letter:")
         
        if guessLetter in spaces:
            print("You have already guessed this letter")
        else:
            for i in range(len(randWord)):
                if guessLetter == randWord[i]:
                    spaces[i] = guessLetter
            if guessLetter not in spaces:
                lives -= 1
                print("Your guess in incorrect")
                print("you have " + str(lives) + " lives left")

        if "_" not in spaces:
            print("hurray! you won.")
            break

    if "_"  in spaces:
        print("You lose!")     
        

    quit = input("Do you want to quit(Y/n)?").lower()