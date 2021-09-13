def devisor(num):
    """numの約数を列挙する 1を含む"""
    import math
    res = []
    for i in range(1,int(math.sqrt(num)+1) + 1):
        if num%i==0:
            res.append(i)
            if i != num//i:res.append(num//i)
    return res

def prime_factorize(num, dict=None):
    """numを素因数分解する"""
    import math
    dict = {} if dict is None else dict
    origin = num
    for i in range(2, int(math.sqrt(origin))+1):
        if num%i==0:
            while num%i==0:
                dict[i]+=1
                num//=i
    if num != 1:
        dict[num] +=1
    return dict