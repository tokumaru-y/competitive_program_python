# https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_e
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
if len(list(set(A))) != N:
    print(-1)
    exit()
compress = {x: ind+1 for ind, x in enumerate(list(sorted(A)))}
tree = BIT(N)
ans = 0
for i in range(N):
    cnt = i - tree.sum(compress[A[i]])
    ans += cnt * A[i]
    tree.add(compress[A[i]], 1)
print(ans)