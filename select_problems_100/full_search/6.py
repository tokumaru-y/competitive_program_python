import sys
import math
sys.setrecursionlimit(10**9)
n=int(input())
s=sys.stdin.readline().rstrip()
char_list = '0123456789'
ans=0
for i in char_list:
    for j in char_list:
        for k in char_list:
            index=0
            target_list = [i,j,k]
            for c in s:
                if target_list[index] == c:
                    index+=1
                if index==3:
                    ans+=1
                    break
print(ans)