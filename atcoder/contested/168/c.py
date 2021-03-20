import math
A,B,H,M=list(map(int,input().split()))
minutes = 6*M
hour = (H*30+M*(0.5))
if hour > minutes:
    ans = A**2 + B**2 -2*A*B*math.cos(math.radians(hour-minutes))
else:
    ans = A**2 + B**2 -2*A*B*math.cos(math.radians(minutes-hour))
print(math.sqrt(ans))
