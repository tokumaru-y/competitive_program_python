X=input()
N=int(input())
alf = {}
d=65
for i in range(65, 91):
    x = chr(i)
    y = X[i-d]
    alf[y]=x
origin = []
alf_dict = []
for i in range(N):  
    inp = input()
    origin.append(inp)
    add = ""
    for j in range(len(inp)):
        add+=alf[inp[j]]
    alf_dict.append([add, i])
alf_dict.sort()
for x in alf_dict:
    print(origin[x[1]])