# https://atcoder.jp/contests/arc017/tasks/arc017_1
def devisor(num):
    """numの約数を列挙する 1を含む"""
    import math
    res = []
    for i in range(2,int(math.sqrt(num)+1) + 1):
        if num%i==0:
            res.append(i)
            if i != num//i:res.append(num//i)
    return res
N=int(input())
div = devisor(N)
print("YES" if len(div) == 0 else "NO")