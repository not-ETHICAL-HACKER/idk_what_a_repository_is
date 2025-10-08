from time import sleep,perf_counter

def fib(x):
    a=0
    b=1
    n=0
    c=perf_counter()
    while a<x:
        print(n,".",a)
        sleep(0)
        n+=1
        a,b=b,b+a
    d=perf_counter()
    e=d-c
    print(e,"seconds")
fib(10**10000)
