
nunber=int(input("Lets see your number:"))

if nunber%2==0:
    print("Your number is even!")
else:
    print("Your number is odd!")

""" First extra"""
if nunber%4==0:
    print("Your number is multiple of 4!")
else:
    print("Your number is not a multiple of 4!")

""" Second extra"""
num=int(input("Give me now again a number"))
check=int(input("and another one"))

if num%check==0:
    print("Your numbers devide evenly! ")
else:
    print("Your numbers don't devide evenly! ")