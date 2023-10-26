import numpy as np

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

arr=np.array(a)
""" Main task """
for i in a:
    if i<5:
        print(i)

""" First extra """
less5=[]
for i in a:
    if i<5:
        less5.append(i)
print(less5)

""" Second extra """
print(arr[arr<5])

""" Third extra """
thress=int(input("Gimme a thresshold"))
print(arr[arr<thress])
