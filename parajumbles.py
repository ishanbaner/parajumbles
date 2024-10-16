import random
import numpy as np
import os

def cleaning(sent):
    ns=''
    for i in sent:
        if i!='\n':
            ns+=i
    return(ns)

file=open('\path','r')  # Replace '\path' with the path to the essays file in your computer 
content=file.read()
content=content.split('.')
score=0
rd='1'
count=0
while rd=='1':
    os.system('clear')
    jumb={}
    sents=[]
    st=random.randint(0,len(content)-5)
    for k in range(st,st+4):
        sents+=[cleaning(content[k])]
    #sents=[cleaning(x) for x in sents]
    jum=np.random.permutation(4)
    for i in range(4):
        print(i+1," ",sents[jum[i]])
        jumb[sents[jum[i]]]=i+1
    answer=''
    for t in range(4):
        answer+=str(jumb[sents[t]])
    answer=int(answer)

    inp=int(input())
    if inp==answer:
        print('Correct!')
        score+=1
    else:
        print('Wrong')
    count+=1
    print("Your answer:",inp)
    print("Correct answer:",answer)

    for i in range(len(sents)):
        print(sents[i])

    print("Press 1 to continue, any key to stop")
    rd=input()
print("Score:",score,'/',count)
