with open("recursive_1.py","w") as f:
    f.write("c = 0\n")
    for i in range(65, 91):
        f.write(f"def {chr(i)}()->None:\n")
        f.write(f"\tc = c + 1\n\t{chr(i+1)+"()" if i < 90 else 'print(\"Hello, World!\")'}\n")


