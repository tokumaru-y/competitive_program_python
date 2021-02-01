n,x=list(map(int,input().split()))
s=input().rstrip()
for c in s:
    x = max(0,x-1) if c=='x' else x+1
print(x)