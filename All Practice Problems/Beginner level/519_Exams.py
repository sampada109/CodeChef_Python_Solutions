# cook your dish here

n = int(input())

for i in range(n):
    
    sch,std,pas = map(int, input().split())
    
    tt_std = sch * std
    
    pas_per = (pas / tt_std) * 100
    
    if( pas_per > 50 ):
        print("YES")
    
    else:
        print("NO")
