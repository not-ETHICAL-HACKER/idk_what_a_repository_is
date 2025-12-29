with open("DONT TOUCH\\gooofy.py","w") as f:
    f.write("i = int(input('enter a number: '))")
    for i in range(10**6):
        f.write(f"\ni+=i")
    f.write("\nprint(i)")