import time
n=0 
while True:
    n+=1
    print("|")
    time.sleep(0.1)
    print("\\")
    time.sleep(0.1)
    print("-")
    time.sleep(0.1)
    print("/")
    time.sleep(0.1)
    if n==25:
        n=0
        print("\n"*25)