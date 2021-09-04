def solve():
    from bisect import bisect_left,insort_left,bisect
    import sys
    input = sys.stdin.readline
    L,Q=list(map(int, input().split()))
    bs = [L]
    for _ in range(Q):
        c,x = list(map(int, input().split()))
        if c == 1:
            insort_left(bs, x)
        else:
            idx = bisect(bs, x)
            ans = bs[idx] - bs[idx-1] if idx>0 else bs[idx]
            print(ans)

if __name__ == "__main__":
    solve()