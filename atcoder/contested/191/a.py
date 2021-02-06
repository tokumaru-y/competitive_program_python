v,t,s,d=list(map(int,input().split()))
print("No" if v*t <= d <= v*s else "Yes")