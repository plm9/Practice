
import time
from datetime import date

name =input("What is your name:")
age=int(input("What is your age:"))

""" -today= date.today()["year"] """
today=date.fromtimestamp(time.time())

years100=100-age

print(name+f" you will be 100 years old in:{today.year+years100}")

Prints =int(input("How many times should I print the message:"))

for i in range(Prints):
    print(name+f" you will be 100 years old in:{today.year+years100}\n")