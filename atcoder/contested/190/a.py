a,b,c=list(map(int,input().split()))
ans=a-b
if ans==0:
    print("Takahashi" if c==1 else "Aoki")
else:
    if ans > 0:
        print("Takahashi")
    else:
        print("Aoki")