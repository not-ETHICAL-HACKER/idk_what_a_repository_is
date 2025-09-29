def golden_ratio (limit:int=1):
    a,b=1,1
    l1=[]
    l2=[]
    while limit>a:
        print(a)
        l1.append(a)
        l2.append(b)
        s1=sum(l1)
        s2=sum(l2)
        g_r=s2/s1
        a,b=b,b+a
    print(f"the golden ratio(approx)is:{g_r}")
    return g_r
import math
golden_rati = (1 + math.sqrt(5)) / 2
a=int(input("enter a limit for the calculations:"))
c=golden_ratio(a)
print(f"actuall golden ratio is{golden_rati}")
print(f"accurcy is {(c/golden_rati)*100}%")
import matplotlib

