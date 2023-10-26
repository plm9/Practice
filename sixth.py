

palindrome=input("What's your word:")


frsthlv=palindrome[:len(palindrome)//2]
scndhlv=palindrome[:len(palindrome)//2-1:-1]

if frsthlv==scndhlv:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")