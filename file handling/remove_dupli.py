def dupl(txt:list[str])->str:
    fin:list[str] = []
    for word in txt:
        if word not in fin:
            fin.append(word)
    return " ".join(fin)

def file_dupe(file:str):
    with open(file,"r+") as f:
        try:
            while True:
                pos = f.tell()
                line = f.readline()
                f.seek(pos)
                f.write(dupl(line.split()))
        except EOFError:
            pass

file_dupe("file handling\\q1_updated.txt")