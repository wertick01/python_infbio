import numpy as np
import time
from numba import jit, cuda
import matplotlib.pyplot as plt

print('\n#5.2')

def M2M(m1,m2):
    s=0
    t=[]
    m3=[]
    if len(m2)!=len(m1[0]):
        print("Матрицы не могут быть перемножены")
        return
    else:
        r1=len(m1)
        c1=len(m1[0])
        c2=len(m2[0])
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0
            m3.append(t)
            t=[]           
    return m3

def MyFunc(matrix):
    for _ in range(100):
        M2M(matrix, matrix)

def NPFunc(matrix):
    for _ in range(100):
        matrix.dot(matrix)

def NPDegreeChoicer():
    np_dct = {}
    for i in range(1, 8):
        npstart_time = time.time()
        matrix = np.random.randint(0, 10, (2**i, 2**i))
        NPFunc(matrix)
        np_dct[i] = time.time() - npstart_time
    return np_dct

@jit(target_backend='cuda')
def DegreeChoicer():
    my_dct = {}
    for i in range(1, 8):
        mystart_time = time.time()
        matrix = np.random.randint(0, 10, (2**i, 2**i))
        MyFunc(matrix)
        my_dct[i] = time.time() - mystart_time
    return my_dct

if __name__=="__main__":
    np_dct = NPDegreeChoicer()

    my_dct = DegreeChoicer()

    print(np_dct, my_dct)

    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(np_dct.keys(), np_dct.values(), c='b',marker="^",ls='--',label='NUMPY',fillstyle='none')
    ax.plot(my_dct.keys(), my_dct.values(), c='g',marker=(8,2,0),ls='--',label='MYFUNC')
    plt.xlabel("Matrix size")
    plt.ylabel("Time spended (seconds)")
    plt.legend(loc=2)
    plt.show()

