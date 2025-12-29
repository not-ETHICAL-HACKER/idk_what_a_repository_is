def fib_rec(lim:int)->int:
    if lim in (1,2):
        return 1
    else:
        return fib_rec(lim-1)+fib_rec(lim-2)
def fib(lim:int)->int:
    a,b=0,1
    for _ in range(lim):
        a,b=b,a+b
    return a
print(fib_rec(10),fib(10))