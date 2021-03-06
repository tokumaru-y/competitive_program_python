N=int(input())
A=list(map(int,input().split()))
m_num=max(A)
prime = [True]*(m_num+1)
num_list = [0]*(m_num+1)
def GCD(x,y):
    if y==0:
        return x
    return GCD(y,x%y)
for a in A:
    num_list[a]+=1
coprime = True
for i in range(2,m_num+1):
    if not prime[i]:continue
    tmp_sum = 0
    for j in range(i,m_num+1,i):
        prime[j]=False
        tmp_sum+=num_list[j]
    if tmp_sum > 1 :
        coprime=False
if coprime:
    print("pairwise coprime")
    exit()
g = 0
for a in A:
    g = GCD(g,a)
if g==1:
    print("setwise coprime")
else:
    print("not coprime")