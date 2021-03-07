N=int(input())
ans = N
num_list = set()
a=2
b=2
while a**b<=N:
    num_list.add(a**b)
    b+=1
    if a**b>N:
        a+=1
        b=2
print(N-len(num_list))