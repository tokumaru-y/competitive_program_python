N=int(input())
A=list(map(int,input().split()))
def gcd(x,y):
    if y==0:
        return x
    return gcd(y, x%y)

coprime = True
num_list = [0]*N
for a in A:
    num_list[a]+=1