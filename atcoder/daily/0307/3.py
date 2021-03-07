N,K=list(map(int,input().split()))
num=N
for _ in range(K):
    tmp_str=sorted(str(num))
    x = int(''.join(tmp_str))
    y = int(''.join(reversed(tmp_str)))
    num = y - x
print(num)