def alsoharomszogmatrix(M):
    for i in range(0,len(M)):
        for j in range(i+1,len(M)):
            if M[i][j]!=0:
                return False
    return True

M=[[1,0,0],
   [1,1,0],
   [1,1,1]]

if alsoharomszogmatrix(M):
    print("igen ez egy alsó háromszög mátrix")
else:
    print("ez nem egy alsó háromszög mátrix")
