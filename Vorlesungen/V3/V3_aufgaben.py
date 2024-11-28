import numpy as np
import random

while True:
    a_shape=(10,10)
    a=np.zeros(a_shape, dtype=str)
    for i in range(a_shape[0]):
        for j in range(a_shape[1]):
            a[i,j]=chr(random.randint(ord('A') , ord('Z')))

    word=str.upper(input("Word: "))
    if (len(word) <= a_shape[0]) and (len(word) <= a_shape[1]):
        try:
            start_x=random.randint(0, a_shape[1]-1-len(word))
        except:
            start_x=0
        try:
            start_y=random.randint(0, a_shape[0]-1-len(word))
        except:
            start_y=0
        direction=random.randint(0,1)
        if direction==0:
            for i in range(len(word)):
                a[start_y,start_x+i]=word[i]
        else:
            for i in range(len(word)):
                a[start_y+i,start_x]=word[i]
        print(a)
    else:
        print("Word too long.")