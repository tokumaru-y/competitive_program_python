class LazySegTree:
    # 参考:https://tsutaj.hatenablog.com/entry/2017/03/30/224339
    """
    Segment Tree
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        初期化

        init_val: 配列の元要素
        ide_ele: 単位元
        """
        self.leaf_size = len(init_val)
        self.num = 1
        while self.num < self.leaf_size:self.num *= 2
        self.tree = [0] *(2*self.num-1)
        self.lazy = [0] * (2*self.num - 1)
        for i in range(self.leaf_size):
            self.tree[i+self.leaf_size-1] = init_val[i]
        for i in range(self.num-2,0,-1):
            self.tree[i] = self.tree[i*2+1] + self.tree[i*2+2]

    
    def eval(self, k, l, r):
        """k番目のノードについて遅延評価を行う"""
        if (self.lazy[k] != 0):
            self.tree[k] += self.lazy[k]
            if r-l > 1:
                self.lazy[2*k+1] += self.lazy[k] / 2
                self.lazy[2*k+2] += self.lazy[k] / 2
            self.lazy[k] = 0

    def add(self, a, b, x, k=0, l=0, r=-1):
        """[a, b)にXの値を加える
        a: index(0-index)　更新したい範囲の左端
        b: index(0-index)　更新したい範囲の右端
        x: integer 
        k: index(0-index)  ノード番号
        l: index(0-index)　現在のノードの扱う範囲（左端）
        r: index(0-index)　現在のノードの扱う範囲（右端）
        """
        if r<0:r = self.num
        self.eval(k, l, r)
        if b <= l or r <= a:return
        
        if a <= l and r<= b:
            self.lazy[k] += (r-l) * x
            self.eval(k, l, r)
        else:
            self.add(a, b, x, 2*k+1, l, (l+r)//2)
            self.add(a, b, x, 2*k+2, (l+r)//2, r)
            self.tree[k] = self.tree[2*k+1] + self.tree[2*k+2]
    
    def get_sum(self, a, b, k=0, l=0, r=-1):
        if r<0:r=self.num
        self.eval(k, l, r)
        if b<= l or r <= a:return 0
        if a<= l and r<= b:
            return self.tree[k]
        left_value = self.get_sum(a, b, 2*k+1, l, (l+r)//2)
        right_value = self.get_sum(a, b, 2*k+2, (l+r)//2, r)
        return left_value + right_value

class RMQLazySegTree:
    # 参考:https://tsutaj.hatenablog.com/entry/2017/03/30/224339
    """
    Segment Tree
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        初期化

        init_val: 配列の元要素
        ide_ele: 単位元
        """
        self.ide_ele = ide_ele
        self.leaf_size = len(init_val)
        self.num = 1
        while self.num < self.leaf_size:self.num *= 2
        self.tree = [0] *(2*self.num-1)
        self.lazy = [0] * (2*self.num - 1)
        self.segfunc = segfunc
        for i in range(self.leaf_size):
            self.tree[i+self.leaf_size-1] = init_val[i]
        for i in range(self.num-2,0,-1):
            self.tree[i] = self.segfunc(self.tree[i*2+1], self.tree[i*2+2])

    
    def eval(self, k, l, r):
        """k番目のノードについて遅延評価を行う"""
        if (self.lazy[k] != 0):
            self.tree[k] += self.lazy[k]
            if r-l > 1:
                self.lazy[2*k+1] += self.lazy[k]
                self.lazy[2*k+2] += self.lazy[k]
            self.lazy[k] = 0

    def add(self, a, b, x, k=0, l=0, r=-1):
        """[a, b)にXの値を加える
        a: index(0-index)　更新したい範囲の左端
        b: index(0-index)　更新したい範囲の右端
        x: integer 
        k: index(0-index)  ノード番号
        l: index(0-index)　現在のノードの扱う範囲（左端）
        r: index(0-index)　現在のノードの扱う範囲（右端）
        """
        if r<0:r = self.num
        self.eval(k, l, r)
        if b <= l or r <= a:return
        
        if a <= l and r<= b:
            self.lazy[k] += x
            self.eval(k, l, r)
        else:
            self.add(a, b, x, 2*k+1, l, (l+r)//2)
            self.add(a, b, x, 2*k+2, (l+r)//2, r)
            self.tree[k] = self.segfunc(self.tree[2*k+1], self.tree[2*k+2])
    
    def query(self,a, b, k=0, l=0, r=-1):
        if r<0:r=self.num
        self.eval(k,l,r)
        if r<=a or b<=l:
            return self.ide_ele
        elif a<=l and r<=b:
            return self.tree[k]
        else:
            left_value = self.query(a, b, 2*k+1, l, (l+r)//2)
            right_value = self.query(a, b, 2*k+2, (l+r)//2, r)
            return self.segfunc(left_value, right_value)