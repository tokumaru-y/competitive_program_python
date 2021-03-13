A,B,W=list(map(int,input().split()))
W*=1000
mmin = float('inf')
mmax = 0
for i in range(1,1000001):
    if A*i <= W and W <= B*i:
        mmin = min(mmin, i)
        mmax = max(mmax, i)
if mmax ==0:
    print("UNSATISFIABLE")
else:
    print(mmin,mmax)