X=int(input())
import math
def is_prime(x):
    if x == 1:return False
    for i in range(2,math.isqrt(x)+1):
        if x%i==0:return False
    return True
while not is_prime(X):X+=1
print(X)
