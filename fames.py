import random


def common(name1:str,name2:str)->str:
    l:list[str] = []
    for ch in name1:
        if name1.count(ch)>name2.count(ch) and ch not in l:
            l.append(ch)
    return ''.join(l)
def cross(name1:str,name2:str,key:str)->str:
    l:list[str] = list(key)
    name1,name2=common(name1,name2),common(name2,name1)
    print(name1,name2)
    n = len(name1)+len(name2)
    while l:
        print(l)
        if len(l)==1:
            return l[0]
        l.pop((len(l)-1)%n)
    return ""
# print(cross("dhinesh","dhaksesh","flames"))
for i in range(1000):
    r = random.gauss(0,10)
    if r>25:
        print(r)