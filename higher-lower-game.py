from game_data import data
from higherLowerGameDisplayart import logo, vs
import random
from replit import clear

b = []
score = 0
game_over = False
def random_account():
    global b
    if len(b) == len(data):
        return "Won"
    a = random.choice(data)
    for i in b:
        if i == a:
            a = random.choice(data)
    b.append(a)
    return a

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

#makin the accout at position become the next account at position a

#clear the screen between rounds

choice_a = random_account()

while game_over == False:
    choice_b = random_account()
    print(logo)
    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Against B: {format_data(choice_b)}")
    input_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice_a["follower_count"] > choice_b["follower_count"]:
        correct_answer = "a"
        choice_a = choice_a
    else:
        correct_answer = "b"
        choice_a = choice_b
    clear()
    if input_guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}.")
