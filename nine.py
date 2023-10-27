import random 

number=random.randint(1,9)

tries=0
while True:
    guess=input("Guess a number between 1 and 9:")
    if guess=="exit":
        break
    else:
        guessint=int(guess)
        tries+=1
        if guessint > number:
            print("The number is lower")
        elif guessint < number:
            print("The number is higher")
        elif guessint==number:
            print(f"You found the number {number} with {tries} tries")
            break