T=int(input())
for _ in range(T):
    a,b,c=list(map(int, input().split()))
    ans = 0
    cnt_b = b//2
    add = 0
    if b>=2 and (a>=2 or c>=1):
        need = cnt_b
        if need >= c:
            add += c
            need -= c
            c = 0
        else:
            c -= need
            add += need
            need =0
        if need >0:
            if need*2 >= a:
                add += a//2
                a -= need*2
            else:
                a -= need*2
                add += need
    if c > 0 and a > 0:
        if c//2 > 0:
            if c//2 >= a:
                add += a
                a=0
            else:
                a -= c//2
                add += c//2
            c = 1 if c%2==1 else 0
        if a <= 0:
            print(add)
            continue
        if c > 0:
            if c*3 >= a:
                add += a//3
                a-=c*3
            else:
                add += c
                a -= c*3
    if a>0:
        add += a//5
    print(add)

