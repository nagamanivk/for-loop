a="mani"
b=5
print("mani ,"*(b-1)+a)

n=int(input("enter the no:"))
for i in range(n,0,-1):
    for j in range (i,0,-1):
        print(i,end="")
    print()
