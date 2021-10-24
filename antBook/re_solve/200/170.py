# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D&lang=jp
class BIT:
    """引用元:https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree
    """
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
N=int(input())
A=list(map(int, input().split()))
bit = BIT(max(A)+1)
ans = 0
for i in range(N):
    ans += i - bit.sum(A[i])
    bit.add(A[i],1)
print(ans)