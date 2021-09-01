from collections import defaultdict
from heapq import heapify,heappop,heappush
import sys
input = sys.stdin.readline
def solve():
    N=int(input())
    rights=defaultdict(list)
    for _ in range(N):
        l,r = list(map(int, input().split()))
        rights[l].append(r)
    set_ind = 0
    set_list = [x for x in rights.keys()]
    set_list.append(float("inf"))
    set_list.sort()
    target_box = set_list[0]
    h = []
    is_ok = True
    next_in_value = set_list[set_ind]
    while set_ind < len(set_list)-1:
        set_ind+=1
        next_in_value=set_list[set_ind]
        for r in rights[target_box]:
            heappush(h, r)
        while len(h) > 0 and next_in_value > target_box:
            pop_num = heappop(h)
            if pop_num < target_box:
                is_ok=False
                break
            target_box+=1
        target_box = next_in_value
    if is_ok:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()