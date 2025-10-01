import time,threading
n=0 
a="|"
b="\\"
c="-"
d="/"
t=0.05
while True:
    break
    print(a*40)
    time.sleep(t)
    print(b*40)
    time.sleep(t)
    print(c*40)
    time.sleep(t)
    print(d*40)
    time.sleep(t)
def sum(nums,target):
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l.append(i,j)
                    print(l)
        return l
for i in range(10):
    time.sleep(0.5)
    print("hello world\a")