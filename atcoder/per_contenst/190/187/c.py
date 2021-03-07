N=int(input())
d={}
S=[input().rstrip() for _ in range(N)]
origin = []
for i,s in enumerate(S):
    origin.append(s)
    d.setdefault(s,i)
for s in origin:
    if s in d and '!'+s in d:
        print(s)
        exit()
print("satisfiable")