from sys import stdin


def solve(n,x):
    res=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            left = x-(i+j)
            if (left>i and left > j and left<=n):
                res+=1
    return res

if __name__ == '__main__':
    while True:
        n,x = [ int(x) for x in stdin.readline().rstrip().split()]
        if n==0 and x==0:
            break
        ans = solve(n,x)
        print(ans)