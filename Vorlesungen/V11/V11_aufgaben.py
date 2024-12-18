import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams.update({'font.size': 28})

size=(100,100)
field=np.random.randint(0,2,size)

fig=plt.figure()
im=plt.imshow(field, animated=True)

def update_plot(i, field, im, plt):
    plt.title("Generation {0:d}".format(i))
    temp=np.zeros(size, dtype=int)
    for x in range(size[0]):
        for y in range(size[1]):
            s=np.sum(field[max(0,x-1):min(size[0],x+2), max(0,y-1):min(size[1],y+2)])
            if (field[x,y]==0 and s==3) or (field[x,y]==1 and 3<=s<=4):
                temp[x,y]=1
            else:
                temp[x,y]=0
    field[:,:]=temp[:,:]
    im.set_array(field)

Anim=animation.FuncAnimation(fig, update_plot, 1000, fargs=(field, im, plt), interval=1)
plt.show()