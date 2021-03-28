S=input().rstrip()
ll = len(S)

def check(s,e,S):
    for i in range(s,e):
        if S[i] != S[e-i-1]:
            return False
    return True
flag = check(0,ll,S) and check(0,len(S[:(ll-1)//2]),S[:(ll-1)//2]) and check((ll+3)//2 -1, len(S[(ll+3)//2 -1]) , S[(ll+3)//2 -1])
print("Yes" if flag else "No")