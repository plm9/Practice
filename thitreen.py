
def FibonacciGen(num):
    fibList=[1]
    fst=0
    scnd=1
    count=1
    while count<num:
        nxt=fst+scnd
        fibList.append(nxt)
        fst=scnd
        scnd=nxt
        count+=1
        
    return fibList



num=int(input("How many Fibonacci number you want? "))
print(FibonacciGen(num))