bidder={}
name = ""
benchmarkamt = 0
quit = "y"
while quit == "y":
    a = input("What is bidder's name?")
    b = input("What is the bid amount?")
    bidder[a] = b
    quit = input("Any other bidder(Y/n)?").lower()
    print("\n"*50)

for i in bidder:
    if int(bidder[i]) > benchmarkamt:
        name = i
        benchmarkamt = int(bidder[i])

print(f"{name} won the bidding with the highest bid of {benchmarkamt}")
