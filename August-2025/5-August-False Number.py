# cook your dish here
for _ in range(int(input())):
    l=list(input())
    if l[0]=="1":
        print(10,end="")
        for i in range(1,len(l)):
            print(l[i],end="")
    else:
        print(1,end="")
        for i in range(len(l)):
            print(l[i],end="")
    print()   
