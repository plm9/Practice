
print("Choose between 'r' 'p' 's'")


while True:
    user1=input("Player 1:")
    user2=input("Player 2:")

    if user1=="r":
        if user2=="p":
            print("Player 2 wins!")
            break
        elif user2=="s":
            print("Player 1 wins!")
            break
        else:
            print("Try again!")
    elif user1=="p":
        if user2=="r":
            print("Player 1 wins!")
            break
        elif user2=="s":
            print("Player 2 wins!")
            break
        else:
            print("Try again!")
    elif user1=="s":
        if user2=="r":
            print("Player 2 wins!")
            break
        elif user2=="p":
            print("Player 1 wins!")
            break
        else:
            print("Try again!")