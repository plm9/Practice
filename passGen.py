import numpy as np 
from nltk.corpus import words

wordslist=words.words()

bigWords=[]
for i in range(len(wordslist)):
    if  len(wordslist[i])>4 and len(wordslist[i])<10:
        bigWords.append(wordslist[i])

SPdictionary={"s":"$","o":"0","e":"3","a":"@","l":"1","c":"<"}
SpecialChar=["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","'","<",">",".","?","/"]

def weak1():
    keywords=np.random.choice(bigWords,2+1)
    passez="".join(keywords)

    rndidx=np.random.choice(np.arange(0,len(passez)),4)

    for i in rndidx:
        passez=passez.replace(passez[i],passez[i].upper(),1)

    for let,sp in SPdictionary.items():
        if let in passez:
            passez=passez.replace(let,sp)

    return passez

def weak2():
    keywords=np.random.choice(bigWords,4)
    spch=np.random.choice(SpecialChar,4)
    permpass=""
    for wrd,sp in zip(keywords,spch):
        permpass+=wrd+sp
    passez=permpass

    rndidx=np.random.choice(np.arange(0,len(passez)),6)

    for i in rndidx:
        passez=passez.replace(passez[i],passez[i].upper(),1)

    for let,sp in SPdictionary.items():
        if let in passez:
            passez=passez.replace(let,sp)

    return passez

def weakHardcore():
    keywords=np.random.choice(bigWords,6)
    spch=np.random.choice(SpecialChar,6)
    permpass=""
    for wrd,sp in zip(keywords,spch):
        permpass+=wrd+sp
    passez=permpass

    rndidx=np.random.choice(np.arange(0,len(passez)),8)

    for i in rndidx:
        passez=passez.replace(passez[i],passez[i].upper(),1)

    for let,sp in SPdictionary.items():
        if let in passez:
            passez=passez.replace(let,sp)

    return passez


while True:
    cmplx=input("Choose the complexity of the password [1 ,2, Hardcore]")
    if cmplx=="1":
        print(weak1())
        break
    elif cmplx=="2":
        print(weak2())
        break 
    elif cmplx=="Hardcore":
        print(weakHardcore())
        break
    else:
        print("Wrong choice")




