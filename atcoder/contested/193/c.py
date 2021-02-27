import math
N=int(input())
if N==1:
    print(1)
elif N==2:
    print(2)
else:
    d = 0
    for i in range(2, math.isqrt(N)+1):
        tmp = i*i
        if math.sqrt(i) >= 2:
            continue
        while tmp <=N:
            tmp*=i
            d+=1
        # a,b=i,N//i
        # if a >= 2:                
        #     for j in range(2,100):
        #         if a**j>N:break
        #         d+=1
        # if b >= 2:
        #     for j in range(2,100):
        #         if b**j>N:break
        #         d+=1
        # print(a,b)
    print(N-d)
    # def factorization(n):
    #     arr = []
    #     temp = n
    #     for i in range(2, int(-(-n**0.5//1))+1):
    #         if temp%i==0:
    #             cnt=0
    #             while temp%i==0:
    #                 cnt+=1
    #                 temp //= i
    #             arr.append([i, cnt])

    #     if temp!=1:
    #         arr.append([temp, 1])

    #     if arr==[]:
    #         arr.append([n, 1])

    #     return arr

    # ll = factorization(N) 
    # ans = N
    # d = 1
    # for num, cnt in ll:
    #     if cnt >= 2:
    #         d *= cnt - 1
    # print(ll)
    # print(ans -d)