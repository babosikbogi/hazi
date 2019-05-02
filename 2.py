import sys

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input("adjon meg egy számot: "))
lst=[2]

for i in range(3,sys.maxsize):
    if prime(i):
        lst.append(i)
        if len(lst)==n:
            print(lst[n-1])
            break
