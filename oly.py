import csv

def oly():
    with open("Oly.csv") as f:
        read = csv.reader(f)
        country = input("e")
        for rec in read:
            if country.lower() == rec[0].lower():
                print(int(rec[1]) + int(rec[2]) + int(rec[3]))
                break
            else:
                print("Country not found.")

with open("Oly.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Country", 1, 2, 3])
oly()