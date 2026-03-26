import pickle
import time
import random


def line_word(file: str):
    with open(file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            print(f"Line {str(i):2s} : {len(line):5d}")


# line_word("misc\\Quotes.txt")


def Input(Id: int, name: str, members: int, duration: int):
    with open("misc\\clubs.pkl", "ab") as f:
        pickle.dump([Id, name, members, duration], f)


def update(Id: int, name: str, members: int, duration: int):
    with open("misc\\clubs.pkl", "rb+") as f:
        try:
            while True:
                pos = f.tell()
                rec = pickle.load(f)
                if int(rec[-1]) >= 3:
                    f.seek(pos)
                    pickle.dump([Id, name, members, duration], f)
        except EOFError:
            ...


def display(members: int):
    with open("misc\\clubs.pkl", "rb") as f:
        try:
            while True:
                rec = pickle.load(f)
                if int(rec[2]) == members:
                    print(rec)
        except EOFError:
            ...


for i in range(100):
    Input(i, f"club{i}", abs(round(random.gauss(10, 1))),
          abs(round(random.gauss(1, 5))))
print("Before update")
display(10)
for i in range(100):
    update(i, f"club{i}", abs(round(random.gauss(10, 1))),
           abs(round(random.gauss(1, 5))))
print("After update")
display(10)
