import string
N=int(input())
ans = []
lis = string.ascii_lowercase
while N!=0:
    N-=1
    tmp = N%26
    ans.append(lis[tmp])
    N//=26
ans.reverse()
print(''.join(ans))