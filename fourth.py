import numpy as np

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

""" Main task """
lister=[]
if len(a)<len(b):
    
    for k in a:
        if (k in b) and (k not in lister):
            lister.append(k)
else:
    for k in b:
        if (k in a) and (k not in lister):
            lister.append(k)

print( lister)

""" First Extra """
rndLen1=np.random.randint(10)
rndLen2=np.random.randint(10)

RndA=np.random.randint(10,size=rndLen1)
RndB=np.random.randint(10,size=rndLen2)

lister=[]
if len(RndA)<len(RndB):
    
    for k in RndA:
        if (k in RndB) and (k not in lister):
            lister.append(k)
else:
    for k in RndB:
        if (k in RndA) and (k not in lister):
            lister.append(k)

print("RndA:", RndA)
print("RndB:", RndB)
print( lister)

""" Second Extra """
print(list(set([x for x in a if x in b])))