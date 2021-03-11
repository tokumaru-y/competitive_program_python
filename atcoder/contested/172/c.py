import string
N=int(input())
ans=''
alp = string.ascii_letters
while N!=0:
    N-=1
    ans+=alp[N%26]
    N//=26
print(''.join(list(reversed(ans))))