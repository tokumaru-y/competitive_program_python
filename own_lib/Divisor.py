def devisor(num):
    """numの約数を列挙する 1を含む"""
    import math
    res = []
    for i in range(1,int(math.sqrt(num)+1) + 1):
        if num%i==0:
            res.append(i)
            if i != num//i:res.append(num//i)
    return res