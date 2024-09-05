# cook your dish here

import math

t = int(input())

for i in range(t):
    
    amount , friend = map(int, input().split())
    
    repair = math.floor(amount//(friend+1))
    
    print( amount - friend*repair )
