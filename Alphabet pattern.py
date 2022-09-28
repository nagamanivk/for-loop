from re import A, I


# A
# B C
# C D E 
# D E F G
# E F G H I:

n=int(input("enter the no:"))
for i in range (n):
    k=ord("A")+i
    for j in range (i+1):
        print(chr(k),end=" ")
        k=k+1
    print()