N=int(input())
if N==1:
    print("BOWWOW")
    exit()
sum_n = N*(N+1)//2
import math
for i in range(2, math.isqrt(sum_n)+1):
    if sum_n%i==0:
        print("BOWWOW")
        exit()
print("WANWAN")