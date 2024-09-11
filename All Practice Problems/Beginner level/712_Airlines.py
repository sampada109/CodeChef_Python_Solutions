# cook your dish here
import math

t = int(input())

for i in range(t):
    
    a,b = map(int, input().split())
    
    r = math.ceil(b/100)
    
    if(r > a):
        print(r-a)
    else:
        print(0)
