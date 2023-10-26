
nunber=int(input("Lets see your number:"))


dividers=[]
for x in range(2,nunber):
    if nunber%x==0:
        dividers.append(x)

print(len(dividers))

""" My extra: Find prime numbers between 0 and 100 """

prime=[]
for k in range(100):
    dividerspr=[]
    for x in range(2,k):
        if k%x==0:
            dividerspr.append(x)

    if len(dividerspr)==0:
        prime.append(k)
    del dividerspr

print(prime)