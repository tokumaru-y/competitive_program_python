# https://algo-method.com/tasks/332/editorial
import math
A,B=list(map(int, input().split()))
s_b = int(math.sqrt(B))
prime_list = [True] * (s_b+1)
prime_list[0]=False
prime_list[1]=False
dif_prime_list = [True] * (B-A+1)
for i in range(2, s_b+1):
    if not prime_list[i]:continue
    tmp = i + i
    while tmp * tmp <= B:
        prime_list[tmp] = False
        tmp += i
    start = (A + (i - 1))//i * i
    if start == i:start += start
    while start <= B:
        dif_prime_list[start- A] = False
        start += i
print(sum(dif_prime_list))