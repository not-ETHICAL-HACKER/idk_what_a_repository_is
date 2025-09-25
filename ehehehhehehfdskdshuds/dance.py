def sqr(year:int):
    if (year)**0.5 in range(1000):
        print(f"{year} is a perfect square year")
    else:
        nxt_sqr=(int(((year)**0.5+1))**2)
        print(f"{year} is not perfect square.\nNext perfect square year is {nxt_sqr}")
while True:
    sqr(int(input("enter a year:")))