from sys import stdin
import math

def solve(n):
    res=0
    for i in range(1,n+1,2):
        cnt=0
        for j in range(1,int(math.sqrt(i)+1)):
            if i % j == 0:
                if j == i//j:
                    cnt+=1
                else:
                    cnt+=2
        else:
            if cnt == 8:
                res+=1
    return res
if __name__ == "__main__":
    n=int(input())
    ans=solve(n)
    print(ans)