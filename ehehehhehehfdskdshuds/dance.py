def fac(x:int):
    if x==1:
        return 1
    else:
        return x*fac(x-1)
def gold_r(x:int|None = 1,n:int|None = 1):
    nn=0
    sign=1
    l=[]
    for i in range(1,n+1):
        a=(x**nn)/fac(n)*sign
        l.append(a)
        sign*=-1
        nn+=1
        print(sum(l))
    print(l)
a=int(input("enter1:"))
b=int(input("enter2:"))
gold_r(a,b)

