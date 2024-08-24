# cook your dish here

n = int(input())

for i in range(n):
    
    a, m = map(int, input().split())
    
    if( a < 50 ):
        print("Z")
    elif( a >= 50 and m < 50 ):
        print("F")
    else:
        print("A")
