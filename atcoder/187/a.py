import sys
import sys
import math
sys.setrecursionlimit(10**9)
a,b=input().split()
sum_a=sum(list(map(int,a)))
sum_b=sum(list(map(int,b)))
print(max(sum_a,sum_b))