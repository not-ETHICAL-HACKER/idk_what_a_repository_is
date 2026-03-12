from time import sleep
from random import choices
def matrix(chars:str):
    n = len(chars)
    res = "".join(choices(list(chars), k=n))
    inv = res
    ind = 0
    for i in range(n):
        for j in range(32,255):
            
            inv = res[:i] + chr(j) + res[i+1:]
            res = inv
            if chr(j) == chars[ind]:
                ind += 1
                res = res[:i] + chars[ind-1] + res[i+1:]
                break
            print(inv,end="\r")
            sleep(1/240)
    
matrix(open("garbage.txt",encoding="utf-8").read()[:50])