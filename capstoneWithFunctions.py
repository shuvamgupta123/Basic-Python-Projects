import random

play = input("Do you want to play Jack-Capestone 21(Y/n)?").upper()
Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def randomCards():
    return random.choices(Cards, k=2)

cardSet={
    "PlayerCards":randomCards(),
    "DealerCards":randomCards(),
}
lastCard = random.choice(Cards)

def inGame(play):
    if play == "Y":
        print(f"\nThe delear has suffeled the cards.")
        print(f"\nYou have {cardSet['PlayerCards']} numbered cards.")
        print(f"Dealer has [{cardSet['DealerCards'][0]}, *] numbered cards. ")
        thirdcard = input("\nDo you want to add an extra card(Y/n)?").upper()

        if thirdcard == "Y":
            cardSet['PlayerCards'].append(lastCard)
            print(f"You have {cardSet['PlayerCards']}")
            print(f"Dealer had {cardSet['DealerCards']}")
        else:
            print(f"You had {cardSet['PlayerCards']}")
            print(f"Dealer had {cardSet['DealerCards']}")
        
        a = sum(cardSet['PlayerCards'])
        b = sum(cardSet['DealerCards'])

        if a > b and a<=21:
            print(f"You won by {a-sum(cardSet['DealerCards'])} points.")
        elif a < b:
            print(f"You lose by {sum(cardSet['DealerCards'])-a} points.")
        elif a == b:
            print("Draw")
    else:
        print("Thank you for considering the game.")


inGame(play)