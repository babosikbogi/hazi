import numpy as np

def insert(num):
    m=np.chararray((100,100),unicode=True)
    m[:]="~"
    counter=0
    for i in range(1,96,4):
        for j in range(1,96,4):
            if counter<num:
                for k1 in range(i,i+3):
                    for k2 in range(j,j+3):
                        m[k1,k2]='O'
                counter+=1
    print(m)
    return

def max():
    num = int(input("Szigetek szama: "))
    if num > 24 * 24:
        raise ValueError("A maximum szigetek száma, 576!")
    if num<577:
        insert(num)
max()