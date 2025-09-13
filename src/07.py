i = str(input())
q,w=0,0
for t in range(len(i)):
    if i[t].upper() == i[t]:
        q = t
        break

for t in range(len(i)):
    if i[t] in ['0',"1","2","3","4","5",'6',"7","8","9"]:
        w = t+1
        break
print(i[q:len(i):w-q])