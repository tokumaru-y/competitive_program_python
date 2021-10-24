# https://atcoder.jp/contests/joisc2011/tasks/joisc2011_bookshelf
class SegTree:
    # 引用元:https://qiita.com/takayg1/items/c811bd07c21923d7ec69
    """
    Segment Tree
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        初期化

        init_val: 配列の元要素
        ide_ele: 単位元
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新

        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る

        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
N=int(input())
W = [int(input()) for _ in range(N)]
S = [int(input()) for _ in range(N)]
seg = SegTree([0]*(N), max, 0)
ans = 0
sum = 0
for i in range(N):
    sum += W[i]*2
    S[i] -= 1
    seg.update(S[i], seg.query(0,S[i])+W[S[i]]*2)
    ans=max(ans, seg.query(S[i], S[i]+1))
print(sum-ans)