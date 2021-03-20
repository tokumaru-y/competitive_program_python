N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
passed = [-1] * N
passed[0] = 0
def search(top):
    next = A[top] - 1
    if passed[next]:
        return passed[top] - passed[next] + 1
    passed[next] = A[top] + 1
    search(next)
round_cnt = search(0)
if max(passed) >= K:
    print(passed.index(K)+1)
    exit()

left = K - (passed)