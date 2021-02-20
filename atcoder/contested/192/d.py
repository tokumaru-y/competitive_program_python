import math
X=input().rstrip()
M=input()
m=0
for x in X:
    m=max(m,int(x))
if len(X) < len(M):
    right = 2**(len(X)-len(M))
    left = m
    for i in reversed(range(left,right+1)):
        tmp = 0
        for ss,x in enumerate(reversed(X)):
            tmp+=i**(ss)*int(x)
        if tmp<=int(M):
            print(i-m)