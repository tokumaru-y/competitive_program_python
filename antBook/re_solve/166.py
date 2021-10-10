# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
# 参考コード、解説:https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion
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
btree = BIT(2**20)
N=int(input())
A=list(map(int, input().split()))
ans = 0
sum = 0
for i in range(N):
    btree.add(A[i],1)
    ans += (i+1)-btree.sum(A[i])
print(ans)