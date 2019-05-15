import numpy as np
import random
def lista(ad):
    a=len(ad)
    lista=[1]*a
    for i in range(1,a):
        for j in range(0,i):
            if ad[i]>ad[j] and lista[i]<lista[j]+1:
                lista[i]=lista[j]+1
        maxhely=0
        for i in range(a):
            maxhely=max(maxhely,lista[i])
        return maxhely
ls=np.random.randint(1,10,5)
ls1=np.random.randint(1,10,5)

print(ls)
print(ls1)

print(lista(ls))
print(lista(ls1))