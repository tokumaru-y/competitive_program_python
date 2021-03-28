X,Y,A,B,C = list(map(int, input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
apples=a[:X]+b[:Y]
apples.sort()
ci = 0
for i in range(len(apples)):
    if apples[i] < c[ci]:
        apples[i] = c[ci]
        ci += 1
    if ci >= C:break
print(sum(apples))