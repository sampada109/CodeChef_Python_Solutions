import math

t = int(input())
for i in range(t):
    n = int(input())
    c = n*(0.2)                    #20% commision on each insurance
    print(math.ceil(100/c))        # min no. of insurance to earn atleat 100 dollars
