import numpy as np
import time
from numba import jit, cuda

print('\n#5.2')

def M2M(m1,m2):
    s=0
    t=[]
    m3=[]
    if len(m2)!=len(m1[0]):
        print("Матрицы не могут быть перемножены")
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
    res = matrix
    for _ in range(100):
        res = M2M(res, matrix)
    return res

def NPFunc(matrix):
    res = matrix
    for _ in range(100):
        res = res.dot(matrix)
    return res

def NPDegreeChoicer():
    for i in range(1, 8):
        matrix = np.random.randint(0, 10, (2**i, 2**i))
        res = NPFunc(matrix)
    return res

@jit(target_backend='cuda')
def DegreeChoicer():
    for i in range(1, 8):
        matrix = np.random.randint(0, 10, (2**i, 2**i))
        res = MyFunc(matrix)
    return res

if __name__=="__main__":
    npstart_time = time.time()
    _ = NPDegreeChoicer()
    npworktime = time.time() - npstart_time
    print("Time for NumPy func:", npworktime)

    start_time = time.time()
    _ = DegreeChoicer()
    worktime = time.time() - start_time
    print("Time for my func on GPU:", worktime)
