K=int(input())
S=input().rstrip()
ll = len(S)
if K>=ll:
    print(S)
else:
    print(S[:K]+"...")