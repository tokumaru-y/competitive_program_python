from sys import stdin
import math

def solve(s):
    res=0
    tmp=0
    for c in s:
        if c in ['A','C','G','T']:
            tmp+=1
        else:
            res = max(res,tmp)
            tmp=0
    else:
        res=max(res,tmp)
    return res
if __name__ == "__main__":
    S = stdin.readline().rstrip()
    ans=solve(S)
    print(ans)