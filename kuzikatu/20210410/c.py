N=int(input())
A=list(map(int, input().split()))
dif = 1
for a in A:
    dif *= 1 if a%2==1 else 2
cnt = 3**N
print(cnt-dif)