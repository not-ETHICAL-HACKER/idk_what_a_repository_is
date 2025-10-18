s="bananas"
count={}
for ch in s:
    count[ch]=count.get(ch,0)+1
print(count)
