# cook your dish here

t = int(input())

for i in range(t):
    
    n = int(input())
    
    good = True
    
    s = list(map(int, input().split()))
    
    for j in s:
        
        if( j <= 4 ):
            good = False
            
    if(good):
        print("YES")
    else:
        print("NO")
