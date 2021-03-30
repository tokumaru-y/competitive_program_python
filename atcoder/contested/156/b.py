N,K=list(map(int,input().split()))
def gcd(x,y,cnt):
    cnt+=1
    if y==0:return cnt
    return gcd(y,x%y,cnt)
print(gcd(N,K,0))