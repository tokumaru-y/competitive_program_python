from sys import stdin
import math

def solve(n,m,sings):
    res=0
    for i in range(m):
        for j in range(i+1,m):
            tmp=0
            for line in range(n):
                tmp+=max(sings[line][i],sings[line][j])
            else:
                res=max(res,tmp)
    return res

if __name__ == "__main__":
    n,m = [int(x) for x in stdin.readline().rstrip().split()]
    sings=[]
    for _ in range(n):
        sings.append([int(x) for x in stdin.readline().rstrip().split()])
    ans=solve(n,m,sings)
    print(ans)